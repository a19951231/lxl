from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException#导入此异常处理的包
import logging
import logging.config
from common1.data_pz import data

CON_LOG = '../config1/log.conf'
logging.config.fileConfig(CON_LOG)
logging =logging.getLogger()

class BaseView1(object):

    def __init__(self,driver):
        self.driver=driver
    def find_element(self,loc,ka):
        try:  # try做判断，当找到下面的android:id/button2元素，会给予b，然后执行else里的代码，如果找不到直接报except里的错误
            b = WebDriverWait(self.driver, 20, 0.2).until(lambda x: x.find_element(by=loc,value=ka))  # 进行id定位
            # b=lxl.find_element_by_id("android:id/button2")#进行id定位
        except (NoSuchElementException, Exception) as e:
            logging.error(u'错误原因为: %s' % str(e))
        else:
            logging.info(data["ts"]["ts4"])
            return b.click()

    def find_element1(self,loc,ka,a):
        try:  # try做判断，当找到下面的android:id/button2元素，会给予b，然后执行else里的代码，如果找不到直接报except里的错误
            b = WebDriverWait(self.driver, 20, 0.2).until(lambda x: x.find_element(by=loc,value=ka))  # 进行id定位
            # b=lxl.find_element_by_id("android:id/button2")#进行id定位
        except (NoSuchElementException, Exception) as e:
            logging.error(u'错误原因为: %s' % str(e))
        else:
            logging.info(data["ts"]["ts4"])
            return b.send_keys(a)

    def find_elements1(self,loc,ka,a):
        try:  # try做判断，当找到下面的android:id/button2元素，会给予b，然后执行else里的代码，如果找不到直接报except里的错误
            b = WebDriverWait(self.driver, 20, 0.2).until(lambda x: x.find_elements(by=loc,value=ka)[a])#进行id定位
            # b=lxl.find_element_by_id("android:id/button2")#进行id定位
        except (NoSuchElementException, Exception) as e:
            logging.error(u'错误原因为: %s' % str(e))
        else:
            logging.info(data["ts"]["ts4"])
            return b.click()

    def find_elements2(self,loc,ka,a,c):
        try:  # try做判断，当找到下面的android:id/button2元素，会给予b，然后执行else里的代码，如果找不到直接报except里的错误
            b = WebDriverWait(self.driver, 20, 0.2).until(lambda x: x.find_element(by=loc,value=ka)[a])  # 进行id定位
            # b=lxl.find_element_by_id("android:id/button2")#进行id定位
        except (NoSuchElementException, Exception) as e:
            logging.error(u'错误原因为: %s' % str(e))
        else:
            logging.info(data["ts"]["ts4"])
            return b.send_keys(c)

    def find_element2(self,loc,ka):
        try:  # try做判断，当找到下面的android:id/button2元素，会给予b，然后执行else里的代码，如果找不到直接报except里的错误
            b = WebDriverWait(self.driver, 20, 0.2).until(lambda x: x.find_element(by=loc,value=ka))  # 进行id定位
            # b=lxl.find_element_by_id("android:id/button2")#进行id定位
            return b
        except (NoSuchElementException, Exception) as e:
            logging.error(u'错误原因为: %s' % str(e))

    def find_elements3(self,loc,ka,a):
        try:  # try做判断，当找到下面的android:id/button2元素，会给予b，然后执行else里的代码，如果找不到直接报except里的错误
            b = WebDriverWait(self.driver, 20, 0.2).until(lambda x: x.find_elements(by=loc,value=ka)[a])  # 进行id定位
            # b=lxl.find_element_by_id("android:id/button2")#进行id定位
            return b
        except (NoSuchElementException, Exception) as e:
            logging.error(u'错误原因为: %s' % str(e))

    def get_window_size1(self):#获取屏幕的宽方法封装
        try:
            return self.driver.get_window_size()['width']
        except(NoSuchElementException,Exception) as e:
            logging.error(u'错误原因为: %s' % str(e))

    def get_window_size2(self):#获取屏幕的高方法封装
        try:
            return self.driver.get_window_size()['height']
        except(NoSuchElementException,Exception) as e:
            logging.error(u'错误原因为: %s' % str(e))

    def swipe1(self,start_x, start_y, end_x, end_y, duration):#把滑动方法进行封装
        try:
            return self.driver.swipe(start_x, start_y, end_x, end_y, duration)
        except(NoSuchElementException, Exception) as e:
            logging.error(u'错误原因为: %s' % str(e))