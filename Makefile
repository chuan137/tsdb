
server:
	gunicorn -c config/gunicorn.py tsdb.flaskr:app
