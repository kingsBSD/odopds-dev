FROM debian

MAINTAINER Giles Richard Greenway

ENV HOME /root

RUN sed -i s/httpredir/ftp.us/ /etc/apt/sources.list

RUN apt-get -q -y update

RUN DEBIAN_FRONTEND=noninteractive apt-get -q -y --fix-missing install \
    build-essential \
    curl \
    git \
    libpq-dev \
    lynx \
    mongodb \
    mongodb-server \
    nano \
    nginx \
    openssh-server \
    php5-fpm \
    php5-sqlite \
    postgresql \
    postgresql-contrib \
    python-dev \
    python-pip \
    python-virtualenv \
    screen \
    supervisor \
    unzip 

# Create virtualenvs    
RUN virtualenv pdsEnv    
RUN virtualenv registryEnv

# Grab Git repos.
RUN cd /pdsEnv && git clone https://github.com/HumanDynamics/openPDS.git
RUN cd /registryEnv && git clone https://github.com/HumanDynamics/openPDS-RegistryServer.git

# Patch and install Python requirements
RUN sed -i 's/pymongo/pymongo==2.7/g' /pdsEnv/openPDS/requirements.txt
RUN /pdsEnv/bin/pip install -r /pdsEnv/openPDS/requirements.txt

RUN sed -i 's/pymongo/pymongo==2.7/g' /registryEnv/openPDS-RegistryServer/conf/requirements.txt
RUN sed -i 's/django-allauth/django-allauth==0.8.3/g' /registryEnv/openPDS-RegistryServer/conf/requirements.txt
RUN /registryEnv/bin/pip install -r /registryEnv/openPDS-RegistryServer/conf/requirements.txt

# Sigh, nodejs    
RUN curl --location https://deb.nodesource.com/setup_0.12 | bash -
RUN DEBIAN_FRONTEND=noninteractive apt-get -q -y --fix-missing install --yes nodejs

# https://www.npmjs.com/package/mongo-express
RUN git clone https://github.com/andzdroid/mongo-express
RUN mv /mongo-express/config.default.js /mongo-express/config.js
RUN sed -r -i "s/(adminUsername:) ''/\1 'user'/" /mongo-express/config.js 
RUN sed -r -i "s/(adminPassword:) ''/\1 'pass'/" /mongo-express/config.js
RUN cd /mongo-express && npm install  

# Default MongoDb database.
RUN mkdir -p /data/db 

# Install pexpect in both virtualenvs for the start-up scripts.
RUN /pdsEnv/bin/pip install pexpect 
RUN /registryEnv/bin/pip install pexpect 
 
# RegistryServer database. 
RUN mkdir -p  /var/www/trustframework/registryEnv/OMS-RegistryServer
RUN touch /var/www/trustframework/registryEnv/OMS-RegistryServer/test.db

RUN  mkdir -p /var/run/sshd

# http://www.phpliteadmin.org/
RUN cd /var/www/html && curl --location https://bitbucket.org/phpliteadmin/public/downloads/phpLiteAdmin_v1-9-6.zip > phpLiteAdmin_v1-9-6.zip
RUN cd /var/www/html && unzip phpLiteAdmin_v1-9-6.zip
RUN rm /var/www/html/phpLiteAdmin_v1-9-6.zip

ADD scripts /
ADD conf / 

RUN cp default /etc/nginx/sites-enabled/
RUN cp nginx.conf /etc/nginx/
RUN cp phpliteadmin.config.php /var/www/html/

RUN cp index.html /var/www/html/

CMD /usr/bin/supervisord
