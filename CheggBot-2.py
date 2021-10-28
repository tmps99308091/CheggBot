#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import pdfkit
import os


def send_test_mail(body,email,url):
    
    pdfkit.from_url(url, 'out.pdf')
    
    sender_email = "knifegod001@gmail.com"
    receiver_email = email
    #receiver_email = "chocolate80114@gmail.com"
    #receiver_email = "b08502152@ntu.edu.tw"

    msg = MIMEMultipart()
    msg['Subject'] = '[Tom的蝦皮賣場]Chegg代查'
    msg['From'] = 'Tom的蝦皮賣場'
    msg['To'] = receiver_email

    #msgText = MIMEText('<b>%s</b>' % (body), 'html')
    #msg.attach(msgText)

    #filename = "text.txt"
    #msg.attach(MIMEText(open(filename).read()))

    #with open('Unknown.jpg', 'rb') as fp:
        #img = MIMEImage(fp.read())
        #img.add_header('Content-Disposition', 'attachment', filename="Unknown.jpg")
        #msg.attach(img)
        
    pdf = MIMEApplication(open("out.pdf", 'rb').read())
    pdf.add_header('Content-Disposition', 'attachment', filename= "example.pdf")
    msg.attach(pdf)

    try:
        
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login('knifegod001@gmail.com', 'sam900628')
        smtp_server.sendmail(sender_email, receiver_email, msg.as_string())
        smtp_server.close()
        
    except Exception as e:
        print(e)
        
    os.remove('out.pdf')

#send_test_mail("同學們好，這是這次期中考的補充資料，請大家在考前熟讀，謝謝")


#@app.route('/')
#def hello_world():
    #return "Hello world!"

#if __name__ == "__main__":
    #send_test_mail("Welcome to Medium!")
    #app.run('0.0.0.0',port=5000)  """     


# In[ ]:


from flask import Flask,render_template,request
 
app = Flask(__name__, template_folder='templates')
 
@app.route('/')
def form():
    return render_template('form.html')
 
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        send_test_mail("Chegg代查",form_data['Email'],form_data['Url'])
        print(form_data['Email'])
        print(form_data['Url'])
        return render_template('data.html',form_data = form_data)
        
 
 
app.run(host='0.0.0.0', port=5000)


# In[7]: