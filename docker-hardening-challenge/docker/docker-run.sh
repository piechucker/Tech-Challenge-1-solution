#!/bin/bash
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

docker run -d --rm -p 5001:5001 --env-file=$SCRIPT_DIR/../.env.sh --name docker_harden_challenge dockerhardeningchallenge:latest

docker cp $SCRIPT_DIR/../gcp-service-account.json docker_harden_challenge:/gcp-service-account.json

docker attach docker_harden_challenge
