#Function defination
def myfriends(name="ajay"):                       #name is formal argument
    print(f'hello {name}, how are you')
    print("hello  "+name+", how are you")

    #function calling
myfriends('dipesh')                        #name is actual argument

#default argument

myfriends()                                #name is default argument

def myfriends2(*std):                         #function defination
    print("hello "+std[0])
    
myfriends2("sajid","deepak","rajesh")         #name is actual argument

def multiplicationnomber(x,y):            

     return  x * y                          #a function is return by value

answer = multiplicationnomber(50,30)      

print(answer)
print(f"the result is  {answer} ")

