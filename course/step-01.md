# Implement a Python service with Flusk

The first step within our course is to implement a simplistic service in Python that opens a port and serves a simple JSON through HTTP protocol.
The convenient [Flask web framework](https://flask.palletsprojects.com/en/2.2.x/) helps to serve Python microservice endpoints.
Use following command to install Flask within your Python environment:

```bash
pip install flask
```

or

```bash
python -m pip install flask
```

The code snippet below shows the simplistic Python service that creates a Flask app by reading the name from the environment variable and serves the two endpoints '/' and '/products', as it is shown below:

```python
from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def home():
   ret = {
       'path' : 'home'   
   }
   # now call an internal service method
   products()
   # then return
   return json.dumps(ret)


@app.route('/products')
def products():
   ret = {
       'path' : 'products'   
   }
   return json.dumps(ret)
```

## Run your Python Flask app

To run the Flask app locally, you first need to export the application name as shown below and then run the app with the command flask run.

```bash
export FLASK_APP=app
flask run
```

On the console Flask informs about the local Web address serving its content.

```bash
iMac:python-otel-demo-service wolfgang$ flask run
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
