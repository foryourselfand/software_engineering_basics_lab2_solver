import os
import re
import zipfile
from argparse import ArgumentParser
from argparse import Namespace
from dataclasses import dataclass
from filecmp import dircmp
from json import JSONDecodeError
from json import loads
from typing import Dict
from typing import List
from typing import Optional
from typing import Set
from typing import Union

import requests
from icecream import ic


@dataclass
class Commit:
    index: int
    branch: str
    user: str
    branch_to_merge: Optional[str] = None


Task = Dict[str, Dict[str, Union[int, str, List[int], Dict[str, Union[int, str]]]]]
Commits = Dict[int, Commit]
Solution = List[str]


def get_args() -> Namespace:
    parser = ArgumentParser()
    required = parser.add_argument_group('required named arguments')
    required.add_argument('-v', '--variant', required=True, help='variant number', type=int)
    required.add_argument('-j', '--jsessionid', required=True, help='JSESSIONID from cookies', type=str)
    required.add_argument('-p', '--p_auth', required=True, help='p_auth from params', type=str)
    return parser.parse_args()


def get_task(args: Namespace) -> Task:
    params = {
        'p_p_id': 'selab2_WAR_seportlet',
        'p_p_lifecycle': '1',
        'p_p_state': 'normal',
        'p_p_mode': 'view',
        '_selab2_WAR_seportlet_javax.portlet.action': 'getBranches',
        'p_auth': args.p_auth,
    }
    
    data = {
        'variant': args.variant
    }
    
    cookies = {
        'JSESSIONID': args.jsessionid,
    }
    
    response = requests.post('https://se.ifmo.ru/courses/software-engineering-basics', params=params, data=data, cookies=cookies)
    
    json_raw: str = response.text
    json_correct = re.sub(r'br_(\d+) ', r'"br_\1" ', json_raw)
    try:
        return loads(json_correct)
    except JSONDecodeError:
        exit('check JSESSIONID from cookies and p_auth from params')


def extract_commit(args: Namespace, commit_index: int) -> None:
    params = {
        'p_p_id': 'selab2_WAR_seportlet',
        'p_p_lifecycle': '2',
        'p_p_state': 'normal',
        'p_p_mode': 'view',
        'p_p_cacheability': 'cacheLevelPage',
    }
    
    data = {
        'variant': args.variant,
        'commit': commit_index
    }
    
    cookies = {
        'JSESSIONID': args.jsessionid,
    }
    
    response = requests.post('https://se.ifmo.ru/courses/software-engineering-basics', params=params, data=data, cookies=cookies)
    
    dir_base = f'res/{args.variant}'
    dir_zips = f'{dir_base}/zips'
    dir_commits = f'{dir_base}/commits'
    name_commit = f'commit{commit_index}'
    filename_zip = f'{dir_zips}/{name_commit}.zip'
    dir_commit_extracted = f'{dir_commits}/{name_commit}/'
    
    os.makedirs(dir_zips, exist_ok=True)
    os.makedirs(dir_commits, exist_ok=True)
    
    with open(f'{filename_zip}', 'wb+') as zip_file:
        zip_file.write(response.content)
    
    with zipfile.ZipFile(f'{filename_zip}', 'r') as zip_reference:
        zip_reference.extractall(f'{dir_commit_extracted}')


def get_commits(task: Task) -> Commits:
    commits: Commits = {}
    
    for branch, values in task.items():
        user_int = values['user']
        user_str = 'red' if user_int == 0 else 'blue'
        for commit_index in values['commits']:
            commit_current = Commit(index=commit_index, branch=branch, user=user_str)
            commits[commit_index] = commit_current
    
    for branch_to_merge, values in task.items():
        merge_value: Dict[str, Union[int, str]] = values.get('merge', None)
        if merge_value is None:
            continue
        commit_to_merge: int = merge_value['commit']
        commits[commit_to_merge].branch_to_merge = branch_to_merge
    return commits


def get_commit_index_max(task: Task) -> int:
    commit_index_max: int = 0
    for branch_value in task.values():
        commit_index_max = max(commit_index_max, max(branch_value['commits']))
    return commit_index_max


def extract_commits(args: Namespace, commit_index_max: int) -> None:
    for commit_index in range(commit_index_max + 1):
        extract_commit(args=args, commit_index=commit_index)


def get_solution_git(commits: Commits, dir_base: str) -> Solution:
    solution: Solution = [
        '#!/bin/bash',
        '',
        '#init',
        'cd ~/opi2',
        'rm -rf repo_git',
        'mkdir repo_git',
        'cd repo_git',
        'git init',
        ''
    ]
    user_current: str = ''
    branch_current: str = ''
    branches_visited: Set[str] = set()
    dir_previous: str = ''
    branch_to_last_dir: Dict[str, str] = {}
    for commit_index in range(len(commits.values())):
        solution.append(f'#r{commit_index}')
        commit_current: Commit = commits[commit_index]
        
        if user_current != commit_current.user:
            user_current = commit_current.user
            solution.append(f'git config --local user.name {user_current}')
            solution.append(f'git config --local user.email {user_current}@gmail.com')
        
        if branch_current != commit_current.branch:
            branch_current = commit_current.branch
            if branch_current not in branches_visited:
                branches_visited.add(branch_current)
                solution.append(f'git checkout -b {branch_current}')
            else:
                solution.append(f'git checkout {branch_current}')
        
        dir_current: str = f'{dir_base}/commits/commit{commit_index}'
        if commit_current.branch_to_merge is not None:
            solution.append(f'git merge {commit_current.branch_to_merge} --no-commit')
            merge_dir_cmp = dircmp(dir_previous, dir_current)
            merge_right_only: List[str] = merge_dir_cmp.right_only
            merge_diff_files: List[str] = merge_dir_cmp.diff_files
            if merge_right_only or merge_diff_files:
                solution.append('git checkout --ours .')
        
        branch_to_last_dir[branch_current] = dir_current
        allow_empty: str = ''
        
        if dir_previous != '':
            copy_dir_cmp = dircmp(dir_previous, dir_current)
            copy_right_only: List[str] = copy_dir_cmp.right_only
            copy_diff_files: List[str] = copy_dir_cmp.diff_files
            if not copy_right_only and not copy_diff_files:
                allow_empty = '--allow-empty '
        solution.append('ls | grep -v .git | xargs rm -rf')
        solution.append(f'cp -r ../commits/commit{commit_index}/* .')
        solution.append('git add .')
        solution.append(f'git commit {allow_empty}-m "r{commit_index}"')
        solution.append('')
        
        dir_previous = dir_current
    return solution


def get_solution_svn(commits: Commits, dir_base: str) -> Solution:
    solution: Solution = [
        '#!/bin/bash',
        '',
        '#init',
        'cd ~/opi2',
        'rm -rf repo_svn',
        'mkdir repo_svn',
        'cd repo_svn',
        '',
        '#init remote',
        'svnadmin create origin',
        'REMOTE_URL="file://$(pwd -P)/origin"',
        'COMMITS=~/opi2/commits',
        'svn mkdir -m "project structure" $REMOTE_URL/trunk $REMOTE_URL/branches --username "red"',
        '',
        '#init local',
        'svn checkout $REMOTE_URL/trunk working_copy',
        'cd working_copy',
        '',
    ]
    
    branch_current: str = ''
    branches_visited: Set[str] = set()
    dir_previous: str = ''
    branch_to_last_dir: Dict[str, str] = {}
    for commit_index in range(len(commits.values())):
        solution.append(f'#r{commit_index}')
        commit_current: Commit = commits[commit_index]
        
        if branch_current != commit_current.branch:
            branch_previous: str = branch_current
            branch_current = commit_current.branch
            if branch_current not in branches_visited and branch_current != 'br_0':
                branches_visited.add(branch_current)
                branch_from: str = 'trunk' if branch_previous == 'br_0' else f'branches/{branch_previous}'
                solution.append(f'svn copy $REMOTE_URL/{branch_from} $REMOTE_URL/branches/{branch_current} -m "Add {branch_current}" --username "{commit_current.user}"')
            
            if commit_index != 0:
                if commit_current.branch == 'br_0':
                    solution.append(f'svn switch $REMOTE_URL/trunk')
                else:
                    solution.append(f'svn switch $REMOTE_URL/branches/{commit_current.branch}')
        
        dir_current: str = f'{dir_base}/commits/commit{commit_index}'
        
        if commit_current.branch_to_merge is not None:
            solution.append(f'svn merge $REMOTE_URL/branches/{commit_current.branch_to_merge}')
            merge_dir_cmp = dircmp(dir_previous, dir_current)
            merge_right_only: List[str] = merge_dir_cmp.right_only
            merge_diff_files: List[str] = merge_dir_cmp.diff_files
            if merge_right_only or merge_diff_files:
                solution.append('svn resolve . -R --accept=working')
        
        branch_to_last_dir[branch_current] = dir_current
        empty_commit: bool = False
        if dir_previous != '':
            copy_dir_cmp = dircmp(dir_previous, dir_current)
            copy_right_only: List[str] = copy_dir_cmp.right_only
            copy_diff_files: List[str] = copy_dir_cmp.diff_files
            if not copy_right_only and not copy_diff_files:
                empty_commit = True
        if commit_index != 0:
            solution.append('svn rm --force *')
        solution.append(f'cp -r $COMMITS/commit{commit_index}/* .')
        
        if empty_commit:
            solution.append(f'echo "r{commit_index}" > temporary_file')
        solution.append('svn add --force *')
        
        solution.append(f'svn commit -m "commit{commit_index}" --username "{commit_current.user}"')
        solution.append('')
        
        dir_previous = dir_current
    
    return solution


def write_solution(args: Namespace, solution_name: str, solution: Solution):
    with open(f'res/{args.variant}/{solution_name}', 'w+') as file_solution_git:
        file_solution_git.writelines(line + '\n' for line in solution)


def main() -> None:
    args: Namespace = get_args()
    
    dir_base: str = f'res/{args.variant}'
    os.makedirs(dir_base, exist_ok=True)
    
    task: Task = get_task(args=args)
    commit_index_max: int = get_commit_index_max(task=task)
    extract_commits(args=args, commit_index_max=commit_index_max)
    
    commits: Commits = get_commits(task=task)
    
    # for commit_index_current in range(1, commit_index_max + 1):
    #     commit_index_previous: int = commit_index_current - 1
    #     dir_previous: str = f'{dir_base}/commits/commit{commit_index_previous}'
    #     dir_current: str = f'{dir_base}/commits/commit{commit_index_current}'
    #     diff_files: List[str] = dircmp(dir_previous, dir_current).diff_files
    #     ic(diff_files)
    
    solution_git: Solution = get_solution_git(commits=commits, dir_base=dir_base)
    write_solution(args=args, solution_name='solution_git.sh', solution=solution_git)
    
    solution_svn: Solution = get_solution_svn(commits=commits, dir_base=dir_base)
    write_solution(args=args, solution_name='solution_svn.sh', solution=solution_svn)


if __name__ == '__main__':
    main()
