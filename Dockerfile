FROM centos:centos7

RUN rpm --import https://mirror.go-repo.io/centos/RPM-GPG-KEY-GO-REPO && \
    curl -s https://mirror.go-repo.io/centos/go-repo.repo | tee /etc/yum.repos.d/go-repo.repo

RUN yum update -y && yum install -y rpmdevtools \
                                    httpd \
                                    wget \
                                    tree \
                                    git \
                                    createrepo \
                                    golang

COPY cuda-rhel7.repo /etc/yum.repos.d/

RUN yum install -y gcc gcc-c++ kernel-devel make

RUN mkdir /work
WORKDIR /work

#COPY local.repo /etc/yum.repos.d/

COPY . /work
