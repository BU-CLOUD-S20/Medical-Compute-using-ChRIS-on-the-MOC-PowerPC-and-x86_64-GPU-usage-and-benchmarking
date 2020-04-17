# Docker file for matmultiply ChRIS plugin app
#
# Build with
#
#   docker build -t <name> .
#
# For example if building a local version, you could do:
#
#   docker build -t local/pl-MatMultiply .
#
# In the case of a proxy (located at 192.168.13.14:3128), do:
#
#    docker build --build-arg http_proxy=http://192.168.13.14:3128 --build-arg UID=$UID -t local/pl-MatMultiply .
#
# To run an interactive shell inside this container, do:
#
#   docker run -ti --entrypoint /bin/bash local/pl-MatMultiply
#
# To pass an env var HOST_IP to container, do:
#
#   docker run -ti -e HOST_IP=$(ip route | grep -v docker | awk '{if(NF==11) print $9}') --entrypoint /bin/bash local/pl-MatMultiply
#
# Haoyang Wang haoyangw@bu.edu
FROM nvidia/cuda-ppc64le:10.1-devel
LABEL maintainer "haoyangw@bu.edu"
ENV APPROOT="/usr/src/matmultiply"
COPY ["matmultiply", "${APPROOT}"]
COPY ["requirements.txt", "${APPROOT}"]
COPY ["dependencies.txt","${APPROOT}"]
WORKDIR $APPROOT


RUN apt update
RUN apt install -y build-essential python3 llvm-7
RUN ln -s /usr/bin/llvm-config-7 /usr/bin/llvm-config
RUN apt install -y python3-pip
RUN pip3 install -r dependencies.txt
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["matmultiply.py", "--help"]

