# OpenTelemetry Course Example

Within this exercise course you will learn how to use OpenTelemetry to instrument and observe a
simplistic service written in Python.
The course is organized in step-by-step tasks to guide readers from building the Python service,
over instrumenting the service with OpenTelemetry until deploying and running it within Google Cloud.

## Course outline

1. [Implement a Python service with Flusk](./course/step-01.md)
2. [Instrument your app with OpenTelemetry](./course/step-02.md)
3. Export traces into a local file
4. Build a Docker container
5. Upload the Docker image to Dockerhub
6. Pull the image in Google Cloud
7. Deploy and run the service in Google Cloud
8. Configure the service to send OpenTelemetry to Dynatrace








## Pull the Docker image within Google Cloud

Pull image in Google Cloud:

- Open Google Cloud Shell in a browser
- docker pull wolfgangb33r/python-otel-demo-service
- docker images
- docker tag ff3? gcr.io/{project-id}/python-otel-demo-service // project id is the Google Cloud project id from URL
- docker push gcr.io/{project-id}/python-otel-demo-service

## OTLP HTTP exporter environment variables

- export OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=https://<YOUR>.live.dynatrace.com/api/v2/otlp
- export OTEL_EXPORTER_OTLP_TRACES_HEADERS="Authorization=Api-Token <YOUR_TOKEN>"