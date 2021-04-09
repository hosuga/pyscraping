# README
## version
```
$ python -V
Python 3.9.0
```

## install
```
# seleniumモジュール
$ pip install selenium
# envモジュール
$ pip install python-dotenv
```

## .env
```
$ pwd
{Your Project Path}/PythonScraping
$ echo "CHROMEDRIVER_PATH = \"{Your chromedriver Path}/chromedriver\"" > .env
```

## execute
```
$ pwd
{Your Project Path}/PythonScraping
$ python scraping_executor.py
CardName:  xxxxx
=== Start login ===
Your Login Info: {"login_id": "yourID", "login_password": "yourPassword"}

=== Start authenticate ===
Your Answer: {"answer": "yourAnswer"}

=== Start get_info ===

===COMPLETED====
```