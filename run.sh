python3 -m venv env
source env/bin/activate
cd dvg/backend
python3 -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
#deactivate
python3 manage.py runserver
cd ../frontend
yarn serve