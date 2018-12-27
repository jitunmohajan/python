#print hello world
print("Hello world")


#    take a user 
inputz=input() #this will take a string as input
print(len(z)) #here len mean string length
z=int(input("insert the new input>>"))

print(type(z)) # find varriable type
a=int(input()) #int type user 
inputb=float(input())#float type user 
inputc=bool(input())  #boolean type user input
print(a,'AND',b,'AND',c)   #print mutiple variable system
#<<<<<<<<<<<<<LIST_TYPE1# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
list=[] # declare an array
a=[0]*5 # define 5 as a null/0print('in list position 2=',a[2])


list=[int(i) for i in input().split()] #insert values into a list in a line
list.append(1) #insert last by appendinglist.append(3)
print(list.pop(1))

#<<<<<<<<<<<<<LIST_TYPE2>>>>>>>>>>>>>>>>>squar = []
for x in range(1, 11):
    squar.append(x++2)

print(squar)

squer = [x**2 for x in range(1, 11)]
print(squar)


finishers = ['jitun', 'pious', 'joy', 'ankit']
print(finishers)

first_two = finishers[:2]
print(first_two)

#<<<<<<<<<<<<<<<<<<<LIST_TYPE3>>>>>>>>>>>>>>>>>new = ['jitun', 'pious', 'joy', 'ankit']
print(new)

Copy_new=new[:]
print("<<<<<<<<<<<<<<Copy the hole list>>>>>>>>>>>>>>>>>>>>>>..\n")
print(Copy_new)
first_two = new[:2]
print("copy first 2 varriable>>>>>>>>>\n")
print(first_two)

#<<<<<<<<<<<<<<<<<<<<<LIST_TYPE4>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
list = {'!1st number': 12, '2nd number': 13}
for name, number in list.items():
    print(name + ' loves ' + str(number))

# <<<<<<<<<<<<<<<<<<<<<LIST_TYPE5>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
a = [9, 4, 6, 7, 5, 1, 3, 2]

print(max(a))# max funtionprint(min(a)) # min functionprint(sum(a)) #sum function

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>LOOP>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>a=3while a:
    print('jitun mohajan')
    a-=1
for x in list:
    print(x)
#>>>>>>>>>>>>>>>>>>>>>>>>>
#how to find ascii value
x='A'y=ord(x) # find ascii valueprint(y)


name=[] #create an array but according to phyton its called 
listname=["joy","pious","ankit","jitun"]
print(name[1]) #print the array[1] name

#<<<<<<<<<<<<<<<CREATE_FUNCTION>>>>>>>>>>>>>>>>>>>
def main(): #create function>>>>>>>>>>    
	a=12    
	b=13    
	print("sum of ",a," and ",b,">>",a+b)
main() #call function >>>>>>>


#<<<<<<<<<<<<<<<<<<FUNCTION 2>>>>>>>>>>>>>>>>

def add_numbers(x,y,z): #create function    
	return x+y+z
sum = add_numbers(3,5,7) #call functionprint(sum)
