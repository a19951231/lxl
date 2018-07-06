import sys#导入sys
path="C:\\kyb_test\\"#设置路径
sys.path.append(path)#使用sys调用路径，这样我们在cmd里或jenks里运行不会报我们导入的下面的包的错误
import logging
from common1.commmon_fun import Common
from common1.desired_caps1 import appium_desired
from selenium.common.exceptions import NoSuchElementException
import yaml
from common1.data_pz import data#调用封装好的yaml模块


#file = open('../lxl1/fz.yaml', 'r')
#data = yaml.load(file)

class LoginView(Common):
    def login_action(self,username,password):
        #self.check_cancelBtn()#调用commmon模块里的Common类里的check_cancelBtn方法并且运行
        #self.check_skipBtn()#调用commmon模块里的Common类里的check_skipBtn()方法并且运行
        Common.check_cancelBtn(self)
        Common.swipeLeft(self)
        Common.check_skipBtn(self)

        logging.info(data["ts"]["ts5"])
        logging.info('username is:%s' %username)
        Common.find_element1(self,data["ys"][2]["id"],data["ys"][2]["zhh"],username)#因为LoginView方法继承了Common方法，而Common方法继承了BaseView1方法，BaseView1方法继承object，所以我们可以使用Common调用BaseView1里的方法

        logging.info('password is:%s'%password)
        Common.find_element1(self,data["ys"][3]["id"],data["ys"][3]["mm"],password)#也可以把Common换成self去调用find_element1方法,使用self调用，（）里就不要有self，self就是Java的this的意思

        logging.info('click loginBtn')
        Common.find_element(self,data["ys"][4]["id"],data["ys"][4]["dlann"])
        logging.info('login finished!')

    def check_account_alert(self):#定义一个登录成功后判断是否有那个提醒框，
        logging.info(data["ts"]["ts6"])
        try:
            element = self.find_element2(data["ys"][0]["id"],data["ys"][7]["qdann1"])#定位提醒框的确定元素
        except NoSuchElementException:#人工没有就提示pass跳过
            pass

    def logout_action(self):#退出app操作
        logging.info(data["ts"]["ts7"])#打印日志
        self.find_element(data["ys"][0]["id"],data["ys"][10]["RightButton"])#点击设置按钮
        self.find_element(data["ys"][0]["id"],data["ys"][11]["logoutBtn"])#在设置页面点击退出按钮
        self.find_element(data["ys"][0]["id"],data["ys"][7]["qdann1"])#点击退出按钮会弹出一个确定退出的框，点击确定

    def check_loginStatus(self):#登录成功后的操作方法
        logging.info(data["ts"]["ts10"])
        self.check_market_ad()#调用commmon里的check_market_ad()方法
        self.check_account_alert()#调用check_account_alert(self)方法
        #上面2个方法都是判断登录成功后，是否有这2个弹框出现，如果有就点击操作，如果没有就跳过

        try:
            self.find_element(data["ys"][0]["id"],data["ys"][8]["woann"])#然后点击我的按钮，跳转到我的的页面
            self.find_element2(data["ys"][0]["id"],data["ys"][9]["username"])#在我的页面里判断是否有这个用户名称元素存在
        except (NoSuchElementException,Exception) as e:#获取不了try里面的元素会执行下面的操作
            logging.error('错误原因为: %s' % str(e))#报错
            self.getScreenShot(data["ts"]["ts9"])#进行截图操作
            return False#返回false
        else:#如果存在就执行下面的代码
            logging.info(data["ts"]["ts8"])#打印日志
            self.logout_action()#调用logout_action()方法进行退出app操作
            return True#返回true



if __name__ == '__main__':
    driver=appium_desired()
    l=LoginView(driver)
    l.login_action(data["username1"],data["password1"])
    l.check_loginStatus()#调用这个方法