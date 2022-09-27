class Backpack:
    def __init__(self):
        self.content= []
    def add(self, item):
        self.content.append(item)
        print('Положил в рюкзак', item)
    def inspect(self):
        #проверим,что внутри
        print('тут лежит:')
        for item in self.content:
            print('  ',item)
my_backpack= Backpack()
my_backpack.add('зарядка')
my_backpack.add('ноут')
my_backpack.inspect()