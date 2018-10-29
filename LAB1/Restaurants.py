class Restaraunts:

    def __init__(self, name, tables, max_dishes):
        self.name = name
        self.max_dishes = max_dishes
        self.tables = tables

    def __repr__(self):
        return str(self.name) + " " + str(self.tables) + " " + str(self.max_dishes)