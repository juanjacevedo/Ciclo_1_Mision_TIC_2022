x = 1
'''
while x <= 10:
    print(x)
    x += 1
print("Finalizado!!!")
'''
'''
while x <= 10:  # false

  if (x <= 10): # false
  print(x)
    x -= 1               <-------- No ejecutar, es un ciclo infinito
  else:
    break

print("Finalizado!!!")
'''
'''while True:
    if (x <= 10):
        print(x)
        x += 1
    else:
        break
print("Finalizado")'''

'''i = 2
j = 25

while i < j:
    print(i,j, sep = ", ")
    i *= 2
    j += 10

print("The end.")
print(i,j, sep = ",")'''
