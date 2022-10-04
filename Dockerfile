FROM python:3.10.7-alpine
LABEL Maintainer="CarbonAnik"

WORKDIR /usr/src/app

COPY . /usr/src/app/
RUN pip install -r requerment.txt

CMD [ "python","-u","/usr/src/app/bot.py" ]
EXPOSE 5050