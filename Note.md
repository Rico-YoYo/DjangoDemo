# 开发中的注意点



 >### 怎样删除github上的文件夹，但不删除本地文件夹
 >#### 步骤：（以删除.idea文件夹为例）
 > 1.git rm -r --cached .idea  #--cached不会把本地的.idea删除  
2.git commit -m 'delete .idea dir'  
3.git push -u origin master`


# python 项目自动生成requirements.txt文件
> 1.生成：
> pip freeze > requirements.txt

> 2.安装：
> pip install -r requirements.txt
