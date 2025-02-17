# When to use @classmethod and @staticmethod

class Item:
    @staticmethod
    def is_integer(num):
        '''
                This should do something that has a relationship
                with class, but not something that must be unique
                per instance!
        '''
    @classmethod
    def instantiate_from_something(cls):
        '''
        This should also do something that has a relationship
        with class, but usually those are used to manipulate
        different structures of data to instantiate objects, like
        we have done with CSV.
        :return:
        '''
# However, those could be also called from instances
item1 = Item()
item1.is_integer(5)
item1.instantiate_from_something()