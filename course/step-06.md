# Upload the Docker image to Dockerhub

After building the Docker image, its time to upload the image to Dockerhub so that we can easily pull and deploy it from any popular cloud environment.
The precondition for this step is a valid Dockerhub account!
Within the Dockerhub account a new repository needs to be created and the newly created image can then be either manually tagged with the Dockerhub repository name and then pushed to Dockerhub, or an automation step is used for that process.
Within this course a convenient GitHub action was used to automatically build the Docker image and within another automated step to upload the image to the Dockerhub repository with every GitHub repository commit.

See below the GitHub action workflow that was defined to automatically build the Docker image and to upload it to Dockerhub:

```yaml
name: Docker Image CI

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:

  build:
 
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      - name: Set up QEMU
        uses: docker/setup-qemu-action@v1
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v1
      - name: Login to DockerHub
        uses: docker/login-action@v1 
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      - name: Build and push
        id: docker_build
        uses: docker/build-push-action@v2
        with:
          push: true
          tags: wolfgangb33r/python-otel-demo-service
      - name: Image digest
        run: echo ${{ steps.docker_build.outputs.digest }}

```
