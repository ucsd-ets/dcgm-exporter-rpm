Name:           dcgm-exporter
Version:        2.3.1
Release:        1%{?dist}
Summary:        Install dcgm exporter
Source0:        https://github.com/NVIDIA/gpu-monitoring-tools/archive/refs/tags/%{version}.tar.gz
License:        Apache License Version 2.0
URL:            https://example.com/cuda
Requires:       datacenter-gpu-manager, git, gcc, gcc-c++ kernel-devel, golang, make
%description

This is a package

%build
cat > start-dcgm.sh <<EOF
#!/usr/bin/bash
systemctl --now enable nvidia-dcgm
dcgm-exporter
EOF

%install

rm -rf $RPM_BUILD_ROOT

mkdir -p %{buildroot}/usr/bin/
install -m 755 start-dcgm.sh %{buildroot}/usr/bin/start-dcgm.sh

tar -xvzf %{_sourcedir}/*.tar.gz
cd %{_builddir}/gpu-monitoring-tools-%{version}
tar -xvzf %{_sourcedir}/*.tar.gz
cd %{_builddir}/gpu-monitoring-tools-%{version}

mkdir -p %{buildroot}/usr/share/gpu-monitoring-tools
cp -r %{_builddir}/gpu-monitoring-tools-%{version} %{buildroot}/usr/share/gpu-monitoring-tools

%post
cd /usr/share/gpu-monitoring-tools/gpu-monitoring-tools-%{version}
make binary
make install

%files
/usr/bin/start-dcgm.sh
/usr/share/gpu-monitoring-tools

%changelog
* Thu Apr 15 2021 root
- Start