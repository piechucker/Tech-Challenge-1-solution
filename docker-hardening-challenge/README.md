# Docker hardening challenge

## Getting started

To make the docker to build, create `.env.sh` based on `.env.sh.sample`. Define your GCP project, bucket name and create a random SECRET_KEY for the Flask server.
```
cp .env.sh.sample .env.sh
```
Also you have to create `gcp-service-account.json` in the root folder of the project, so the Flask service will actually be able to access your GCP storage bucket. If you want to use a different service account file name, update `.env.sh` accordingly.

## How to run the container

Build the image
```
./docker/docker-build.sh
```
Then simply run it
```
./docker/docker-run.sh
```
The service is available on your host machine at http://localhost:5001

## The actual task
- Create a nice and secure dockerfile for us that will do the same thing as this one
- Please document the your process and the whys

## Submit
When you're done, simply send it back to us.

## :four_leaf_clover: Good luck :four_leaf_clover: