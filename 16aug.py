# find ASCII value of a character 'X' and 'x'
d='x'
print("the ASCII value of'" + d + "' is",ord(d))

#write program to computer Quotient and Remainder 
m=6
d=8

n=m/d
print("Quotient is",n)
g=m%d
print("Remainder is",g)

#swap two numbers using temporary variable 
x=15
y=20
temp = x
x=y
y= temp 

print("x value after swapping is",x)
print("y value after swapping is",y)

# write program to check whether a number is even or odd -88,37,1658
num=88371658

if (num % 2) == 0:
    print("{0} is even". format(num))
else:
    print("{0} isodd".format(num))

#check whether an alphabet is vowel or consonant using if...else statement -a,b,e,o
x='a'
if x in('a','e','i','o','u'):
    print("the given alphabet is vowel",x)
else:
    print("the given alphabet is consonant",x)

#write program to calculate monthly simple intrest and compund intrest(5%month) on amount - 161258/-
p=161258
r=6
t=30
print('the principal is',p)
print('the rate is',r)
print('the time is',t)

si=(p*r*t)/100
print(' the simple intrest is', si)

#program to calculate GST i.e 18%on base price 34900/-

bp=34900
GST=0.18 * bp 
print("GST =", GST)

#program to generate equated monthly instalment (EMI)(intrest)5%month of 3 year and 5 year of amount 161258/-
a=161258
e3=a/36
e5=a/60

emi=e3+(0.05*e3)
emi=e5+(0.05*e5)
print(" EMI for 3 year with intrest",emi)
print(" EMI for 5 year with intrest",emi)




