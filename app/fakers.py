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
from faker import Faker
from app.models import Plan, SubPlan

faker = Faker('zh_CN')

def gen_faker_plan(count=10):
    for i in range(count):
        plan = Plan(body=faker.sentence(nb_words=10), user_id=12)
        plan_id = plan.add()
        for j in range(10):
            subplan = SubPlan(
                body=faker.text(max_nb_chars=35),
                plan_id=plan_id,
                user_id = 12
            )
            subplan.add()
                
