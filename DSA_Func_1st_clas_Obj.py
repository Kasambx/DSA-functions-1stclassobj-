# Functions as first class objects

def greeting(lang):
    if lang == 'eng':
        return 'Hello World'
    if lang == 'swa':
        return 'Mambo Kasamba'
    else : return 'Are you an alien'

print(greeting)

# we can include them in other objects, such as lists
l = [greeting('eng'), greeting('swa'), greeting('ger')]
print(l[0])

# functions can also be used as arguments for other functions 
def cally(y):
    lang = 'swa'
    return (y(lang))

cally(greeting)
print(cally(greeting))

#High order functions
# using map()
lst = [1,2,3,4,]

list(map((lambda x: x**3), lst))
print(list(map((lambda x: x**3), lst)))

#High order functions
# using filter()
list(filter((lambda x: x<3), lst))
print(list(filter((lambda x: x<3), lst)))

#creating my very own high order function
#sorting words in a string & printing them in a list in order of no of characters
words = str.split('Kasamba will be a great opensourcer')
sorted(words, key=len)
print(sorted(words, key=len))

#creating my very own high order function
#case sensitive sorting
k = ['W','D','C','a','c']
k.sort(key=str.lower)
print(k)

# Recursive functions

