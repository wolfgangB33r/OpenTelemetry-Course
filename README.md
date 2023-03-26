# OpenTelemetry Course

Within this exercise course you will learn how to use OpenTelemetry to instrument and observe a
simplistic service written in Python.
The course is organized in step-by-step tasks to guide readers from building the Python service,
over instrumenting the service with OpenTelemetry until deploying and running it within Google Cloud.

## Course outline

1. [Implement a Python service with Flusk](./course/step-01.md)
2. [Instrument your app with OpenTelemetry](./course/step-02.md)
3. [Export traces into a local file](./course/step-03.md)
4. [Configure OpenTelemetry to export to Dynatrace](./course/step-04.md)
5. [Build a Docker container](./course/step-05.md)
6. [Upload the Docker image to Dockerhub](./course/step-06.md)
7. Pull the image in Google Cloud
8. Deploy and run the service in Google Cloud

## Pull the Docker image within Google Cloud

Pull image in Google Cloud:

- Open Google Cloud Shell in a browser
- docker pull wolfgangb33r/python-otel-demo-service
- docker images
- docker tag ff3? gcr.io/{project-id}/python-otel-demo-service // project id is the Google Cloud project id from URL
- docker push gcr.io/{project-id}/python-otel-demo-service
