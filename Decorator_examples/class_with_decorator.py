def p_decorate(func):
    def func_wrapper(self):
        return "<p>{0}</p>".format(func(self))

    return func_wrapper


# def p_decorate(func):
#     def func_wrapper(*args, **kwargs):
#         return "<p>{0}</p>".format(func(*args, **kwargs))
#
#     return func_wrapper


class Person(object):
    def __init__(self):
        self.name = "Umesh"
        self.lname = "Kumar"

    @p_decorate
    def get_fullname(self):
        return self.name + " " + self.lname


my_person = Person()

print(my_person.get_fullname())
