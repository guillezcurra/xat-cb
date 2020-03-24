release: python manage.py migrate
web: daphne mysite.asgi:application --port $PORT --bind 0.0.0.0 -v2
web: docker run -p 6379:6379 -d redis:5
