import json
import os
import zipfile
from dataclasses import dataclass
from typing import Dict
from typing import List
from typing import Optional
from typing import Set
from typing import Union

import requests


def get_task(variant: int) -> Dict[str, Dict[str, Union[int, str, List[int], Dict[str, Union[int, str]]]]]:
    cookies = {
        'JSESSIONID': 'MhewXg2IYCWvJ6ZsX8xYGuBlfHMzb02LFpQmDdBm.helios',
    }
    
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://se.ifmo.ru',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://se.ifmo.ru/courses/software-engineering-basics',
        'Accept-Language': 'ru',
    }
    
    params = {
        'p_p_id': 'selab2_WAR_seportlet',
        'p_p_lifecycle': '1',
        'p_p_state': 'normal',
        'p_p_mode': 'view',
        '_selab2_WAR_seportlet_javax.portlet.action': 'getBranches',
        'p_auth': 'pzEAP8Ei',
    }
    
    data = {
        'variant': variant
    }
    
    response = requests.post('https://se.ifmo.ru/courses/software-engineering-basics', headers=headers, params=params, cookies=cookies, data=data)
    
    json_raw: str = response.text
    for br_index in range(3):
        json_raw = json_raw.replace(f'br_{br_index} ', f'"br_{br_index}" ')
    return json.loads(json_raw)


def extract_commit(variant: int, commit: int) -> None:
    cookies = {
        'JSESSIONID': 'MhewXg2IYCWvJ6ZsX8xYGuBlfHMzb02LFpQmDdBm.helios',
    }
    
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://se.ifmo.ru',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://se.ifmo.ru/courses/software-engineering-basics',
        'Accept-Language': 'ru,en-US;q=0.9,en;q=0.8',
    }
    
    params = {
        'p_p_id': 'selab2_WAR_seportlet',
        'p_p_lifecycle': '2',
        'p_p_state': 'normal',
        'p_p_mode': 'view',
        'p_p_cacheability': 'cacheLevelPage',
    }
    
    data = {
        'variant': variant,
        'commit': commit
    }
    
    response = requests.post('https://se.ifmo.ru/courses/software-engineering-basics', headers=headers, params=params, cookies=cookies, data=data)
    
    dir_base = f'res/{variant}'
    dir_zips = f'{dir_base}/zips'
    dir_commits = f'{dir_base}/commits'
    name_commit = f'commit{commit}'
    filename_zip = f'{dir_zips}/{name_commit}.zip'
    dir_commit_extracted = f'{dir_commits}/{name_commit}/'
    
    os.makedirs(dir_base, exist_ok=True)
    os.makedirs(dir_zips, exist_ok=True)
    os.makedirs(dir_commits, exist_ok=True)
    
    with open(f'{filename_zip}', 'wb+') as zip_file:
        zip_file.write(response.content)
    
    with zipfile.ZipFile(f'{filename_zip}', 'r') as zip_reference:
        zip_reference.extractall(f'{dir_commit_extracted}')


@dataclass
class Commit:
    index: int
    branch: str
    user: str
    branch_to_merge: Optional[str] = None


def get_solution_git(commits: Dict[int, Commit]) -> List[str]:
    solution: List[str] = [
        '#!/bin/bash',
        '',
        '#init',
        'cd ~/opi2',
        'rm -rf gitRepo',
        'mkdir gitRepo',
        'cd gitRepo',
        'git init',
        ''
    ]
    user_current: str = ''
    branch_current: str = ''
    branches_visited: Set[str] = set()
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
        
        if commit_current.branch_to_merge is not None:
            solution.append(f'git merge {commit_current.branch_to_merge} --no-commit')
        
        solution.append('ls | grep -v .git | xargs rm -rf')
        solution.append(f'cp -r ../commits/commit{commit_index}/* .')
        
        if commit_current.branch_to_merge is not None:
            solution.append('git checkout --ours -- ./*')
        
        solution.append('git add .')
        solution.append(f'git commit --allow-empty -m "r{commit_index}"')
        solution.append('')
    return solution


def get_solution_svn(commits: Dict[int, Commit]) -> List[str]:
    solution: List[str] = [
        '#!/bin/bash',
        '',
        '#init',
        'cd ~/opi2',
        'rm -rf svnRepo',
        'mkdir svnRepo',
        'cd svnRepo',
        '',
        '#init remote',
        'svnadmin create origin',
        'REMOTE_URL="file://$(pwd -P)/origin"',
        'COMMITS=~/opi2/commits',
        'svn mkdir -m "project structure" $REMOTE_URL/trunk $REMOTE_URL/branches',
        '',
        '#init local',
        'svn checkout $REMOTE_URL/trunk working_copy',
        'cd working_copy',
        '',
    ]
    
    branch_current = ''
    branches_visited: Set[str] = set()
    for commit_index in range(len(commits.values())):
        solution.append(f'#r{commit_index}')
        commit_current: Commit = commits[commit_index]
        
        if branch_current != commit_current.branch:
            branch_current = commit_current.branch
            if branch_current not in branches_visited and branch_current != 'br_0':
                branches_visited.add(branch_current)
                solution.append(f'svn copy $REMOTE_URL/trunk $REMOTE_URL/branches/{branch_current} -m "Add {branch_current}" --username "{commit_current.user}"')
            
            branch_temp = 'trunk' if commit_current.branch == 'br_0' else commit_current.branch
            solution.append(f'svn switch $REMOTE_URL/{branch_temp}')
        
        if commit_current.branch_to_merge is not None:
            solution.append(f'svn merge $REMOTE_URL/branches/{commit_current.branch_to_merge}')
        
        solution.append('svn rm ./* --force')
        solution.append(f'cp -r $COMMITS/commit{commit_index}/* .')
        solution.append(f'echo "r{commit_index}" > temporary_file')
        
        if commit_current.branch_to_merge is not None:
            solution.append('svn resolve . -R --accept mine-full')
        solution.append('svn add ./* --force')
        solution.append(f'svn commit -m "commit{commit_index}" --username "{commit_current.user}"')
        solution.append('')
    
    return solution


def main() -> None:
    variant: int = 283500
    
    data: Dict[str, Dict[str, Union[int, str, List[int], Dict[str, Union[int, str]]]]] = get_task(variant=variant)
    
    for commit in range(15):
        extract_commit(variant=variant, commit=commit)
    
    commits: Dict[int, Commit] = {}
    
    for branch, values in data.items():
        user_int = values['user']
        user_str = 'red' if user_int == 0 else 'blue'
        for commit_index in values['commits']:
            commit_current = Commit(index=commit_index, branch=branch, user=user_str)
            commits[commit_index] = commit_current
    
    for branch_to_merge, values in data.items():
        merge_value: Dict[str, Union[int, str]] = values.get('merge', None)
        if merge_value is None:
            continue
        commit_to_merge: int = merge_value['commit']
        commits[commit_to_merge].branch_to_merge = branch_to_merge
    
    solution_git: List[str] = get_solution_git(commits)
    with open(f'res/{variant}/solution_git.sh', 'w+') as file_solution_git:
        file_solution_git.writelines(line + '\n' for line in solution_git)
    
    solution_svn: List[str] = get_solution_svn(commits)
    with open(f'res/{variant}/solution_svn.sh', 'w+') as file_solution_svn:
        file_solution_svn.writelines(line + '\n' for line in solution_svn)


if __name__ == '__main__':
    main()
