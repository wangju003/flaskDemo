from flask import Flask
#引入Flask_Sqlalchemy
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()#实例化SQLAlchemy

#这样写为什么会出错？ ModuleNotFoundError: No module named '__main__.views'; '__main__' is not a package
# from .views.user import user
from app.views.user import user

#创建app
def create_app():
    app = Flask(__name__)
    app.debug=True
    #设置配置文件
    app.config['JSON_AS_ASCII'] = False  # 指定json编码格式 如果为False 就不使用ascii编码
    app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"  # 指定浏览器渲染的文件类型，和解码格式；

    #注册蓝图
    app.register_blueprint(user)
    return app
    #得到了1个app

if __name__=='__main__':
    appp = create_app()
    appp.run()