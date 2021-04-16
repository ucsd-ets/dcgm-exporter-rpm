FROM centos:centos8

RUN dnf update -y && dnf install -y rpmdevtools \
                                    httpd \
                                    wget \
                                    tree \
                                    git \
                                    createrepo \
                                    golang

COPY cuda-rhel7.repo /etc/yum.repos.d/

RUN dnf install -y gcc gcc-c++ kernel-devel make

RUN mkdir /work
WORKDIR /work

COPY local.repo /etc/yum.repos.d/

COPY . /work
