import json
import os
import zipfile
from pprint import pprint

import requests


def get_task(variant: int):
    cookies = {
        'JSESSIONID': 'tAok66w_ZTZBh-_K7OQL715_fNKTwUIJmDNOeJSt.helios',
    }
    
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://se.ifmo.ru',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://se.ifmo.ru/courses/software-engineering-basics',
        'Accept-Language': 'ru,en-US;q=0.9,en;q=0.8',
    }
    
    params = (
        ('p_p_id', 'selab2_WAR_seportlet'),
        ('p_p_lifecycle', '1'),
        ('p_p_state', 'normal'),
        ('p_p_mode', 'view'),
        ('_selab2_WAR_seportlet_javax.portlet.action', 'getBranches'),
        ('p_auth', 'qCvHkE9p'),
    )
    
    data = {
        'variant': variant
    }
    
    response = requests.post('https://se.ifmo.ru/courses/software-engineering-basics', headers=headers, params=params, cookies=cookies, data=data)
    
    json_raw = response.text
    for br_index in range(3):
        json_raw = json_raw.replace(f'br_{br_index} ', f'"br_{br_index}" ')
    return json.loads(json_raw)


def get_commit(variant: int, commit: int):
    cookies = {
        'JSESSIONID': 'tAok66w_ZTZBh-_K7OQL715_fNKTwUIJmDNOeJSt.helios',
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
    
    params = (
        ('p_p_id', 'selab2_WAR_seportlet'),
        ('p_p_lifecycle', '2'),
        ('p_p_state', 'normal'),
        ('p_p_mode', 'view'),
        ('p_p_cacheability', 'cacheLevelPage'),
    )
    
    data = {
        'variant': variant,
        'commit': commit
    }
    
    response = requests.post('https://se.ifmo.ru/courses/software-engineering-basics', headers=headers, params=params, cookies=cookies, data=data)
    
    os.makedirs(f'res/{variant}', exist_ok=True)
    os.makedirs(f'res/{variant}/zips', exist_ok=True)
    os.makedirs(f'res/{variant}/commits', exist_ok=True)
    
    with open(f'res/{variant}/zips/commit{commit}.zip', 'wb+') as zip_file:
        zip_file.write(response.content)
    
    with zipfile.ZipFile(f'res/{variant}/zips/commit{commit}.zip', 'r') as zip_reference:
        zip_reference.extractall(f'res/{variant}/commits/commit{commit}/')


def main() -> None:
    variant = 21643
    
    data = get_task(variant=variant)
    pprint(data)
    
    commits = []
    for branch_key, branch_value in data.items():
        commits_current = branch_value['commits']
        commits += commits_current
    
    for commit in commits:
        get_commit(variant=variant, commit=commit)


if __name__ == '__main__':
    main()
