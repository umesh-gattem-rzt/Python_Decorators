def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))

    return func_wrapper


def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))

    return func_wrapper


def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))

    return func_wrapper


@p_decorate
def get_name(name):
    return "Hello this is {0}".format(name)


@div_decorate
@p_decorate
@strong_decorate
def my_name(name):
    return "Hello this is {0}".format(name)


print(get_name("Umesh"))
print(my_name("Umesh"))
