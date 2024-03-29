from flask import Flask
import json
import os

# Those two environment variables must be present
if 'OTEL_EXPORTER_OTLP_TRACES_ENDPOINT' not in os.environ:
    print("Environment variable OTEL_EXPORTER_OTLP_TRACES_ENDPOINT is missing!")
    
if 'OTEL_EXPORTER_OTLP_TRACES_HEADERS' not in os.environ:
    print("Environment variable OTEL_EXPORTER_OTLP_TRACES_HEADERS is missing!")

from opentelemetry.exporter.otlp.proto.http.trace_exporter import (
    OTLPSpanExporter,
)

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter
)

from opentelemetry.sdk.resources import Resource

trace_provider = TracerProvider(resource=Resource.create({
            "service.name": "shoppingcart",
            "service.instance.id": "instance-12",
        }),)

# Sets the global default tracer provider
trace.set_tracer_provider(trace_provider)

# Creates a tracer from the global tracer provider
tracer = trace.get_tracer(__name__)

# Processor for console export
processor = BatchSpanProcessor(ConsoleSpanExporter())
trace_provider.add_span_processor(processor)

# Processor for OTLP span export to Dynatrace or any other receiver
span_exporter = OTLPSpanExporter()

span_processor = BatchSpanProcessor(span_exporter)
trace_provider.add_span_processor(span_processor)

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
