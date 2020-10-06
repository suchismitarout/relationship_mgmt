FROM alpine:3.8
MAINTAINER Suchismita Rout
RUN apk add --no-cache --update python3
RUN pip3 install --upgrade pip setuptools
RUN pip install -U pip
COPY app/requirement.txt /tmp/
RUN pip install -r /tmp/requirement.txt
COPY . /opt/
WORKDIR /opt/app
ENV PYTHONPATH=$PYTHONPATH:/opt/
EXPOSE 5000
##CMD ["sleep","1000"]
CMD ["python3", "main_server.py"]
