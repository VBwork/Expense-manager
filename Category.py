import json
import os

class Category:
    def __init__(self, name):
        self.name = name

    def to_dict(self):
        category = self.name
        return category

    def __repr__(self):
        return self.name


class CategoryManager:
    file_categories = 'categories.json'
    new_category = 0

    def __init__(self):
        self.categories = self.load_data_categories()

    def add_category(self, category):
        self.new_category = len(self.categories) + 1
        self.categories[str(self.new_category)] = category
        self.save_data_categories()

    def get_categories(self):
        return self.categories

    def load_data_categories(self):

        if os.path.exists(self.file_categories):
            with open(self.file_categories, 'r') as openfile:
                categories = json.load(openfile)
        else:
            categories = {'1': 'Food', '2': 'Transport', '3': 'Home', '4': 'Close'}

        return categories

    def to_dict(self):
        return self.categories

    def save_data_categories(self):
        save_categories = json.dumps(self.categories, default = lambda o: o.to_dict(), indent = 4)

        with open(self.file_categories, 'w') as f:
            f.write(save_categories)