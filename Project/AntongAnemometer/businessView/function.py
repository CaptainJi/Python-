from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from openpyxl import Workbook
from os import path
# 发送邮件模块
import smtplib
from email.mime.text import MIMEText  # 定义邮件内容
from email.header import Header  # 定义邮件标题
from email.mime.multipart import MIMEMultipart  # 定义邮件附件
from email.mime.image import MIMEImage  # 定义附件图片

import time
import logging.config
import os
import sys

# 读取日志配置文件
conlog_file = '../config/log.conf'
conlog = path.join(path.dirname(path.abspath(__file__)), conlog_file)
# conlog = '../config/log.conf'
logging.config.fileConfig(conlog)
logging = logging.getLogger()

now = time.strftime('%Y' + '年' + '%m' + '月' + '%d' + '日-' + '%H' + '点' + '%M' + '分')


# res_html = '../data/风表状态监测' + now + '.html'


def login():

    driver = webdriver.Chrome()
    driver.get('https://natapp.cn/login')
    driver.maximize_window()
    try:
        logging.info('开始登录')
        driver.find_element_by_id('login').send_keys('13684631497')
    except NoSuchElementException:
        driver.get_screenshot_as_file('../screenshots/登录异常' + now + '.png')
        logging.warning('登录异常；请查看登录截图“../screenshots/登录异常' + now + '.png”')
        page_source = driver.page_source
        res_html = '../data/登录异常' + now + '.html'
        with open(res_html, mode='w', encoding='utf-8') as file:
            file.write(page_source)
        driver.close()
        return res_html
    else:
        driver.find_element_by_id('password').send_keys('123456789')
        driver.implicitly_wait(1)
        driver.find_element_by_css_selector('#login_form > div:nth-child(6) > button').click()
        # driver.implicitly_wait(2)
        # driver.find_element_by_css_selector('body > a.sidebar_switch.ttip_r.off_switch').click()
        driver.implicitly_wait(1)
        driver.find_element_by_css_selector('#collapse_16 > div > ul > li:nth-child(2) > a').click()
        cookies = driver.get_cookies()

        driver.get_screenshot_as_file('../screenshots/状态截图' + now + '.png')

        page_source = driver.page_source
        res_html = '../data/风表状态监测' + now + '.html'
        with open(res_html, mode='w', encoding='utf-8') as file:
            file.write(page_source)
        return res_html


def parss_data(res_html):
    # 载入页面
    with open(res_html, mode='r', encoding='utf-8') as file:
        html = file.read()

    # 创建BeautifSoup实例，解析html数据
    bs = BeautifulSoup(html, 'lxml')  # 指定使用html解析器lxml
    table = bs.table  # 获取页面表格信息
    try:
        tr_arr = table.find_all('tr')  # 获取行信息
    except AttributeError:
        logging.warning('数据分析异常')
        try:
            sendMail(latestReport(), latestScreenshot())
        except:
            logging.warning('邮件发送异常')
            sys.exit(0)
        sys.exit(0)
    else:
        logging.info('开始分析风表状态')
        result = []  # 构造列表
        # 循环取得每行中指定列内容；.get_text(strip=True)为只取文字内容
        for tr in tr_arr[2:]:
            td_arr = tr.find_all('td')
            id = td_arr[0].get_text(strip=True)
            name = td_arr[1].get_text(strip=True)
            expire = td_arr[6].get_text(strip=True)
            flow = td_arr[7].get_text(strip=True)
            status = td_arr[8].get_text(strip=True)
            online = td_arr[9].get_text(strip=True)
            # 判断是否含有报警信息
            if online == '离线':
                logging.warning('%s离线' % name)
                warning = '../warning/%s离线报警' % name + now + '.html'
                with open(warning, mode='w', encoding='utf-8') as file:
                    file.write(html)
                sendMail(latestReport(), latestScreenshot())
            else:
                logging.info('%s状态正常' % name)
            # 构造字典
            row = {
                'ID': id,
                '名称': name,
                '到期时间': expire,
                '本月流量': flow,
                '状态': status,
                '在线': online,
                '检查时间': now
            }
            # 字典内容添加进列表
            result.append(row)
        return result


# 保存内容到excel
def save_to_excel(data):
    # 创建工作薄workbook
    book = Workbook()
    # 创建工作表
    sheet = book.create_sheet('风表监控', 0)
    # 向工作表中添加表头数据
    sheet.append(['ID', '名称', '到期时间', '本月流量', '状态', '在线', '检查时间'])
    # 添加表头内容
    for item in data:
        row = [item['ID'], item['名称'], item['到期时间'], item['本月流量'], item['状态'], item['在线'], item['检查时间']]
        sheet.append(row)

    # 输出保存
    book.save('../reports/风表监控' + now + '.xlsx')
    logging.info('数据已保存到/reports/风表状态监测' + now + '.xlsx')


# 获取最新警报文件
def latestReport():
    reportDir = '../warning/'
    # 获取文件列表
    lists = os.listdir(reportDir)
    # 文件排序
    lists.sort(key=lambda fn: os.path.getatime(reportDir + fn))
    latestFile = os.path.join(reportDir, lists[-1])
    # print(latestFile)
    return latestFile


# 获取最新截图
def latestScreenshot():
    screenshotDir = '../screenshots/'
    # 获取文件列表
    lists = os.listdir(screenshotDir)
    # 截图排序
    lists.sort(key=lambda fn: os.path.getatime(screenshotDir + fn))
    latestScreenshot = os.path.join(screenshotDir, lists[-1])
    # print(latestScreenshot)
    return latestScreenshot


# 发送邮件
def sendMail(latestReport, latestScreenshot):
    with open(latestReport, 'rb') as file:
        report = file.read()
    with open(latestScreenshot, 'rb') as file:
        screenshot = file.read()

    smtpserver = 'smtp.exmail.qq.com'  # 定义邮箱服务器地址
    user = 'server@antong.cn'  # 定义用户名
    password = 'sZQoGbHRWXCikARv'  # 定义客户端密码
    sender = 'server@antong.cn'  # 定义发送人
    receivers = ['server@antong.cn']  # 定义接收人多接收人用“,”分隔

    # 定义邮件标题及内容
    subject = '风表离线报警'
    content = '<html><h1 style="color:red">风表离线报警</h1><body><p><img src="cid:image1"></p></body></html>'
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
    att.add_header('Content-Disposition', 'attachment', filename='风表监测报警.html')
    # att['Content-Disposition'] = "attachment:filename='风表检查报告.html'"
    msgRoot.attach(att)

    # 有多个附件时可启用以下内容
    # att2 = MIMEImage(screenshot, 'html', 'utf-8')
    # att2['Content-Type'] = 'application/octet-stream'
    # # att2['Content-Disposition'] = "attachment:filename='风表监测截图.png'"
    # att2.add_header('Content-Disposition', 'attachment', filename='')
    # msgRoot.attach(att2)

    # 发送邮件动作
    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)

    logging.info('开始发送邮件')
    try:
        smtp.sendmail(sender, receivers, msgRoot.as_string())
    except Exception as msg:
        logging.warning(msg)
    else:
        smtp.quit()
        logging.info('邮件发送完成')


# 删除过期文件

from datetime import datetime, timedelta
import datetime


def delDir(dir, datatime01):
    # 获取文件夹下所有文件和文件夹
    files = os.listdir(dir)

    for file in files:
        # filepath = os.path.join(dir , file)#路径拼接
        filePath = dir + "/" + file
        # 判断是否是文件
        if os.path.isfile(filePath):
            # 最后一次修改的时间
            last1 = os.stat(filePath).st_mtime  # 获取文件的时间戳
            filetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(last1))  # 将时间戳格式化成时间格式的字符串
            # 删除七天前的文件
            if (datatime01 < filetime):  # datatime01是当前时间7天前的时间，filetime是文件修改的时间，如果文件时间小于(早于)datatime01时间，就删除
                os.remove(filePath)
                logging.info('过期文件已清理！！！')
        elif os.path.isdir(filePath):
            # 如果是文件夹，继续遍历删除
            delDir(filePath, datatime01)
            # 如果是空文件夹，删除空文件夹
            if not os.listdir(filePath):
                os.rmdir(filePath)
                logging.info('过期文件已清理！！！')


if __name__ == '__main__':
    # # login()
    # data = '../data'
    # screenshots = '../screenshots'
    # # 获取过期时间
    # starttime = datetime.datetime.now()
    # d1 = starttime + timedelta(days=-0)
    # # d1 = starttime - timedelta(days=7) #获取7天前的时间
    # date1 = str(d1)
    # index = date1.find('.')  # 第一次出现的位置
    # datatime01 = date1[:index]
    # delDir(data, datatime01)
    # delDir(screenshots, datatime01)
    save_to_excel(parss_data(login()))
