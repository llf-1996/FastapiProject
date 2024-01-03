# -*- coding: utf-8 -*-
"""
@Author: llf
@Email: 
@Time: 2023/08/26
@desc: 
"""
# 性能测试
# pip install locust
from locust import HttpUser, TaskSet, task


# 定义用户行为
class UserBehavior(TaskSet):

    @task
    def baidu_index(self):
        self.client.get("/")


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]  # 指向一个定义的用户行为类
    min_wait = 3000  # 执行事务之间用户等待时间的下界（单位：毫秒）
    max_wait = 6000  # 执行事务之间用户等待时间的上界（单位：毫秒）


if __name__ == "__main__":
    # http://localhost:8089
    import os

    os.system("locust -f locust_demo.py --web-host=localhost --web-port=8089 --host=https://www.lilinfeng.work")
