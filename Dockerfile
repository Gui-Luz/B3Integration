FROM ubuntu:18.04

RUN apt-get update -y ; apt-get upgrade -y
RUN apt-get install -y apache2 --no-install-recommends; apt-get install -y libapache2-mod-wsgi-py3 --no-install-recommends
RUN a2enmod wsgi
RUN a2enmod lbmethod_byrequests

RUN mkdir /var/www/B3Integration
COPY . /var/www/B3Integration

RUN cd /usr/local/bin ; ln -s /usr/bin/python3 python

# Need to get up to date pip
RUN apt-get install -y wget --no-install-recommends
RUN adduser --system --group --disabled-login bflaskappuser ; cd /home/bflaskappuser/
RUN apt-get update -y ; apt-get upgrade -y
RUN apt-get install -y python3-pip --no-install-recommends
RUN wget -O get-pip.py 'https://bootstrap.pypa.io/pip/3.6/get-pip.py' ; python get-pip.py --disable-pip-version-check --no-cache-dir
# pip should be now pip3
RUN pip --version ; rm -f get-pip.py

#temp looking for workaround
#https://github.com/pypa/pip/issues/6158
#RUN pip install --no-cache-dir -r /var/www/BasicFlaskApp/requirements.txt
RUN pip install -r /var/www/B3Integration/requirements.txt

RUN chown -R bflaskappuser:www-data /var/www/B3Integration

COPY B3Integration.conf /etc/apache2/sites-available/B3Integration.conf
RUN a2ensite B3Integration

RUN rm -rf /etc/apache2/sites-available/000-default.conf
RUN rm -rf /etc/apache2/sites-enabled/000-default.conf
RUN rm -rf /var/www/B3Integration/B3Integration.conf
RUN rm -rf /var/www/B3Integration/Dockerfile
RUN rm -rf /var/www/B3Integration/requirements.txt

RUN service apache2 start
#RUN source /etc/apache2/envvars
RUN sleep 10
RUN chown -R bflaskappuser:www-data /var/www/B3Integration
RUN service apache2 stop
RUN sleep 10
RUN service apache2 start
RUN sleep 4

EXPOSE 80

RUN apt-get clean

ENTRYPOINT ["/bin/bash", "/usr/sbin/apache2ctl", "-D", "FOREGROUND"]