import requests
import json


class InsertFixtures():

    def __init__(self, file_name):
        self.file_name = file_name
        self.projects = self.get_projects()
        self.categories = self.get_categories()

    def get_projects(self):
        with open(self.file_name, 'r') as f:
            return json.load(f)['projects']

    def get_categories(self):
        with open(self.file_name, 'r') as f:
            return json.load(f)['categories']

    def post_projects(self):
        for project in self.projects:
            print(project)
            response = requests.post("http://localhost:3080/projects/create/", json=project)
            response.raise_for_status()

    def post_categories(self):
        for category in self.categories:
            print(category)
            response = requests.post("http://localhost:3080/categories/create/", json=category)
            response.raise_for_status()


obj = InsertFixtures('fixtures.json')
obj.post_categories()
obj.post_projects()
