FROM python:3.13.0a5-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app
RUN mkdir /var/log/metadefender-menlo

EXPOSE 3000

ENTRYPOINT ["python3"]

CMD ["-m", "metadefender_menlo"]