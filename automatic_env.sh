
source venv/bin/activate
sudo pip3 install -r requirements.txt

export FLASK_APP=main.py
export FLASK_DEBUG=1
export FLASK_ENV=development

flask run