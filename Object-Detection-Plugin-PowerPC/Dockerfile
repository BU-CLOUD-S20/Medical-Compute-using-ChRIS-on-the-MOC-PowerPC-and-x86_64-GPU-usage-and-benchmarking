FROM docker.io/ibmcom/powerai:1.6.2-all-ubuntu18.04-py37
ENV LICENSE=yes
LABEL maintainer "haoyangw@bu.edu"
ENV APPROOT="/usr/src/objdect"
WORKDIR $APPROOT
USER root
#RUN export PATH=/usr/include/linux/:$PATH && \
#    export C_INCLUDE_PATH=/usr/include/linux/:$C_INCLUDE_PATH && \
#    export LIBRARY_PATH=/usr/include/linux/:$LIBRARY_PATH &&\
#    export CPATH=$CPATH:/usr/include/linux/


RUN apt update && apt install -y --no-install-recommends python3-dev python3-opencv build-essential libboost-all-dev python-numpy python-setuptools libboost-python-dev libboost-thread-dev nvidia-cuda-dev
RUN apt install -y --no-install-recommends ffmpeg
#build-essential python3-pip python3-setuptools zlib1g-dev libjpeg-dev libsm6 libxext6 libxrender-dev python3-tk

USER pwrai
ENV PATH=/opt/anaconda/envs/wmlce/bin:$PATH
RUN /bin/bash -c "pip install pycuda chrisapp"

USER root
COPY ["objectdetection", "${APPROOT}/objectdetection"]
COPY ["VOCdevkit", "${APPROOT}/VOCdevkit"]
COPY ["entrypoint.sh", "/usr/local/bin"]
RUN chmod 777 /usr/local/bin/entrypoint.sh
RUN chown -R pwrai $APPROOT

USER pwrai
WORKDIR $APPROOT/objectdetection
ENTRYPOINT ["entrypoint.sh"]
#SHELL ["/opt/anaconda/bin/conda", "run","-n", "wmlce", "/bin/bash", "-c"]
#RUN source activate wmlce && pip install pycuda
#ENTRYPOINT ["/opt/anaconda/bin/conda", "run","-n", "wmlce", "/bin/bash", "-c"]
#RUN $CONDA_INSTALL_DIR/bin/activate $CONDA_ENV

#RUN export PATH=/usr/include/linux/:$PATH && \
#    export C_INCLUDE_PATH=/usr/include/linux/:$C_INCLUDE_PATH && \
#    export LIBRARY_PATH=/usr/include/linux/:$LIBRARY_PATH &&\
#    export CPATH=$CPATH:/usr/include/linux/
#RUN pip3 install tensorflow-gpu==1.14
#make git pkg-config wget libssl-dev libevent-pthreads* libprotobuf-dev
#libboost-tools-dev libboost-thread1.62-dev magics++
#build & install CMake
