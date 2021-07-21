# MyBookStore
BookStoreProject
项目运行详细说明，运行环境将在这里说明

项目环境  Python 3.9.6 + Django 3.2.5

项目下载 git clone https://github.com/anzhaoyun/MyBookStore.git

安装所有依赖环境 pip install -r requirements.txt

在MyBookStore -> settings.py 中配置自己的MySQL链接，
其中{'USER':'root','PASSWORD':'123456'}为自己的数据库的用户名和密码，
请输入自己的mysql数据库用户名和密码，并建立mybookstore数据库，设置字符集为utf8mb4

创建数据库迁移 python manage.py makemigrations

执行数据库迁移 python manage.py migrate

服务器开启 python manage.py runserver 

#创建后台超级管理员 python manage.py createsuperuser

#创建新的APP python manage.py startapp library