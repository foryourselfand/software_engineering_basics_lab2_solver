# software_engineering_basics_lab2_solver

## Installation

```shell
git clone https://github.com/foryourselfand/software_engineering_basics_lab2_solver.git
python3 -m venv venv_python3 # tested on python3.7, but should work on >= python3.6
source venv_python3/bin/activate
# venv_python3\Scripts\activate.bat # Windows
pip install -r requirements.txt
```

## Usage

```shell
python3 solver.py --help

#usage: solver.py [-h] -v VARIANT -j JSESSIONID -p P_AUTH [-e]
#
#optional arguments:
#  -h, --help            show this help message and exit
#
#required named arguments:
#  -v VARIANT, --variant VARIANT
#                        variant number
#  -j JSESSIONID, --jsessionid JSESSIONID
#                        JSESSIONID from cookies
#  -p P_AUTH, --p_auth P_AUTH
#                        p_auth from params
```

## Examples

```shell
python3 solver.py --variant 134538 --jsessionid YcuD-TUVDbhlPjafeoIjO1RA1xlsgXAtiz_JxgAh.helios --p_auth HkW6wAwA
python3 solver.py --p_auth Supxz0z7 --jsessionid oeEJpf_6urlKNLWMTXjXQJjQUPTiWTCGvQ72-kfA.helios --variant 331039
# don't change jsessionid and p_auth every time, only if needed (stopped working, so needs update)  
```

## Results

Directory `res/{variant}/` contains `solution_git.sh`, `solution_svn.sh` and directories `commits/` and `zips/`

## JSESSIONID? p_auth?

* go to https://se.ifmo.ru/courses/software-engineering-basics
* open network window in browser
* type variant and press enter
  ![git_img_1.png](res/git_img_1.png)
* choose first response, open headers window
* find and copy JSESSIONID from Cookie at Request Headers and p_auth from Query String Parameters
  ![git_img_2.png](res/git_img_2.png)
