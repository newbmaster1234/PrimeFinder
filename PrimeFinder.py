from multiprocessing.sharedctypes import Value
print('\n' * 2)
print('Welcome to PrimeFinder! It will find prime and composite numbers.\n It will state the numbers from 1 to what ever you want!')
ans = int(input("\nwhat number do you want it to stop?\n>"))
if ans <= 2:
    raise ValueError("You can\'t put 2 or lower!")
print('\n1 is a prime number')
print('2 is a prime number')
print('3 is a prime number')
a = 3
d, e = 0, 3
for c in range(1, ans-2):
    a = a + 1
    for b in range(2, a):
        if a %b == 0:
            print(a, "is is a composite number.", b, "x", a//b, "makes", a, end=".\n") 
            d = d + 1
            break
    else:
        print(a, "is is a prime numnber.")
        e = e + 1
print('\nThere are', d, 'composites and', e, 'primes\n')
print(e/(d+e)*100, "percent of numbers are prime.\n")
