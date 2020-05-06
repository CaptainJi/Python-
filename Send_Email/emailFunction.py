import logging
import os
import time
# 发送邮件模块
import smtplib
from email.mime.text import MIMEText  # 定义邮件内容
from email.header import Header  # 定义邮件标题
from email.mime.multipart import MIMEMultipart  # 定义邮件附件
from email.mime.image import MIMEImage  # 定义附件图片


# 获取当前时间
def getTime():
    # windows文件名禁止使用“:”所以时间格式要避免类似“14:30:25”
    now_time = time.strftime('%Y' + '年' + '%m' + '月' + '%d' + '日' '%H' + '点' + '%M' + '分' + '%S' + '秒')
    return now_time


# 获取最新报告
def latestReport():
    reportDir = '../reports/'
    # 获取文件列表
    lists = os.listdir(reportDir)
    # 文件排序
    lists.sort(key=lambda fn: os.path.getatime(reportDir + fn))
    latestFile = os.path.join(reportDir, lists[-1])
    print(latestFile)
    return latestFile


# 获取最新截图
def latestScreenshot():
    screenshotDir = '../screenshots/'
    # 获取文件列表
    lists = os.listdir(screenshotDir)
    # 截图排序
    lists.sort(key=lambda fn: os.path.getatime(screenshotDir + fn))

    latestScreenshot = os.path.join(screenshotDir, lists[-1])
    print(latestScreenshot)
    return latestScreenshot


# 发送邮件
def sendMail(latestReport, latestScreenshot):
    with open(latestReport, 'rb') as file:
        report = file.read()
    with open(latestScreenshot, 'rb') as file:
        screenshot = file.read()

    smtpserver = 'smtp.exmail.qq.com'  # 定义邮箱服务器地址
    user = 'jiqing@antong.cn'  # 定义用户名
    password = 'omRSPv3EiCSii5kH'  # 定义客户端密码
    sender = 'jiqing@antong.cn'  # 定义发送人
    receivers = ['jiqing@antong.cn']  # 定义接收人多接收人用“,”分隔

    # 定义邮件标题及内容
    subject = '风表监测报告'
    content = '<html><h1 style="color:red">风表监测报告</h1><body><p><img src="cid:image1"></p></body></html>' + report
    msgImage = MIMEImage(screenshot)  # 定义图片
    msgRoot = MIMEMultipart('alternative')
    msgRoot.attach(MIMEText(content, 'html', 'utf-8'))
    msgImage.add_header("Content-ID", "<image1>")  # 定义图片id 在html文本中引用
    msgRoot.attach(msgImage)
    msgRoot['Subject'] = Header(subject, 'utf-8')
    msgRoot['From'] = user
    msgRoot['To'] = ','.join(receivers)

    # 构造附件
    att = MIMEText(report, 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att.add_header('Content-Disposition', 'attachment', filename='风表检查报告.html')
    # att['Content-Disposition'] = "attachment:filename='风表检查报告.html'"
    msgRoot.attach(att)

    # 有多个附件时可启用以下内容
    # att2 = MIMEImage(screenshot, 'html', 'utf-8')
    # att2['Content-Type'] = 'application/octet-stream'
    # # att2['Content-Disposition'] = "attachment:filename='风表监测截图.png'"
    # att2.add_header('Content-Disposition', 'attachment', filename='风表监测截图.png')
    # msgRoot.attach(att2)

    # 发送邮件动作
    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)

    print('开始发送邮件')
    smtp.sendmail(sender, receivers, msgRoot.as_string())
    smtp.quit()
    print('邮件发送完成')


# 获取截图
def getScreenShot(driver, module):
    # 获取当前时间
    now_time = getTime()
    # 获取截图相对路径
    image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s %s.png' % (module, now_time)
    logging.info('获取“%s”屏幕截图' % module)
    print('截图:' + '%s %s.png' % (module, now_time))
    driver.get_screenshot_as_file(image_file)


if __name__ == '__main__':
    # driver = webdriver.Chrome()
    # driver.get('https://natapp.cn/tunnel/lists')
    # getScreenShot(driver, '截图')
    latestFile = latestReport()
    latestScreenshoot = latestScreenshot()
    sendMail(latestFile, latestScreenshoot)