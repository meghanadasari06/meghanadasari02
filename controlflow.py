#if 
 
if 10>5:
    print("!0 is greater ")

#if else

a=20
n=int(input("enter number"))

if a>n:
      print(a,"is greater")
else: 
      print(a,"is smaller")


#elif

if n>0:
      print("positive number")
elif n==0 :
      print("number is zero")
else :
      print("negative number")

    
#for loop 
number=[1,2,3,6,5,6,7,8,9]
sum=0
num=0
for num in number :
    sum=sum+num
    print("sum : ",sum)


#range ()
print("range seque ",range(10))
print("range sequance allitems is " , list(range(10)))

#while loop
s=0
i=1
b=700
while i<=b:
      s=s+i
      i=i+1
print("sum =",s)

#break 
if 10<5 :
   Pass
for b in "hello python" :
    if b=='y':
        break 
        print(b)


#continue 
for b in "hello python" :
    if b=='y' :
       continue 
    print(b)


    #pass 
    print("pass statement ")
    if 10>5:
        pass



