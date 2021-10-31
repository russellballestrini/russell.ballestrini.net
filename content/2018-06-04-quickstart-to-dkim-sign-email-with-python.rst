Quickstart to DKIM Sign Email with Python
################################################################

:author: Russell Ballestrini
:slug: quickstart-to-dkim-sign-email-with-python
:date: 2018-06-04 09:03
:tags: Code
:status: published

For a long time I have put off DKIM signing email sent from  my web services because I couldn't wrap my head around all the indirection Postfix requires to make it work.

Honestly, I put it off for over 5 years...

Today a thought sprung into my head: 

    "Could I sign Email at the application level before passing to Postfix?"

As you may know, I primarily use the Python programming language, so I did some research and found a reference to a single library called ``dkimpy`` (previously ``pydkim``). The codebase started over 10 years ago and appeared stable and mature.

The part that sold me was that ``dkimpy`` seemed compatible with the two Python standard library modules which I already use:

* ``email`` which I use to prepare messages
* ``smtplib`` which I use to transport messages to Postfix running on localhost

One issue I did have with ``dkimpy`` was the complete lack of examples or even a quickstart guide.

For this reason, I have written this post!


The Missing dkimpy Quickstart Guide
======================================

1. To install ``dkimpy`` you may use ``pip`` (``requirements.txt``) or in my case I added it to my ``setup.py``.

2. Generate a public / private keypair. Don't let this step trip you up, the process easy. In a Unix -like environment you may run the following commands to create the keys.

   generate private key (I name my file after the domain and DKIM selector I plan to use).

   .. code-block:: bash

    openssl genrsa -out remarkbox.com.20180605.pem 1024
   
   generate public key from the private key.

   .. code-block:: bash

    openssl rsa -in remarkbox.com.20180605.pem -out remarkbox.com.20180605.pub -pubout

3. Install the public key (``.pub``) as a DNS TXT record, where the record name ("selector") is ``20180605._domainkey`` and the value body is:

   .. code-block:: bash

    v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDcplYPRsqIFwXuggtH2XgQDMX+e+6sGnWdV8ld/FR9zgRAxB+DeiCEVooVvYt2JRZUEokgDFvys82Q+JTbN4qHNz19bdcBGrnTsnIFaQYpgeQYmPLdDtcWRKzTYMRNCnRmmEXyGv7WIDcaTapIq9NFgLmy1QT7ZTxuNjQtDB/2LwIDAQAB;

   You may choose any selector, I happen to like to use YearMonthDay. Additionally you will substitute your public key in place of mine. Put each the line of the public key on a single line in the TXT record.

4. On each of my application servers I store my private portion of my DKIM key in ``/etc/dkim/remarkbox.com.20180605.pem``. You may store your key any where on the filesystem that is accessible to the user or group running the application.

5. This is how I used to send Email with Python:

   .. code-block:: python

    import smtplib
    
    from email.mime.multipart import MIMEMultipart
    
    from email.mime.text import MIMEText
    
    # catch socket errors when postfix isn't running...
    from socket import error as socket_error
    
    
    def send_email(
        to_email,
        sender_email,
        subject,
        message_text,
        message_html,
        relay="localhost"
    ):
        msg = MIMEMultipart("alternative")
        msg.attach(MIMEText(message_text, "plain"))
        msg.attach(MIMEText(message_html, "html"))
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = to_email
        # TODO: react if connecting to postfix is a socket error.
        s = smtplib.SMTP(relay)
        s.sendmail(sender_email, [to_email], msg.as_string())
        s.quit()
        return msg


6. This is how I now send DKIM signed Email with Python:

   .. code-block:: python

    # ref: https://github.com/russellballestrini/miscutils/blob/master/miscutils/mail.py

    import dkim
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    # catch socket errors when postfix isn't running...
    from socket import error as socket_error


    def send_email(
        to_email,
        sender_email,
        subject,
        message_text,
        message_html,
        relay="localhost",
        dkim_private_key_path="",
        dkim_selector="",
    ):

        # the `email` library assumes it is working with string objects.
        # the `dkim` library assumes it is working with byte objects.
        # this function performs the acrobatics to make them both happy.

        if isinstance(message_text, bytes):
            # needed for Python 3.
            message_text = message_text.decode()
    
        if isinstance(message_html, bytes):
            # needed for Python 3.
            message_html = message_html.decode()

        sender_domain = sender_email.split("@")[-1]
        msg = MIMEMultipart("alternative")
        msg.attach(MIMEText(message_text, "plain"))
        msg.attach(MIMEText(message_html, "html"))
        msg["To"] = to_email
        msg["From"] = sender_email
        msg["Subject"] = subject

        try:
            # Python 3 libraries expect bytes.
            msg_data = msg.as_bytes()
        except:
            # Python 2 libraries expect strings.
            msg_data = msg.as_string()
 
        if dkim_private_key_path and dkim_selector:
            # the dkim library uses regex on byte strings so everything
            # needs to be encoded from strings to bytes.
            with open(dkim_private_key_path) as fh:
                dkim_private_key = fh.read()
            headers = [b"To", b"From", b"Subject"]
            sig = dkim.sign(
                message=msg_data,
                selector=str(dkim_selector).encode(),
                domain=sender_domain.encode(),
                privkey=dkim_private_key.encode(),
                include_headers=headers,
            )
            # add the dkim signature to the email message headers.
            # decode the signature back to string_type because later on
            # the call to msg.as_string() performs it's own bytes encoding...
            msg["DKIM-Signature"] = sig[len("DKIM-Signature: ") :].decode()

            try:
                # Python 3 libraries expect bytes.
                msg_data = msg.as_bytes()
            except:
                # Python 2 libraries expect strings.
                msg_data = msg.as_string()

        # TODO: react if connecting to relay (localhost postfix) is a socket error.
        s = smtplib.SMTP(relay)
        s.sendmail(sender_email, [to_email], msg_data)
        s.quit()
        return msg


**As always, leave a comment or contact me for questions or help.**
