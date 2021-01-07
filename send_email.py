import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import click
import click_config_file

@click.command()
@click.option('--host', help='smtp host', required=True)
@click.option('--port', help='smtp port', required=False, default=25)
@click.option('--use_tls/--no-use_tls', help='using encryption', default=False)
@click.option('--sender', help='email sender', required=True)
@click.option('--password', help='email password', default=None)
@click.option('recipients', '--recipient',  help='email recipients', multiple=True, required=True)
@click.option('--subject', help='email subject', required=False, default="")
@click.option('--body', help='email body', required=False, default="")
@click.option('attachments', '--attachment', help='email attachments', multiple=True, type=click.Path(), required=False)
@click_config_file.configuration_option(default="config.ini")
def send(host, port, sender, password, recipients, attachments, subject, body, use_tls):   
    # Create the enclosing (outer) message
    outer = MIMEMultipart()
    outer['Subject'] = subject
    outer['To'] = recipients[0]
    outer['From'] = sender
    body = MIMEText(body)
    outer.attach(body)

    # Add the attachments to the message
    for file in attachments:
        try:
            with open(file, 'rb') as fp:
                msg = MIMEBase('application', "octet-stream")
                msg.set_payload(fp.read())
            encoders.encode_base64(msg)
            msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
            outer.attach(msg)
        except:
            print("Unable to open one of the attachments. Error ")
            raise

    composed = outer.as_string()

    # Send the email
    try:
        with smtplib.SMTP(host, port) as s:
            s.ehlo()
            if use_tls:
                s.starttls()
            s.ehlo()
            if password != None:
                s.login(sender, password)
            s.sendmail(sender, recipients, composed)
            s.close()
        print("Email sent!")
    except:
        print("Unable to send the email. Error: ")
        raise

if __name__ == '__main__':
    send()
    
