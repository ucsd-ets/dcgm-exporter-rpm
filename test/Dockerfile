FROM centos:centos7

RUN yum update -y && \
    rpm --import https://mirror.go-repo.io/centos/RPM-GPG-KEY-GO-REPO && \
    curl -s https://mirror.go-repo.io/centos/go-repo.repo |  tee /etc/yum.repos.d/go-repo.repo

RUN mkdir /work

COPY ./cuda-rhel7.repo /etc/yum.repos.d/

COPY ./dcgm-exporter-2.3.1-1.el7.x86_64.rpm /work

WORKDIR /work
