# decorator means a feature that you can add additional feature to your funcions without rewriting the whole code
# Reference: STEAM 教育學習網, FreeCodeCamp

# if it is hard to understand, maybe you can try debugging tools, it's pretty useful if you wanna know the overall code flow
# how decorators work 
# def laugh(func): # first function: put function here
#     print("Laughing-- ")
#     return func # recrusive: call another func inside of a function

# def cry(): # second function 
#     print("and sobbing..")

# shout_n_cry = laugh(cry) # laugh func decos cry func
# shout_n_cry() # run the func you set
# Laughing-- 
# and sobbing..
# OR ----------------------
# def laugh(func):
#     print("I'm laughing! ")
#     return func
# # use syntactic sugar '@', add on top of the function before 'cry'
# @laugh
# def cry():
#     print("and sobbing...")

#cry() # cleaner code and same effect, no need more complex defines
# I'm laughing! 
# and sobbing...
# OR ----------------------
# Multiple decorators
def laugh(func):
    print("I'm laughing! ")
    return func


def cry(func):
    print("and sobbing...")
    return func

def tired(func):
    print("and feeling so tired...")
    return func

def sad(func):
    print("and so frustrated...")
    return func

@sad # fourth and so on...
@tired # thrid
@cry # second
@laugh # first: decos from buttom to top ^
def end():
    print("This is the end")

end() # result 
