#!/bin/bash
set -euxo pipefail

python3 -m pipenv run pip freeze > requirements.txt

image_name="python:pipenv"
docker build --rm --pull --file "Dockerfile" --label "python-pip-env" --tag "${image_name}" .

vol_name="python-pipenv-vol"
docker volume create "${vol_name}"

# Run the default CMD / RUN in Dockerfile
workdir="app"
docker run \
  --rm \
  --workdir /${workdir} \
  --mount type=volume,source="${vol_name}",destination=/${workdir}/logs \
  ${image_name}
