from scripts import base
from web import models

def run():
    exists = models.PricePolicy.objects.filter(category=1,title="个人免费版").exists()
    if not exists:
        models.PricePolicy.objects.create(
            category=1,
            title="个人免费版",
            price=0,
            project_num=2,
            project_member=2,
            project_space=20,
            each_file_size=5,

        )

if __name__ == '__main__':
    run()