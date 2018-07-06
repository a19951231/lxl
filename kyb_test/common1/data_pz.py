import yaml

with open('../config1/kyb.yaml', 'r', encoding="utf-8") as file:  # 这样写法比较好，就算我们文件不close，也不会说读取不了或释放不了
    data = yaml.load(file)  # 然后使用yaml.load()方法读取file这个文件并且给予data