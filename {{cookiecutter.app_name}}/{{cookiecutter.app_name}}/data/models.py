from sqlalchemy_utils import Timestamp
from {{cookiecutter.app_name}}.extensions import db


class Article(db.Model, Timestamp):
    __tablename__ = 'article'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.Unicode(), default='')
    source = db.Column(db.Unicode(), default='')
    text = db.Column(db.UnicodeText())
    comment = db.Column(db.UnicodeText())
