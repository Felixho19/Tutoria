virtualenv -p /usr/bin/python2 venv
source venv/bin/activate
pip install -r requirements.txt
# Console 1 (You need to install redis-server first)
redis-server
# Console 2
python manage.py runserver
# Console 3 (if we have enable celery task)
celery -A proj beat

# Use SQLite browser to view db.sqlite3 for user information.

# Check out normal user homepage in
http://127.0.0.1:8000/tutoria/index
# Check out admin user homepage in with endeavor:endeavor
http://127.0.0.1:8000/admin