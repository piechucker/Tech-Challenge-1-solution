#### Tech-Challenge-1-solution Readme

## Introduction
This repository contains the solution for the Tech Challenge 1. The original Dockerfile was modified to improve the security, reduce the image size, and minimize the attack surface. In this readme, we will discuss the changes made to the original Dockerfile and the reasoning behind them.

## Changes Made
The following changes were made to the original Dockerfile:

## Switched the base image
Switched the base image to python:3.9-slim-buster for a smaller and more secure image.
The original Dockerfile used the python:latest image as the base image, which is a rather large image and contains many packages that are not necessary for this application. In the new Dockerfile, I used a smaller frolvlad/alpine-python3 image as the base image. The base image has been changed to a more lightweight and secure Alpine Linux image, which reduces the attack surface and decreases the size of the image.

## Multi-stage build
The Dockerfile was split into two stages. The first stage builds the regctl binary, which is used in the second stage. This approach is more secure because it reduces the size of the final image and eliminates any unnecessary packages or files that were used during the build process.

## Installed essential packages
 The apk package manager is used to install packages in the Alpine Linux image. In the new Dockerfile, I added some essential packages like curl, bash, libstdc++, git, sqlite, libffi-dev, openssl-dev, g++, git, and musl-dev using apk package manager to ensure the necessary dependencies are available. I also removed any unnecessary packages to minimize the attack surface of the image.

## Google Cloud SDK installation
 In the original Dockerfile, the Google Cloud SDK was installed using curl. In the new Dockerfile, I switched to using wget as it is more secure than curl. Additionally, I added verification of the integrity of the downloaded file using the sha256sum command. This ensures that the downloaded file has not been tampered with and reduces the risk of attacks such as man-in-the-middle attacks.

## Copy files and directories
In the original Dockerfile, all files in the project directory were copied to the image. In the new Dockerfile, I only copied the necessary files and directories required to build and run the application. This reduces the size of the image and minimizes the attack surface.

## Included vendor packages
In the original Dockerfile, the vendor directory was not included in the build process. In the new Dockerfile, I added the vendor directory to the build process to ensure that all vendor packages are included in the final image. This change ensures that all dependencies are available in the image and reduces the risk of dependency-related vulnerabilities.
