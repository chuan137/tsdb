
.PHONY: server
server:
	gunicorn -c server/gunicorn.py server.flaskr:app
