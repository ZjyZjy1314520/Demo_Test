import unittest
from time import sleep
from page.login_page import Login
from selenium import webdriver
#from BeautifulReport import BeautifulReport
class Demo(unittest.TestCase):
    def setUp(self):
        self.url="https://mail.163.com"
        self.title="网易"
        self.user_name="13075910470" #账号
        self.user_password="zjy1314520" #密码
        self.driver=webdriver.Chrome()
        self.imgs=[]
        # @BeautifulReport.add_test_img("测试报告")
    def test_1_login(self):
        self.login_page=Login(self.driver,self.url,self.title)
        self.login_page.open()
        self.login_page.click_on(("id","lbNormal"))
        self.login_page.chage_frame()
        sleep(3)
        self.login_page.input_name(self.user_name)
        self.login_page.input_password(self.user_password)
        sleep(2)
        #login_page.save_img("测试报告") #截图
        self.login_page.click_on(("id","dologin"))
        sleep(2)
        self.login_page.add_img(self.imgs)
        print(self.login_page.get_login_message())
        assert "网易邮箱6.0版" in self.login_page.get_login_message()

    def tearDown(self):
        print("结束")
        self.driver.close()
if __name__=="__main__":
    unittest.main()