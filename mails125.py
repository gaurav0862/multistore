import smtplib, ssl

def mailing(reciever,subject,text):
        gmail_user = 'sdsgupta1998@gmail.com'
        gmail_pwd = 'lalli@123'
        TO = reciever

        SUBJECT = subject
        TEXT = text
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        BODY = '\r\n'.join(['To: %s' % TO,
                'From: %s' % gmail_user,
                'Subject: %s' % SUBJECT,
                '', TEXT])

        server.sendmail(gmail_user, [TO], BODY)
        return('success')



# mailing(mail,sub,txt)