python3 -m venv env
source env/bin/activate
cd dvg/backend
pip install -r requirements.txt
#deactivate
python3 manage.py runserver
cd ../frontend
yarn serve