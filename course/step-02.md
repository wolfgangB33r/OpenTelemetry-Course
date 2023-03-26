# Instrument your Flask App with OpenTelemetry

In this step the Flask app is manually instrumented with OpenTelemetry.
The OpenTelemetry instrumentation depends on the API as well as on the SDK implementation, which can be 
imported by using the pip statements shown below:

```bash
pip install opentelemetry-api
pip install opentelemetry-sdk
```

Once the OpenTelemetry packages are successfully installed, the instrumentation of your service code can be done.
Import statements as well as the creation of the trace provider are added at the beginning and each function gets its own span report.

```python
from flask import Flask
import json

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
   BatchSpanProcessor,
   ConsoleSpanExporter,
)


from opentelemetry.sdk.resources import Resource


trace_provider = TracerProvider(resource=Resource.create({
           "service.name": "shoppingcart",
           "service.instance.id": "instance-12",
       }),)
processor = BatchSpanProcessor(ConsoleSpanExporter())
trace_provider.add_span_processor(processor)


# Sets the global default tracer provider
trace.set_tracer_provider(trace_provider)


# Creates a tracer from the global tracer provider
tracer = trace.get_tracer(__name__)


app = Flask(__name__)


@app.route('/')
def home():
   with tracer.start_as_current_span("home") as span:
       span.set_attribute("operation.value", 1)
       span.set_attribute("operation.name", "home")
       ret = {
           'path' : 'home'   
       }
       # now call an internal service method
       products()
       # then return
       return json.dumps(ret)


def products():
   # add this span as child into the current trace
   with tracer.start_as_current_span("products") as child:
       child.set_attribute("operation.product.count.value", 99)
       child.set_attribute("operation.name", "products")
       ret = {
           'path' : 'products'   
       }
       return json.dumps(ret)

```
