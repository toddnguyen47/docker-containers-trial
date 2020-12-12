#!/bin/bash

set -euxo pipefail

volume_name="python-pipenv-vol"
target_dir="app"

docker run --interactive --tty \
  --rm \
  --mount type=volume,src=${volume_name},target=/${target_dir} \
  busybox
