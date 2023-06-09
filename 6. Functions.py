def greet_user():      # without parameter
    print('inside function')
greet_user()
print('outside function')

for i in range(2,4):  # instead of list for in in [1,2,3,4] use range
    print("hi")
 
for _ in range(2,4):   # since we are never using the variable i, so we can replace it with single underscore
    print("hi")


def greet_user(first_name,last_name):   # since it has (name) parameter defined, when using this function a argument must be passed
    print(f'Hi {first_name},{last_name}')
greet_user("Vikram","Solanki")
print('outside function')

def greet_user(first_name,last_name):
    print(f'Hi {first_name},{last_name}')
greet_user(first_name="Vikram",last_name="Solanki") #Keyword argument for easy read of function
print('outside function')

def square(number):
 print("number * number")
result = square(2)
print(result) # prints 4
# why does this return None whereas the above function does not return None


# Keyword argument can be passed as 1. positional, 2. default, 3. Keyword, 4.arbitrary
# 1 positional
def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")
hello("Hello", "Mr.", "John", "James")

# 2 default
def net_price(list_price, discount=0, tax=0.05):
   return list_price * (1 - discount) * (1 - tax)
print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 0.1, 0))

# 3 Keyword
def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")
hello("Hello", title="Mr.", last="John", first="James")

# 4 arbitary which is like - in this example
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=1, area=123, first=456, last=7890)
print(phone_num)


# *args       = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#                      * unpacking operator
# ARGS class tuple
def add(*args):    # *args it creates all parameter into a TUPLE and pass it to function.
   total = 0
   for args in args:
       total += args
   return total
print(add(1, 2, 3, 4))

def display_name(*args):
   print(f"Hello", end=" ")
   for arg in args:
       print(arg, end=" ")
display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")

# KWARGS class dictionary
def print_address(**kwargs):
    for value in kwargs.values():
        print(value, end=" ")
print_address(street="123 Fake St.",
              pobox="P.O Box 777",
              city="Detroit",
              state="MI",
              zip="54321")


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants",
               street="123 Fake St.",
               pobox="PO box #1001",
               city="Detroit",
               state="MI",
               zip="54321")

# variable scope resolution  priority order 1. Local -> 2. Encloded -> 3. Global -> built in

# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
#
# lambda parameters:expression

double = lambda x: x * 2
print(double(1))

multiply = lambda x, y: x * y
print(multiply(1,2))

add = lambda x, y, z: x + y + z
print(add(1,2,3))

full_name = lambda first_name, last_name: first_name+" "+last_name
print(full_name("vikram","solanki"))


# func in a variable
def hello():
    print("Hello")
hi = hello
hi()
# say = print
# say("Whoa! I can't believe this works! :O")


# ---------------------------------------------------------------------------------------------------------------
# map() =   applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function,iterable)

store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]

to_euros = lambda data: (data[0],data[1]*0.82)
# to_dollars = lambda data: (data[0],data[1]/0.82)

store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)
# ---------------------------------------------------------------------------------------------------------------

# FILTER FUNCTION--------------------------------------
# filter() =    creates a collection of elements from an iterable,
#               for which a function returns true
#
#               filter(function, iterable)


