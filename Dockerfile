FROM ubuntu:17.10

LABEL maintainer littleairmada@users.noreply.github.com

RUN apt-get -y update

RUN apt-get -y install \
        libevent-dev \
        python3.6-dev \
        python3.6 \
        python3-pip && \
    python3.6 -m pip install \
        locustio \
        websocket-client \
        socketIO-client

COPY ./run.py /run.py

EXPOSE 8089
EXPOSE 5557
EXPOSE 5558

ENTRYPOINT ["python3.6", "-u", "/run.py"]
