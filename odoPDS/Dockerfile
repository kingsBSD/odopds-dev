FROM ubuntu

MAINTAINER Giles Richard Greenway

ENV HOME /root

RUN apt-get -q -y update

RUN DEBIAN_FRONTEND=noninteractive apt-get -q -y --fix-missing install \
    git \
    python-pip \
    python-virtualenv \
    python-dev \
    libpq-dev \
    postgresql \
    postgresql-contrib \
    mongodb \
    mongodb-server \
    supervisor 
    
RUN virtualenv pdsEnv

RUN cd /pdsEnv && git clone https://github.com/HumanDynamics/openPDS.git

RUN sed -i 's/pymongo/pymongo==2.7/g' /pdsEnv/openPDS/requirements.txt
RUN /pdsEnv/bin/pip install -r /pdsEnv/openPDS/requirements.txt
RUN /pdsEnv/bin/pip install pexpect

RUN mkdir -p /data/db

ADD conf /
ADD scripts /

CMD /usr/bin/supervisord


