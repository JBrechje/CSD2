def my_function():
  print("function:", "Hello from a function")

my_function()
my_function()
my_function()

def my_function_pass():
  # if u need a placeholder use; pass
  pass


#function that returns a value
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print("function that returns value:", message)

#function that returns a value directly
def get_greetings():
  return "Hello from a function"

print("function that returns value directly:", get_greetings())


#reusable code
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print("celsius", fahrenheit_to_celsius(77))
print("celsius", fahrenheit_to_celsius(95))
print("celsius", fahrenheit_to_celsius(50))



  #arguments
def my_function(argument):
  print(argument)

my_function("....................from here: arguments..............................")


#arguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
my_function("anthony")

#parameters
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument