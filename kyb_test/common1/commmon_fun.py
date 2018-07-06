from baseView1.baseView2 import BaseView1
from common1.desired_caps1 import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging
from common1.data_pz import data
import time,os

class Common(BaseView1):
    def check_cancelBtn(self):
        logging.info(data["ts"]["ts2"])
        BaseView1.find_element(self,data["ys"][0]["id"],data["ys"][0]["ys1"])

    def check_skipBtn(self):
        logging.info(data["ts"]["ts3"])
        BaseView1.find_element(self,data["ys"][1]["id"],data["ys"][1]["ys2"])

    def get_size(self):#定义一个方法，获取手机屏幕的宽和高
        x = self.get_window_size1()#self是this的意思
        y = self.get_window_size2()
        return x, y

    def swipeLeft(self):#定义一个向左滑动的方法
        logging.info('swipeLeft')#log打印
        l = self.get_size()#把get_size()这个方法返回的x，y给予l
        x1 = int(l[0] * 0.9)#然后定义开始滑动的x点
        y1 = int(l[1] * 0.5)#然后定义开始滑动的y点
        x2 = int(l[0] * 0.1)#然后定义结束滑动的x点
        self.swipe1(x1, y1, x2, y1, 1000)#因为我们的类继承BaseView1的类，所以我们可以调用BaseView1的类的swipe1滑动方法

    def getTime(self):#定义一个获取时间的方法
        self.now=time.strftime("%Y-%m-%d %H_%M_%S")#重新定义一个获取时间方法，time.strftime("%Y-%m-%d %H_%M_%S")就是把时间定义为年/月/日/时/分/秒
        return self.now#返回获取的时间

    def getScreenShot(self,module):#定义一个截图的方法
        try:
            time=self.getTime()#把getTime这个获取的时间方法给予time
            image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots1/%s_%s.png' %(module,time)#然后使用os.path.dirname(os.path.dirname(__file__))获取这个文件的上级文件，然后'/screenshots/%s_%s.png' %(module,time)就是图片存放/screenshots1/路径里，并且命名为xxx.png图片

            logging.info('get %s screenshot' %module)#日志打印
            self.driver.get_screenshot_as_file(image_file)#截图的图片存放的路径和图片名称
        except (NoSuchElementException, Exception) as e:
            logging.error("不能截图出现的错误是%s"%str(e))

    def check_market_ad(self):#判断是否存在关闭按钮的方法
        logging.info('====check_market_ad====')
        try:
            element=self.find_element2(data["ys"][0]["id"],data["ys"][5]["chaann"])
        except NoSuchElementException:
            pass
        else:
            logging.info('close market ad')
            return element.click()

if __name__ == '__main__':
    driver=appium_desired()
    com=Common(driver)
    com.check_cancelBtn()
    #com.check_skipBtn()
    com.swipeLeft()
    com.getScreenShot("滑动页面截图")
    com.check_skipBtn()