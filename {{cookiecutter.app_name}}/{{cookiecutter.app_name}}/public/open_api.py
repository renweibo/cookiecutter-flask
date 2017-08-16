# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from pprint import pprint

from flask import (Blueprint, request, render_template, flash, url_for, redirect, current_app, jsonify)
from {{cookiecutter.app_name}}.extensions import db

blueprint = Blueprint('api', __name__, url_prefix='/api')


@blueprint.route('/sample')
def sample():
    result = dict(code=0, msg='Hello World', data=list(range(10)))
    pprint(result)
    return jsonify(result)
