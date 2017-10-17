class Things(object):


    def __init__(self, name1, name2, name3):
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3

    def basket(self):
        print('In the basket put:', self.name1, self.name2)

    def bag(self):
        print('In the bag put:', self.name2, self.name3)


things = Things('apple,', 'melon', 'flower')
things.basket()
things.bag()
