# name error

n=40
f=10
try:
    print("Div ,m+1")
except(NameError):
    print("name error")

# type error
o='2'
p=2
try:
    print("o+p",o+p)
except(TypeError) :
    print("type error")


#value error
try:
    y=int(input("Enter a variable to raise the error"))
except(ValueError):
    print("value error")


# divide by zero
x=6
y=0
try:
    print("Dividing by zero",x/y)
except(ZeroDivisionError):
    print("divide by zero error")

#flow error

x=687.28
y=29281762513141.52
try:
    print("the addition is :",x**y)
except(OverflowError):
    print("overflow error occured")

#unboundlocal error


    x=10
try:
    def bar():
        print(x)
        x=x+1
    bar()
except:
    print("this is unboundlocalError :")


# syntax error
amount= 10000
try:
    if(amount > 2999)
    print("this is syntax error ")

