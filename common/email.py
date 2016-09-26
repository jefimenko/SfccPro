import smtplib


def sendEmail(from_email_address, password, to_email_addresses, subject_line, message_body):
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()

    server.login(from_email_address, password)

    server.sendmail(
        from_email_address,
        to_email_addresses,
        'Subject: {}\n\n{}\n'.format(subject_line, message_body)
    )

    server.quit()
