FROM python:3.10.7-slim
LABEL Maintainer="CarbonAnik"

WORKDIR /usr/src/app

COPY . /usr/src/app/
RUN pip install -r requerment.txt

CMD [ "python","-u","/usr/src/app/bot.py" ]
EXPOSE 5050

# docker run --name nginx1 --network=custom-bridge-1 -p 80:80 -d nginx
# docker run --name nodeapp1 --network=custom-bridge-1 -e APPID=9999 -d nodeapp