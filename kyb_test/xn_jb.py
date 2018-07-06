from locust import HttpLocust, TaskSet, task

# 定义用户行为
class UserBehavior(TaskSet):

    @task(5)
    def baidu_index(self):
        self.client.get("/")

    @task(6)
    class AboutPage(TaskSet):
        @task
        def on_init(self):
            self.client.get("/betHall/overview")

        @task
        def team_page(self):
            self.client.get("/betHall/betting/5b050d394fe900202c2935a4")

        @task
        def press_page(self):
            self.client.get("/lotteryResult/chart?id=5a9fb7d065308f1fc03b0904")

        @task
        def press_page1(self):
            self.client.get("/lotteryResult/chart?id=5a9fb67465308f1e0d557b38")

        @task
        def press_page2(self):
            self.client.get("/betHall/betting/5a9fb24865308f187e1670b3")

        @task
        def press_page3(self):
            self.client.get("/betHall/betting/5a9fb37f65308f18075b6ea5")

        @task
        def stop(self):
            self.interrupt()


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000
