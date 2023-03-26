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

After instrumenting the service code as it was shown above we can open a local Web browser, load the local page on http://127.0.0.1:5000/ and the OpenTelemetry trace exporter will dump the resulting traces within your local command console, as it is shown below:

```bash
127.0.0.1 - - [09/Feb/2023 17:01:32] "GET / HTTP/1.1" 200 -
{
    "name": "products",
    "context": {
        "trace_id": "0x97463cd269b25ed39994d2d0b191851c",
        "span_id": "0xa1c3a89ade55fdaa",
        "trace_state": "[]"
    },
    "kind": "SpanKind.INTERNAL",
    "parent_id": "0xe161a905283e6bac",
    "start_time": "2023-02-09T16:01:32.010948Z",
    "end_time": "2023-02-09T16:01:32.011069Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {
        "operation.product.count.value": 99,
        "operation.name": "products"
    },
    "events": [],
    "links": [],
    "resource": {
        "attributes": {
            "telemetry.sdk.language": "python",
            "telemetry.sdk.name": "opentelemetry",
            "telemetry.sdk.version": "1.15.0",
            "service.name": "shoppingcart",
            "service.instance.id": "instance-12"
        },
        "schema_url": ""
    }
}
{
    "name": "home",
    "context": {
        "trace_id": "0x97463cd269b25ed39994d2d0b191851c",
        "span_id": "0xe161a905283e6bac",
        "trace_state": "[]"
    },
    "kind": "SpanKind.INTERNAL",
    "parent_id": null,
    "start_time": "2023-02-09T16:01:32.010845Z",
    "end_time": "2023-02-09T16:01:32.011138Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {
        "operation.value": 1,
        "operation.name": "home"
    },
    "events": [],
    "links": [],
    "resource": {
        "attributes": {
            "telemetry.sdk.language": "python",
            "telemetry.sdk.name": "opentelemetry",
            "telemetry.sdk.version": "1.15.0",
            "service.name": "shoppingcart",
            "service.instance.id": "instance-12"
        },
        "schema_url": ""
    }
}
```

With that we finished instrumenting our simple service and we will start to build a Docker container that allows us to run our OpenTelemetry monitored service in any containerized cloud environment.
