# Python-send-email is a simple script to send an email through any smtp server.

At the first, you can use a simple example:

```bash
pip3 install -r requirements.txt
python3 send_email.py --help 
```

You can use config.ini or use command line arguments to send parametrs:
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

You can also build a docker image and send an email through one. 

```bash
docker build -t python-send-email .
docker run -t python-send-email --help
```

Thankы, for your comments and support. It is very important for me. :hugs:
