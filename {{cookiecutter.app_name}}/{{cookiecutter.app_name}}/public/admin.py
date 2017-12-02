from flask_admin import AdminIndexView, expose, Admin
from flask_admin.menu import MenuLink
from flask_login import current_user

from {{cookiecutter.app_name}}.extensions import db
from {{cookiecutter.app_name}}.user.models import *
from flask import url_for, redirect, request
from flask_admin.contrib.sqla import ModelView

from {{cookiecutter.app_name}}.data.admin_view import DataModelView
from {{cookiecutter.app_name}}.data.models import Article



class MyHomeView(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/home.html')

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('user.login', next=request.url))


def register_admin(app):
    admin = Admin(app, name="管理后台",
                  template_mode='bootstrap3',
                  index_view=MyHomeView(name="首页"))
    # admin.add_view(DataModelView(Article, db.session, name="数据1-文章", endpoint="article.admin", category="基本数据"))
    admin.add_view(DataModelView(Article, db.session, name="文章", endpoint="article.admin"))
    admin.add_link(MenuLink(name='退出系统', url='/user/logout'))
