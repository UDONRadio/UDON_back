# udon_back
requires: python3
Also requires a running redis server

run:
python3 -m venv env &&

source env/bin/activate &&

pip install -r requirements.txt &&

python manage.py makemigrations &&

python manage.py migrate &&

python manage.py runserver &&
