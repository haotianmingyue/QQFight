# 开发者 haotian
# 开发时间: 2021/6/30 21:12
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

URL = 'http://ui.ptlogin2.qq.com/cgi-bin/login?appid=614038002&style=9&s_url=http%3A%2F%2Fdld.qzapp.z.qq.com%2Fqpet%2Fcgi-bin%2Fphonepk%3Fcmd%3Dindex%26channel%3D0'
username = '3463956232'
pwd = '123456789lht@'

driver = webdriver.Chrome()
driver.implicitly_wait(5)
#登录
def login(url,username,pwd):
    driver.get(url)
    driver.find_element_by_id('u').clear()
    driver.find_element_by_id('u').send_keys(username)
    driver.find_element_by_id('p').clear()
    driver.find_element_by_id('p').send_keys(pwd)
    driver.find_element_by_id('go').click()
    sleep(2)

# 领取徒弟经验
def ling_qu_tu_di():
    try:
        driver.find_element_by_link_text('领取徒弟经验').click()
        sleep(1)
    except NoSuchElementException:
        print("未领取徒弟经验")
# 每日奖励
def mei_ri_jing_yan():
    try:
        driver.find_element_by_link_text('每日奖励').click()
    except NoSuchElementException:
        print('没有找到每日奖励')
    sleep(1)
    try:
        for i in range(0, 2):
            driver.find_element_by_xpath('//*[@id="id"]/p[1]/a[2]').click()
            sleep(1)
    except NoSuchElementException:
        print('没有找到每日奖励领取按钮')
    driver.find_element_by_link_text('返回大乐斗首页').click() #这一句话是返回

if __name__ == '__main__':
    login(URL,username,pwd)