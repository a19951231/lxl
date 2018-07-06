import os#导入os这个包
from common1.data_pz import data

basth=os.path.dirname(os.path.dirname(__file__))#os.path.dirname(__file__)是获取本地路径，然后外面再加一个os.path.dirname()就是获取本地文件路径的上一级路径
print(basth)
app_path=os.path.join(basth,"app",data["appname"])#这里的os.path.join()方法是把路径拼接起来的
print(app_path)