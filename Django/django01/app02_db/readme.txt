settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'webdb',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app02_db',
]

python manage.py makemigrations
python manage.py migrate
python manage.py syncdb


models(注意 : migration文件夹下的代码)
创建数据库对象
一对多
多对多

数据的增删改查
max_length
default
null
id  主键primary key
auto_now
choice

filter


模板方法 和页面展示
TEMPLATE_DEBUG=True
TEMPLATE_DIRS=(
	os.path.join(BASE_DIR,'templates')
)

自定义simple_tag

include页面

CSRF verification failed. Request aborted. 跨站请求伪造
可以先注掉 #'django.middleware.csrf.CsrfViewMiddleware',


用户名:{{form.username}}	<br/>
邮件:{{ form.email }}		<br/>
or
{{form.as_table}}	<br/>


动态路由 ????

作业 主机管理
用户组 用户       多对多关系  一个用户组 对应 多个用户  
主机表 用户组 一对多关系   一个用户组 对应多个主机
用户注册 登录
主机信息展示 IP 型号 等等
用母版子版 的概念 
静态文件 怎么导入
	

创建 新的项目
创建 目录 templates static
配置  templates static 的路径

model 多对多 一对多 的增删改查  自己好好练习 这个是重点


form

