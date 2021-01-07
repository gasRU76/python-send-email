# Python-send-email is a simple skript for send email over any smtp server.

For start, you can use simple example:

```bash
pip3 install -r requirements.txt
python3 send_email.py --help 
```

You have to use config.ini or use command line arguments for send parametrs:
```bash
Usage: send_email.py [OPTIONS]

Options:
  --host TEXT               smtp host  [required]
  --port INTEGER            smtp port
  --use_tls / --no-use_tls  using encryption
  --sender TEXT             email sender  [required]
  --password TEXT           email password
  --recipient TEXT          email recipients  [required]
  --subject TEXT            email subject
  --body TEXT               email body
  --attachment PATH         email attachments
  --help                    Show this message and exit.
```

You also can build docker image and send email through one. 

```bash
docker build -t python-send-email .
docker run -t python-send-email --help
```

Thank you, for your comments and supports. It is very important for me. :hugs:
