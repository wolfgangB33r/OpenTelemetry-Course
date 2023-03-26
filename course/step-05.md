# Build a Docker container

The Flusk app now is fully implemented and all the necessary OpenTelemetry instrumentation code is present.
Within this step, the Flusk app is transformed into a Docker image that can easily be pulled and deployed in any of the popular cloud environment, such as GCP, EC2 or Azure.

To build a Docker image, two additional files are necessary, the Dockerfile and the requirements.txt file that contains all the applications Python dependencies.

See below the Dockerfile that is used to build a Docker image from our current Flusk app:

```bash
FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
```

Within the requirements.txt file all necessary Python dependencies are listed, as it is shown below:

```bash
flask
opentelemetry-api
opentelemetry-sdk
opentelemetry-exporter-otlp
```
