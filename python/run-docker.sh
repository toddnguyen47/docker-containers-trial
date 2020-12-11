#!/bin/bash
set -euxo pipefail

python3 -m pipenv run pip freeze > requirements.txt

image_name="python:pipenv"
docker build --rm --pull --file "Dockerfile" --label "python-pip-env" --tag "${image_name}" .

# vol_name="python-pipenv-vol"
# docker volume create "${vol_name}"

# Run the default CMD / RUN
# --mount type=volume,source="${vol_name}",target=/app \
docker run \
  --rm \
  --workdir /app \
  ${image_name}
