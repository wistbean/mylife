# -*- coding: utf-8 -*-
################################################################
# 作者：小帅b                                                  #
#                                                              #
# 网站 : https://vip.fxxkpython.com                            #
#                                                              #
# 公众号：fxxkpython                                           #
#                                                              #
#                                                              #
# 声明:                                                        #
# 本项目为小帅b的VIP教程之一，仅供学员学习，禁止商用           #
#                                                              #
################################################################
from flask import render_template, request, url_for, redirect
from flask_login import current_user, login_user, login_required
from app.todo.forms import TodoListForm, TodoForm
from app.todo import todo
from app.models import Plan, SubPlan


@todo.route('/list', methods=['GET'])
@login_required
def todolist():
    form = TodoListForm()
    s = request.args.get('s', '')
    page = request.args.get('page', 1, type=int)
    page_num = 7
    pagination = Plan.query.with_parent(current_user) \
                           .whooshee_search(s) \
                           .order_by(Plan.create_at.desc())\
                           .paginate(page, per_page=page_num)
    todolist = pagination.items
    return render_template('todolist.html', form=form, todolist=todolist, pagination=pagination)


@todo.route('/list/done', methods=['GET'])
@login_required
def todolist_done():
    form = TodoListForm()
    todolist_done = []
    todolist = Plan.query.with_parent(current_user).all()
    for todo in todolist:
        if todo.get_done_percent == 100.0:
            todolist_done.append(todo)
    return render_template('todolist.html', form=form, todolist=todolist_done)


@todo.route('/list/add/', methods=['GET', 'POST'])
@login_required
def add_todolist():
    form = TodoListForm()

    if form.validate():
        body = request.form.get('todo')
        userid = current_user.get_id()
        plan = Plan(body=body, user_id=userid)
        plan.add()
        return redirect(url_for('todo.todolist'))

    return render_template('index.html')


@todo.route('/add/<int:plan_id>', methods=['POST'])
@login_required
def add_todo(plan_id):
    body = request.form.get('todo')
    user_id = current_user.get_id()
    sub_plan = SubPlan(body=body, user_id=user_id, plan_id=plan_id)
    todo_id = sub_plan.add()
    return f"""
                <div class="card-body border border-light">
                    <p class="card-text d-inline">{body}</p>
                    <input type="checkbox" data-todo-id="{todo_id}" value="{plan_id}" class="btn-check d-inline float-right"
                                                                                autocomplete="off">
                </div>
        
    """


@todo.route('/change/<int:sub_plan_id>', methods=['POST'])
@login_required
def change_todo_status(sub_plan_id):
    todo = SubPlan.query.get_or_404(sub_plan_id)
    if todo is not None:
        todo.change_status()
        done_count = todo.query.filter_by(
            is_done=True, plan_id=todo.plan_id).count()
        all_count = todo.query.filter_by(plan_id=todo.plan_id).count()
    return {'done': done_count, 'all': all_count}
