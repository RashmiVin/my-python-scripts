#what would the code print:
def thing():
    print('Hello')
print('There')

#what would the code print:
def func(x):
    print(x)
func(10)
func(20)

#what would the code print:
def stuff():
    print('Hello')
    return
    print('World')
stuff()

#what would the code print:
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
print(greet('fr'), 'Michael')
#Will the below code get executed? No
if x == 5 :
    print('Is 5')
    print('Is Still 5')
    print('Third 5')
# what would the code print:
    x = 0
    if x < 2:
        print('Small')
    elif x < 10:
        print('Medium')
    else:
        print('LARGE')
    print('All done')
# what would the code print:
    if x < 2:
        print('Below 2')
    elif x >= 2:
        print('Two or more')
    else:
        print('Something else')
# what would the code print:
astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1


