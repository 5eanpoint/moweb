#开发框架

开发环境：Python2.7 + Flask + sqlite + virtualenv + 扩展 + pycharm（ide），扩展包参看目录中的requirements.txt



#部署环境
环境：Python2.7 + virtualenv + nginx + tornado

#补充说明
1. web中的图表是以简单的REST方式提供数据，REST的脚本统一放在/app/main/views.py中，然后通过jquery的get和each方法获取json，然后遍历得到每一个item。
2. 新增静态页面放在/app/main/templates/中，采用Jinja2模板，模板的继承关系为：静态页面<-base.html<-flask.ext.bootstrap扩展中的base.html，一般情况下不要修改bootstrap扩展中的文件。
3. 所有的图片、css、js脚本均放在/app/static/中。
4. 初次使用需要安装python环境、pip及virtualenv，安装完成后，执行`pip install -r requirements.txt`安装扩展，然后执行`source ./venv/bin/activate`激活virtualenv虚拟环境（此命令针对linux环境，windows自行百度），激活之后即可进行调试
5. 数据库使用的是python27自带的sqlite，所有的配置均写在config.py中。
