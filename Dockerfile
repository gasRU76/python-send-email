FROM alpine:3.6

RUN mkdir /app && \
  apk add --no-cache python3 && \
  pip3 install click click-config-file

COPY send_email.py /app/

WORKDIR /app/
ENTRYPOINT [ "/usr/bin/python3", "/app/send_email.py" ] 
