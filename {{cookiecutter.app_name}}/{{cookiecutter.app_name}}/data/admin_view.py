from {{cookiecutter.app_name}}.common.admin_common import BaseModelView, updated_formatter, created_formatter
from {{cookiecutter.app_name}}.data.models import *


class DataModelView(BaseModelView):
    can_delete = True
    can_create = True
    can_edit = True
    can_view_details = True
    column_labels = dict(id='序号', comment='备注', updated='更新时间', created="创建时间")

    # column_list = ('updated', 'comment',)
    column_formatters = dict(updated=updated_formatter, created=created_formatter, )
    # column_sortable_list = column_list
    column_default_sort = ('updated', True)
    column_editable_list = ('comment',)

    # column_details_list = ('title', 'source', 'updated', 'text', 'comment',)
    # column_details_list = form_columns
    form_widget_args = {
        'comment': {'rows': 5}
    }
    page_size = 30
