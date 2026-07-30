FROM python:3.10
WORKDIR /usr/app
COPY . .
RUN pip install -r requirements.txt
RUN echo "precedence ::ffff:0:0/96 100" >> /etc/gai.conf
CMD [ "python", "bot.py" ]
