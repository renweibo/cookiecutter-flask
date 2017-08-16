import arrow
import markdown2
from flask import url_for, redirect, request
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from jinja2 import Markup
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name

class BaseModelView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('user.login', next=request.url))


def updated_formatter(v, c, m, p):
    return arrow.get(m.updated).to('Asia/Shanghai').humanize(locale="zh_cn")


def created_formatter(v, c, m, p):
    return arrow.get(m.created).to('Asia/Shanghai').humanize(locale="zh_cn")


def md_formatter(s):
    return Markup(markdown2.markdown(s))


def code_formatter(code, code_type):
    lexer = get_lexer_by_name(code_type)
    formatter = HtmlFormatter(noclasses=True)
    result = highlight(code, lexer, formatter)
    return Markup(result)
