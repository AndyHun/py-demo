from Person import Person


class Scholar(Person):
    """Scholar Class
    不需要显示调用父类Person.__init__(self, name), 因为本身没有定义 __init__
    覆盖父类 类属性 basic_intelligence_level
    重写父类 say_hi
    """
    # class variable, shared by all instance
    basic_intelligence_level = 'HIGH'

    def say_hi(self):
        print('Hello!, My name is:', self.name)

    @staticmethod
    def study():
        print("I am studying!")
