import unittest,time
from common.BeautifulReport import BeautifulReport
from test_case import test_163_login
now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
report_title='用例执行报告'+now+'.html'
report_path=r'G:\UI_Test\Demo_Test\report'

# 报告地址&名称
report_title = r'Example报告_' + now + ".html"  # 如果不能打开这个文件，可能是now的格式，不支持：和空格
if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader=unittest.TestLoader()
    suite.addTests(loader.loadTestsFromModule(test_163_login))
    #运行用例filename=报告名称，description=所有用例总的名称，report_path=报告路径,如果不填写默认当前执行文件目录
    BeautifulReport(suite).report(filename=report_title, description='登录模块',log_path=report_path)