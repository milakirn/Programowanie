#czwarte
tup = ('Witam','wszystkich','na','moim','projekcie','Python')
a = 'Python'

if a in tup:
    print(tup.index(a))

tup2 = ('Witam','wszystkich','na','moim','projekcie','Python','.', 'Jak','ktoś','chce - ','może',
        'sobie','poszukać','kurs','Python','dla','rozwoju','osobistego')
if a in tup2:
    print(tup2.index(a))
    print(tup2.count(a))
#czwarte