FROM python:3.10.7
LABEL Maintainer="CarbonAnik"

ENV DATABASE_URL="postgres://lytqkzvjssyskj:f91ef2a97b8d420871f6670fc77b847bc801e4e444d1152c94d214b5203f87f5@ec2-44-205-112-253.compute-1.amazonaws.com:5432/dd6pmkufmjbuvg"
ENV SLACK_BOT_TOKEN="xoxb-2773747756774-4018188491895-q6Ww4bylDL6D4ftBCUmAuFwg"
ENV SIGNING_SECRET="987ef3ec051aa447531da8b708b2111e"
ENV PORT=5050

WORKDIR /usr/src/app

COPY . /usr/src/app/
RUN pip install -r requerment.txt

CMD [ "python","-u","/usr/src/app/bot.py" ]
EXPOSE 5050

# docker run --name nginx1 --network=custom-bridge-1 -p 80:80 -d nginx
# docker run --name nodeapp1 --network=custom-bridge-1 -e APPID=9999 -d nodeapp