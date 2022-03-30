#!/usr/bin/env python3
def display(func):
    def inner():
        print("Executing", func.__name__, "function")
        func()
        print("Finish")
    return inner

@display #Passing decorated function as parameter. I can add 2 or more decorators
def printer():
    print("Hello world!")

printer() #When I call function It calls decorated function


