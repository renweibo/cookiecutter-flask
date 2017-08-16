from flask import (Blueprint, request, render_template, flash, url_for, redirect, current_app, jsonify)
from vps_status.extensions import db

blueprint = Blueprint('data', __name__, url_prefix='/data')
