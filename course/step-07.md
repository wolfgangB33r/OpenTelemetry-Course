# Pull the image in Google Cloud

The Flusk app was successfully published to Dockerhub and is available as Docker image that can be deployed within any of the popular cloud environments.
Now let's pull the Docker image within a Google GCP project and deploy a running service within the Google Cloud Run environment.

To pull a Docker image from Dockerhub, open the Google Cloud Shell within your Google Cloud console.

Within the Google Cloud Shell, type the following commands to pull the Flusk app from Dockerhub:

```bash
docker pull wolfgangb33r/python-otel-demo-service
```

Now check if the image you just pulled is available, by typing following command:

```bash
docker images
```

If everything succeeded you will see the following output:

```bash
REPOSITORY                              TAG       IMAGE ID       CREATED         SIZE
wolfgangb33r/python-otel-demo-service   latest    a069b1ffca63   6 minutes ago   154MB
```

Now tag the newly pulled Docker image with the project id of the Google cloud projects you want to run the Flusk app in. Of course this project id is specific for your own Google project and you find it in the projects overview page within your Google Cloud console or within the URL of your Google project.
You need to select the IMAGE ID of your pulled image, as you find it in the output above (a069b1ffca63) which of course is specific and you need to replace the id with the id of your own Docker image.

```bash
docker tag a069b1ffca63 gcr.io/<YOUR_GOOGLE_PROJECT_ID>/python-otel-demo-service 
```

Now that the Docker image is correctly tagged with the Google project id you want to use it in, type the command below to finally push it into your Google project's local Docker registry:

```bash
docker push gcr.io/<YOUR_GOOGLE_PROJECT_ID>/python-otel-demo-service
```
