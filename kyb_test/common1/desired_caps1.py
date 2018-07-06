from appium import webdriver
import logging#导入logging
from common1.app_luj import data,app_path##导入配置好的data，用来读取yaml里面的数据和app路径
import logging.config

CON_LOG='../config1/log.conf'#../是返回上一层，然后读取confing1这个路径里的log.conf文件
logging.config.fileConfig(CON_LOG)#然后使用config.fileConfig去读取这个文件
logging1=logging.getLogger()#配置文件


def appium_desired():

    desired_caps={}
    desired_caps['platformName']=data['platformName']
    desired_caps['platformVersion']=data['platformVersion']
    desired_caps['deviceName']=data['deviceName']

    #desired_caps['app']=data['app']
    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']
    desired_caps['noReset']=data['noReset1']
    #desired_caps["app"]=app_path#获取app路径，这个测试app下载安装才配置，如果手机有我们测试的app就不用配置

    desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
    desired_caps['resetKeyboard']=data['resetKeyboard']
    desired_caps["noReset"]=data["noReset1"]

    driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
    logging.info(data["ts"]["ts1"])
    driver.implicitly_wait(8)
    return driver

if __name__ == '__main__':
    appium_desired()#启动app
