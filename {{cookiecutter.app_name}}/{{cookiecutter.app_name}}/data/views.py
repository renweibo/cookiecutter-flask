from flask import (Blueprint, request, render_template, flash, url_for, redirect, current_app, jsonify)
from {{cookiecutter.app_name}}.extensions import db

blueprint = Blueprint('data', __name__, url_prefix='/data')
