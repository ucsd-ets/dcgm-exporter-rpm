Name:           dcgm-exporter
Version:        2.3.1
Release:        1%{?dist}
Summary:        Install dcgm exporter
Source0:        https://github.com/NVIDIA/gpu-monitoring-tools/archive/refs/tags/%{version}.tar.gz
License:        Apache License Version 2.0
URL:            https://example.com/cuda
BuildRequires:  git, gcc, gcc-c++ kernel-devel, golang
Requires:       datacenter-gpu-manager
%description

This is a package

%build
tar -xvzf %{_sourcedir}/*.tar.gz
cd %{_builddir}/gpu-monitoring-tools-%{version}
make binary %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd %{_builddir}/gpu-monitoring-tools-%{version}
make install %{?_smp_mflags}


%changelog
* Thu Apr 15 2021 root
- 
