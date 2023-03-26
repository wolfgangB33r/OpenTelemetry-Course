# Export traces into a local file

After instrumenting the Flask app code you can open a local Web browser, load the local app endpoint http://127.0.0.1:5000/ and the OpenTelemetry trace exporter will dump the resulting traces within your local command console, as it is shown below:

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

With that the instrumenting of the Flask app is finished.
The next step will show how to flexibly configure the OpenTelemetry exporter to send observed spans to any telemetry backend by using environment variables.
