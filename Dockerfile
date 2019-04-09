FROM ubuntu:latest

COPY darknet.sh /
RUN apt-get update 
RUN apt-get upgrade -y
RUN apt-get dist-upgrade -y
RUN apt-get update
RUN apt-get install -y git nano curl build-essential wget python imagemagick
RUN apt-get install -y python-argparse
RUN apt-get install -y python-numpy

RUN apt-get install -y cmake git libgtk2.0-dev pkg-config libavcodec-dev \
libavformat-dev libswscale-dev python-dev python-numpy libtbb2 libtbb-dev \
libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev unzip
RUN apt-get install -y vim

RUN cd \
    && wget https://github.com/opencv/opencv/archive/3.2.0.zip \
    && unzip 3.2.0.zip \
    && cd opencv-3.2.0 \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make -j8 \
    && make install \
    && cd \
    && rm 3.2.0.zip
    
RUN cd \
    && wget https://github.com/opencv/opencv_contrib/archive/3.2.0.zip \
    && unzip 3.2.0.zip \
    && cd opencv-3.2.0/build \
    && cmake -DOPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.2.0/modules/ .. \
    && make -j8 \
    && make install \
    && cd ../.. \
    && rm 3.2.0.zip
    


RUN mkdir -p ~/opencv cd ~/opencv && \
    wget https://github.com/Itseez/opencv/archive/3.2.0.zip && \
    unzip 3.2.0.zip && \
    rm 3.2.0.zip && \
    cd opencv-3.2.0 && \
    mkdir build && \ 
    cd build && \
    cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_C_EXAMPLES=ON \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D BUILD_EXAMPLES=ON .. && \
    make -j4 && \
    make install && \ 
    ldconfig



RUN git clone https://github.com/pjreddie/darknet.git
RUN cd /darknet/python
RUN rm /darknet/python/darknet.py
RUN curl https://raw.githubusercontent.com/Farman001/aiq_darknet/master/darknet.py > /darknet/python/darknet.py




# ************ TILL HERE WE INSTALL OFFICIAL DARKNET REPO THEN DELETE PYTHON FILE AND REPLACE IT WITH THE NEW PYTHON CODE FROM MY GITHUB. 
# ************ docker build .   in /newdocker folder
# ************ docker run -dit "image_id" 
# ************ docker ps            >>>>>>to get container ID
# ************ docker exec -it "container_id" /bin/bash           >>>>>>>>>>>>> get into the container and do whateve u want!!!!!!!!!!!!!!!!!!!
