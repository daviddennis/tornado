Test API in Tornado - David Dennis
==================================

Language: python

Notes:
Since a uwsgi/nginx configuration was not allowed,
this uses Tornado for its non-blocking I/O, giving 
the API greater flexibility and speed while handling requests.

A db index on the `device_uuid` and `sensor_reading_time` fields speeds
up request lookups. This would likely be more performant to use a NoSQL database and cacheing layer (e.g., Redis) in practice.

Requirements:
 - postgres

To run:
1. activate a virtualenv
2. "pip install -r requirements.txt"
3. "psql -U cognical canary < setup.sql"
4. "python app.py"
5. Navigate to http://127.0.0.1:8888/device/preload/ (optional)
5. Make GET/POST requests to http://127.0.0.1:8888/device/