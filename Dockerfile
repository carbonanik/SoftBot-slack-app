FROM python:3.10.7-alpine
LABEL Maintainer="CarbonAnik"

WORKDIR /usr/src/app

COPY requirements.txt requerments.txt

RUN pip install -r requirements.txt

COPY . .

CMD [ "python","-u","/usr/src/app/bot.py" ]
EXPOSE 5050