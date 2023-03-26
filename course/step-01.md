# Implement a Python service with Flusk

The first step within our course is to implement a simplistic service in Python that opens a port and serves a simple JSON through HTTP protocol.
The convenient [Flask web framework](https://flask.palletsprojects.com/en/2.2.x/) (pip install flask) helps to serve Python microservice endpoints, as it is shown below:

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



## Dependencies

- Flask (pip install flask)
- opentelemetry-api
- opentelemetry-sdk

pip install opentelemetry-api
pip install opentelemetry-sdk
pip install opentelemetry-exporter-otlp
pip install Flask