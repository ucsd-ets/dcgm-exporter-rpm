# DCGM Exporter SPEC

Development environment & SPEC file for creating an RPM for installing the DCGM Exporter (https://github.com/NVIDIA/gpu-monitoring-tools).

## Setting up Docker environment

```bash
git clone https://github.com/ucsd-ets/dcgm-exporter-rpm.git
cd dcgm-exporter-rpm

docker build -t dcgm-builder-environment .

# start the docker environment
docker run -v $(pwd):/work -p 80:80 -ti dcgm-builder-environment /bin/bash

# within the docker environment, build the rpm using
./package-dcgm.sh
```
