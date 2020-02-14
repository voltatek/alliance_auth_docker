FROM python:3.6.6-jessie
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    libmysqlclient-dev \
    unzip \
    git \
    curl \
    libssl-dev \
    libbz2-dev \
    libffi-dev \
    supervisor
RUN python3 -m venv /home/allianceserver/venv/auth/
#RUN source /home/allianceserver/venv/auth/bin/activate
RUN pip install --upgrade pip
RUN pip install wheel gunicorn flower requests-oauthlib==0.8.0 django==2.2.1 django-celery-beat==1.1.0
RUN pip install allianceauth
RUN cd /home/allianceserver && allianceauth start myauth
COPY /conf/local.py /home/allianceserver/myauth/myauth/settings/local.py
RUN cd /home/allianceserver && allianceauth update myauth
RUN mkdir -p /var/www/myauth/static
RUN python /home/allianceserver/myauth/manage.py collectstatic
COPY /conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
WORKDIR /home/allianceserver/myauth
EXPOSE 8000
EXPOSE 5555
CMD ["/usr/bin/supervisord"]
