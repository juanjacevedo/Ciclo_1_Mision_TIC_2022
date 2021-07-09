'''
Modele mediante una funci ́on matem ́atica y dise ̃ne un programa
recursivo sin cadenas, tuplas o listas que invierta la cifras de un
n ́umero n dado. Por ejemplo, inversa(654321) = 123456.
'''

'''
def reverse(num):
    reverse=0
    bandera = True
    while bandera: 
        reverse=reverse*10+num%10
        num=num//10
        if num == 0: bandera = False
    return reverse
print (reverse(123456)) 
'''

def reverse(num, rever=0):
    if num==0:
        return rever
    else:
        return reverse(num//10, rever*10 + num%10)

print(reverse(123456))