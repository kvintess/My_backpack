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
    def __str__(self):
        return 'backpack:' + ','.join(self.content)

    def __bool__(self):
        return self.content != []

    def __eq__(self, other):
        return self.content != other.content

    def __add__(self, other):
        new_obj = Backpack()
        new_obj.content.extend(self.content)
        if isinstance(other, Backpack):
            new_obj.content.extend(other.content)
        else:
            new_obj.content.extend(other)
        return new_obj

#окей идем дальше
#расширенное присвоение += -= и т.д
    def __iadd__(self, other):
        self.content.extend(other.content)
        return self

my_backpack = Backpack()
my_backpack.add('tetrad')
my_son_backpack = Backpack()
my_son_backpack.add('ruchka')
my_backpack += my_son_backpack
print(my_backpack)


