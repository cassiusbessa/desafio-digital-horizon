sudo apt install libpq-dev
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r dev-requirements.txt
FLASK_APP=src/main/app.py flask run