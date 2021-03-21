import json
from pprint import pprint

import requests


def get_task(variant: int):
    cookies = {
        'JSESSIONID': 'pN6_CGtbS1GB9OsVpV8UrT_D8rdm77S97X23vKgR.helios',
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
        ('p_auth', 'SRvBCWwB'),
    )
    
    data = {
        'variant': variant
    }
    
    response = requests.post('https://se.ifmo.ru/courses/software-engineering-basics', headers=headers, params=params, cookies=cookies, data=data)
    
    json_raw = response.text
    for br_index in range(3):
        json_raw = json_raw.replace(f'br_{br_index} ', f'"br_{br_index}" ')
    return json.loads(json_raw)


def main() -> None:
    data = get_task(273826)
    pprint(data)


if __name__ == '__main__':
    main()
