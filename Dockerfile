FROM centos:7

RUN yum -y update && yum clean all

RUN yum -y install yum-plugin-ovl

RUN yum -y install wget
RUN yum -y install tar
RUN yum -y install bzip2
RUN yum -y install libXext-devel
RUN yum -y install git
RUN yum -y install cmake
RUN yum -y install patch
RUN yum -y install autoconf
RUN yum -y install automake
RUN yum -y install libtool
RUN yum -y install glibc-static
RUN yum -y install file
RUN yum -y install make
RUN yum -y install nano
RUN yum -y install centos-release-scl
RUN yum -y install devtoolset-8-gcc devtoolset-8-gcc-c++
RUN scl enable devtoolset-8 bash

RUN yum clean all

RUN ln -s /_sps/trunk/ExecFramework/main_execmodule /usr/bin/main_execmodule
RUN ln -s /_sps/trunk/convert /usr/bin/convert

CMD ["/bin/bash"]
