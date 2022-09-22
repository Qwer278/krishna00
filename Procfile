# web: daphne talk.asgi:application --port $PORT --bind 0.0.0.0 
release: python manage.py migrate
# web: daphne -b 0.0.0.0 -p $PORT talk.asgi:application
web: daphne talk.asgi:application --port $port --bind 0.0.0.0 -v2
web: waitress-serve --port=$PORT talk.wsgi:application