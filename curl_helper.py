import re
from sys import argv


def main() -> None:
    if len(argv) == 1:
        exit('provide arguments')
    curl = ' '.join(argv[1:])
    JSESSIONID: str = re.search(r"JSESSIONID=(.*?);", curl).group(0).lstrip("JSESSIONID").lstrip("=").rstrip(";")
    p_auth: str = re.search(r"p_auth=(.*?)'", curl).group(0).lstrip("p_auth").lstrip("=").rstrip("'")
    result: str = f'--jsessionid {JSESSIONID} --p_auth {p_auth}'
    print(result)


if __name__ == '__main__':
    main()
