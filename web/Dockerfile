FROM ubuntu:latest
MAINTAINER Vyacheslav Tykhonov "vyacheslav.tykhonov@dans.knaw.nl"
RUN apt-get update -y
RUN apt-get install -y sshpass vim openssh-server python-pip python-dev build-essential libmysqlclient-dev
RUN pip install --upgrade pip \
	simplejson \
	MySQL-python
#RUN mount -rw -o remount /
#RUN echo 'newpassword' |passwd root
#RUN sshpass -p newpassword ssh root@127.0.0.1

COPY . /app
#COPY flask-bootstrap/ /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app/app.py"]
#CMD ["flask-bootstrap/webapp.py"]
