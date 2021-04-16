#!/bin/bash

rpmdev-setuptree

cp dcgm-exporter.spec ~/rpmbuild/SPECS

cd ~/rpmbuild/SPECS
rpmbuild --undefine=_disable_source_fetch -ba dcgm-exporter.spec
