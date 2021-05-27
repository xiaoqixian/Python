# !/usr/bin/python3
# -*- coding: utf-8 -*-
# > Author      : lunar
# > Email       : lunar_ubuntu@qq.com
# > Created Time: 2021年01月03日 星期日 14时46分55秒
# > Location    : Shanghai
# > Copyright @ https://github.com/xiaoqixian

# Send email in the command line.
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.header import Header
from xml.dom.minidom import parse
import xml.dom.minidom
import argparse
import os

sender_pwd = "this is your password"

def mail(args):
    res = True
    message = MIMEMultipart()
    from_name = args.fr
    to = args.to
    if not from_name:
        from_name = args.sender
    if not to:
        to = args.address
    message['From'] = Header(from_name, 'utf-8')
    message['TO'] = Header(to, 'utf-8')
    subject = args.subject
    if not subject:
        subject = "%s send file(s)" % from_name
    if os.path.exists(subject):
        f = open(args.subject)
        subject = f.read()
        f.close()
    message['Subject'] = Header(subject, 'utf-8')
    if args.attachment:
        files = args.attachment
        for f in files:
            file_name = f.split("/")[-1]
            #print(file_name)
            attach = MIMEApplication(open(f, 'rb').read())
            attach['Content-type'] = 'application/octet-stream'
            #attach['Content-Disposition'] = 'attachment;filename="' + file_name + '"'
            attach.add_header("Content-Disposition", "attachment", filename=(Header(file_name, "utf-8").encode()))
            message.attach(attach)
    server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    server.login(args.sender, sender_pwd)
    server.sendmail(args.sender, args.address, message.as_string())
    server.quit()
    return res

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Arugment parser for email sender")
    parser.add_argument("--fr", "-f", help = "sender name, default: sender email address", default = None)
    parser.add_argument("--to", '-t', help = "receiver name, default: receiver email address", default = None)
    parser.add_argument("--address", "-d", help = "receivers email addresses the email sent to. Multiple addresses separate with comma.", default = "lunar_ubuntu@qq.com")
    parser.add_argument("--sender", "-s", help = "sender email address", default = "lunar_debian@qq.com")
    parser.add_argument("--attachment", "-a", help = "attachment file(s), multiple files separate with comma", default = None, nargs = "*")
    parser.add_argument("--subject", "-j", help = "subject", default = None)
    args = parser.parse_args()

    hint = "Email\ Sent\ Successfully" if mail(args) else "Sending\ Email\ Failed"
    cmd = "notify-send %s -a SendEmail -i /home/lunar/.local/share/icons/BigSur-Originals-Colors-blue/apps/scalable/internet-mail.svg" % hint
    os.system(cmd)


