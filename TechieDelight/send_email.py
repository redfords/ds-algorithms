import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_selenium_report():
    dir_path = "G:/test_runners/selenium_regression_test_5_1_1/TestReport"
    files = ["SeleniumTestReport_part1.html", "SeleniumTestReport_part2.html", "SeleniumTestReport_part3.html"]

    msg = MIMEMultipart()
    msg['To'] = "4_server_dev@company.com"
    msg['From'] = "system@company.com"
    msg['Subject'] = "Selenium ClearCore_Regression_Test_Report_Result"

    body = MIMEText('Test results attached.', 'html', 'utf-8')  
    msg.attach(body)  # add message body (text or html)

    for f in files:  # add files to the message
        file_path = os.path.join(dir_path, f)
        attachment = MIMEApplication(open(file_path, "rb").read(), _subtype="txt")
        attachment.add_header('Content-Disposition','attachment', filename=f)
        msg.attach(attachment)

    s = smtplib.SMTP()
    s.connect(host=SMTP_SERVER)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    print 'done!'
    s.close()