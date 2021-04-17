FROM python:3.7.7-buster
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    libmariadb-dev \
    unzip \
    git \
    curl \
    libssl-dev \
    libbz2-dev \
    libffi-dev
RUN python3 -m venv /home/allianceserver/venv/auth/
#RUN source /home/allianceserver/venv/auth/bin/activate
RUN pip install --upgrade pip
RUN pip install wheel gunicorn flower
RUN pip install allianceauth
RUN cd /home/allianceserver && allianceauth start myauth
COPY /conf/local.py /home/allianceserver/myauth/myauth/settings/local.py
RUN cd /home/allianceserver && allianceauth update myauth
RUN mkdir -p /var/www/myauth/static
RUN python /home/allianceserver/myauth/manage.py collectstatic
RUN pip install supervisor
RUN pip install -U git+https://github.com/shaib/supervisor-stdout.git@patch-1
COPY /conf/supervisord.conf /usr/local/etc/supervisord.conf
WORKDIR /home/allianceserver/myauth
EXPOSE 8000
EXPOSE 5555
CMD ["/usr/bin/supervisord"]
