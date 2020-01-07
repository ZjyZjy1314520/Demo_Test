from common.pagedriver import Action
from selenium.webdriver.common.keys import Keys
class Login(Action):

    name_loc=("name","email")
    password_loc=("name","password")
    enter_login_loc=Keys.ENTER
    frame_loc=(0)
    def __init__(self,driver,page_url=None,page_title=None):
        Action.__init__(self,driver,page_url,page_title)
    def open(self):
        #打开页面
        self._open(self.page_url,self.page_title)
    def chage_frame(self):
        #切换Frame
        self.switch_frame(self.frame_loc)
    def input_name(self,login_name):
        #输入登录名
        self.send_keys(self.name_loc,login_name)
    def input_password(self,login_password):
        #输入密码
        self.send_keys(self.password_loc,login_password)
    def enter_login(self):
        #模拟点击回车登录
        self.send_keys(self.password_loc,self.enter_login_loc,False)

    def get_login_message(self):
        #获取登录后title以断言
        return self.driver.title