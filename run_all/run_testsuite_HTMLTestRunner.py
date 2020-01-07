from common.HTMLTestRunner import HTMLTestRunner
import time
import unittest
path=r'G:\UI_Test\Demo_Test'
if __name__=='__main__':
    suite=unittest.defaultTestLoader.discover(path+r'\test_case',"test_163_login.py")
    filename=path+"/report/"+time.strftime("%Y-%m-%d %H_%M_%S")+".html"
    file=open(filename,"wb")
    HTMLTestRunner(stream=file,title=u"自动化测试报告",description=u"测试用例情况").run(suite)
    file.close()