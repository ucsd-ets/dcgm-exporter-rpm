#!/bin/bash

rpmdev-setuptree

cp dcgm-exporter.spec ~/rpmbuild/SPECS

cd ~/rpmbuild/SPECS
rpmbuild --undefine=_disable_source_fetch -ba dcgm-exporter.spec

cp /root/rpmbuild/RPMS/x86_64/dcgm-exporter-2.3.1-1.el7.x86_64.rpm /work