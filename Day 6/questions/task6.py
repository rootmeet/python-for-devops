#!/usr/bin/python

# membership operators
weekdays = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
days = weekdays
print("days is weekdays: ", (days is weekdays))
a = "hello"
b = "world"
print("a is not b: ", (a is not b))
print("Sunday is in weekdays: ", ("Sunday" in weekdays))
print("Iaitwar is in weekdays: ", ("Iaitwar" in weekdays))
print("Yellow not in weekdays:",  ("Yellow" not in weekdays))
print("Yellow in weekdays:",  ("Yellow" in weekdays))