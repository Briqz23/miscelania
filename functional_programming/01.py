i =  map(lambda x:x**3, range(5))
print(list(i))

j = map(lambda x:x>3, range(10))
print(list(j))

ingredientes1 ,estado = ['tomate', 'ovo', 'carne'], ['fresco','cozido', 'mal-passada']

k = map(lambda x,y, z: x+y+z, ingredientes1, [' ']*len(estado), estado)
print(list(k))