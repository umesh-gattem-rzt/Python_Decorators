from functools import wraps


def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))

        return func_wrapper

    return tags_decorator


@tags("div")
@tags("p")
@tags("strong")
def get_name(name):
    """Returns the Name of person"""
    return "Hello " + name


print(get_name("Umesh Kumar"))

print(get_name.__name__)
print(get_name.__doc__)
print(get_name.__module__)
