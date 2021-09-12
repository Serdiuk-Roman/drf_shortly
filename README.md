# wwf (Wake Wood Flask)

## Base

 - OS: Ubuntu 21.04 x86_64
 - Python 3.9.5(3.9.6 in pyenv)
 - Django 3.2.7
 - DRF 3.12.4
 - sqlite3, Bootstrap

 ## Description

Cервис для сокращения гиперссылок

## Install

Копируем проект

    git clone https://github.com/Serdiuk-Roman/drf_shortly.git

Перейти

    cd drf_shortly

Создать окружение

    python3 -m venv env

Активировать

    source env/bin/activate

Зависимости

    pip install -r requirements.txt

База даних
~~~python3
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
~~~

Перший запуск

    python manage.py runserver

Сылка на api
[http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)
