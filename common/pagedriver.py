from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from common.Log import Logger
from selenium import webdriver
import os
class Action(object):
    #
    #封装所有页面都公用的方法
    #

    def __init__(self,driver,page_url=None,page_title=None):
        self.page_url=page_url
        self.page_title=page_title
        self.driver=driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.Test_log=Logger()
    def add_img(self,imgs):
        imgs.append(self.driver.get_screenshot_as_base64())
    def open(self):
        ## open方法调用_open进行打开链接
        self._open(self.page_url,self.page_title)
    def on_page(self,page_url):
        ##判断获取当前窗口Url地址，进行与配置地址作比较，返回比较结果（True False）
        return page_url in self.driver.current_url
    def _open(self,page_url,page_title):
        #打开页面，检验页面链接是否加载正确

        if page_url and page_title is not None:
            self.driver.get(page_url)
            #print("打开网址%s" % page_url)
            self.Test_log.info("打开网址%s" % page_url)
            #print("网页预期标题：%s" % page_title)
            self.Test_log.info("网页预期标题：%s" % page_title)
            # 使用assert进行校验，打开的链接地址是否与配置的地址一致。调用on_page()方法
            assert self.on_page(page_url),self.Test_log.error(u"打开页面%s失败" %page_url)
    def find_element(self,*locator):
        try:
            #print("定位元素：%s" % (locator,))
            self.Test_log.info("定位元素：%s" % (locator,))
            return WebDriverWait(self.driver,20).until(EC.presence_of_element_located(locator))
        except Exception as msg:
            self.Test_log.info(u"%s 页面中未能找到 %s 元素" %(self,locator))
            #print(u"%s 页面中未能找到 %s 元素" %(self,locator))
            #print("错误信息%s" %msg)
            self.Test_log.info("错误信息%s" %msg)
    def send_keys(self,locator,value,clear_first=True):
        #重新定义send_keys方法,元素内存在文本就先清空
        element=self.find_element(*locator)
        if clear_first :
            element.clear()
            element.send_keys(value)
        else:
            element.send_keys(value)
        #print("输入值：%s" % value)
        self.Test_log.info("输入值：%s" % value)
    def click_on(self,locator):
        #点击按钮
        self.find_element(*locator).click()
    def switch_frame(self,frame_loc):
        #切换frame
        self.driver.switch_to.frame(frame_loc)

