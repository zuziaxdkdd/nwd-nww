def nwd(a,b):
    lista = [a,b]
    wieksza = max(lista)
    mniejsza = min(lista)
    reszta = 1
    while reszta != 0:
        reszta = wieksza % mniejsza
        wieksza = mniejsza
        mniejsza = reszta
    return wieksza


print(nwd(173,54))




def nww(a,b):
    return (a * b)/nwd(a,b)

print(nww(173,54))
