# Python_Decorators



#What is a Decorator
A decorator is the name used for a software design pattern. 
Decorators dynamically alter the functionality of a function, method, or 
class without having to directly use subclasses or change the source code of the function being decorated.

#What is a Python Decorator
A Python decorator is a specific change to the Python syntax that allows us to more conveniently alter functions 
and methods (and possibly classes in a future version). 
This supports more readable applications of the DecoratorPattern but also other uses as well.


#Documentation:

Before we can understand decorators, we must first understand how functions work. 
####1) Functions assigned as Variables:
Function name can be assigned to a variable and that variable can be used to call the function.
#####Example:
```python
def get_name(name):
    return "Hello " + name

my_name = get_name
print(my_name("Kumar"))
```
```python
Output : Hello Kumar
```
####2) Functions inside other Functions:
Functions can be written inside function and can be used as following.
#####Example:

```python
def get_name(name):
    def say_hello():
        return "Hello "

    my_name = say_hello() + name
    return my_name

print(get_name("Kumar"))
```
```python
Output : Hello Kumar
```
####3) Functions as parameters:
Function names can be passed as parameter of other function and can be used as following.
#####Example:
```python
def get_name(name):
    return "Hello " + name

def my_name(func):
    return func("Kumar")

print(my_name(get_name))

```
```python
Output : Hello Kumar
```
####4) Functions return other Functions:
Functions can return another function and can be used as following.
#####Example:
```python
def get_name():
    def my_name():
        name = "Kumar"
        return "Hello " + name
        
    return my_name

name = get_name()
print(name())
```
```python
Output : Hello Kumar
```
####5) Enclosing scope of Functions:
These are called as "Closure" . A very powerful pattern that we will come across while building decorators. 
Another thing to note, Python only allows read access to the outer scope and not assignment. 
Notice how we modified the example above to read a "name" argument from the enclosing scope of the inner function 
and return the new function

#####Example:
```python
def get_name(name):
    def my_name():
        return "Hello " + name

    return my_name

name = get_name("Kumar")
print(name())
```
```python
Output : Hello Kumar
```
###Composition of decorators:
Function decorators are simply wrappers to existing functions. 
Putting the ideas mentioned above together, we can build a decorator. 
In this example let's consider a function that wraps the string output of another function by p tags.

#####Example:
```python
def get_name(name):
    return "Hello this is {0}".format(name)

def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
        
    return func_wrapper

my_name = p_decorate(get_name)
print(my_name("Kumar"))
```
```python
Output : <p>Hello this is kumar</p>
```
We can see from above example that function takes another function as an argument, generates a new function, 
augmenting the work of the original function, and returning the generated function so we can use it anywhere. 
To have get_name itself be decorated by p_decorate, we just have to assign get_name to the result of p_decorate.

```python
get_name = p_decorate(get_name)

print get_name("Kumar")
```

###Python's Decorator Syntax
Python makes creating and using decorators a bit cleaner and nicer for the programmer 
through some syntactic sugar. To decorate get_name we don't have to get_name = p_decorator(get_name).
There is a neat shortcut for that, which is to mention the name of the decorating function 
before the function to be decorated. The name of the decorator should be perpended with an @ symbol.

#####Example :
```python
def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))

    return func_wrapper

@p_decorate
def get_name(name):
    return "Hello this is {0}".format(name)

print(get_name("Kumar"))
```
```python
Output : <p>Hello this is kumar</p>
```

Now let's consider we wanted to decorate our get_name function by 2 other functions 
to wrap a div and strong tag around the string output.

#####Example :
```python
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

print(get_name("Kumar"))
print(my_name("Kumar"))
```
```python
Output : <p>Hello this is Kumar</p>
         <div><p><strong>Hello this is Kumar</div></p></strong>
```
###Decorating methods:
In Python, methods are functions that expect their first parameter to be a reference to the current object. 
We can build decorators for methods the same way, while taking self into consideration in the wrapper function.
#####Example :
```python
def p_decorate(func):
    def func_wrapper(self):
        return "<p>{0}</p>".format(func(self))

    return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "Umesh"
        self.lname = "Kumar"

    @p_decorate
    def get_fullname(self):
        return self.name + " " + self.lname

my_person = Person()
print(my_person.get_fullname())
```
```python
Output : <p>Umesh Kumar</p>
```
###Passing arguments to Decorators :
In the previous example we can notice how redundant the decorators are. 
3 decorators(div_decorate, p_decorate, strong_decorate) each with the same functionality 
but wrapping the string with different tags. We can definitely do much better than that. 
#####Example :

```python

def tags(tag_name):
    def tags_decorator(func):
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
```
```python
Output : <div><p><strong>Hello Umesh Kumar</strong></p></div>
```

In above example we can see that we have reduced the three different functions with same functionality to single function 
by just passing an argument to the decorator function.

###Debugging decorated function:
Finally decorators are just wrapping our functions, in case of debugging that can be problematic since the wrapper function does not carry the name, module and docstring of the original function. Based on the example above if we do:

```python
print(get_name.__name__)
print(get_name.__doc__)
print(get_name.__module__)
```
We can get output as :
```python
func_wrapper
None
__main__
```
The output was expected to be get_name yet, the attributes __name__, __doc__, and __module__ of get_name got overridden by those of the wrapper(func_wrapper. Obviously we can re-set them within func_wrapper but Python provides a much nicer way).

####Functools to the rescue
Python includes the functools module which contains functools.wraps. Wraps is a decorator for updating the attributes of the wrapping function(func_wrapper) to those of the original function(get_name). This is as simple as decorating func_wrapper by @wraps(func).
#####Example

```python
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
```
```python
Output : <div><p><strong>Hello Umesh Kumar</strong></p></div>
         get_name
         Returns the Name of person
         __main__
```
