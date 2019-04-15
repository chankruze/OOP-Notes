def new_decorator(func):

    def wrap_func():
        print("Code here before executing func")
        func()
        print("func() has been called")
    
    return wrap_func


@new_decorator # this does the same as `func_needs_decorator = new_decorator(func_needs_decorator)`
def func_needs_decorator():
    print("This function needs a decorator")

# run without wrapping a decorator.
# func_needs_decorator()

# reassign 'func_needs_decorator' by wrapping 'new_decorator' to 'func_needs_decorator'.
# this will modify the default behavier of the function which is wrapped in  a wrapper function.
#
# func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()

