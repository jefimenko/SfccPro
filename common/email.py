import smtplib


def sendEmail(from_email_address, password, to_email_addresses, subject_line, message_body):
    # Alternate port: 587
    server = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
    server.ehlo()

    server.login(from_email_address, password)

    server.sendmail(
        from_email_address,
        to_email_addresses,
        'Subject: {}\n\n{}\n'.format(subject_line, message_body)
    )

    server.quit()

# Use twillio
# TODO: get email seattlefcc.pro@gmail.com
# TODO: get twillio to seattlefcc.pro@gmail.com
def sendText(message_body):

    pass
