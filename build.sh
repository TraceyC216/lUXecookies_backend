#Install dependencies
pip3 install -r requirements.txt

#Run migrarions
python3 manage.py migrate
python3 manage.py collectstatic --no-input