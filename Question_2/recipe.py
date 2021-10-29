import json
class Recipe:

    def __init__(self, name, cook_time, source):
        self.name = name
        self.cook_time = cook_time
        self.source = source
        pass

    def get_name(self):
        return self.name
        pass

    def get_cook_time(self):
        return self.cook_time
        pass

    def get_source(self):
        return self.source
        pass

    def set_image(self, url):
        pass

    def get_image(self):
        pass


class RecipeProcessor:

    def __init__(self):
        self.recipes = []

    def load_recipes(self, json_file):
        with open(json_file, "r") as f:
            recipes = json.load(f)
            new_recipe = Recipe(recipes[""], recipes[""], recipes[""])
            self.recipes.append(new_recipe)

    def get_recipes(self):
        return self.recipes

    def tabulate_recipes(self):
        pass
