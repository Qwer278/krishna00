# web: daphne talk.asgi:application --port $PORT --bind 0.0.0.0 
web: daphne -b 0.0.0.0 -p $PORT talk.asgi:application
web: waitress-serve --port=$PORT talk.wsgi:application