def jumlah(*numbers) :
    hasil = 0 
    for i in numbers :
        hasil += i
    return hasil

def kurangi(*numbers) :
    hasil = 0 
    for i in numbers :
        hasil += i
    return hasil

def kali(*numbers) :
    hasil = 1
    for i in numbers :
        hasil += i
    return hasil

def bagi(*numbers) : 
    yg_bagi = numbers[0]
    pembagi = numbers[1:]
    for i in pembagi :
        yg_bagi /= i
    return yg_bagi

print 
print(bagi(1000,2,2))