def get_name(name):
    return "Hello this is {0}".format(name)


def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))

    return func_wrapper


my_name = p_decorate(get_name)

print(my_name("Umesh"))
