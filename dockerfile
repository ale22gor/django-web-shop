FROM python:3.4.6
ADD requirements.txt ./requirements.txt
ADD ./eShop/ ./eShop/
WORKDIR /eShop/
RUN pip install -r ../requirements.txt
RUN apt-get update
RUN apt-get install -y curl
EXPOSE 4369 5671 5672 25672 15671 15672
