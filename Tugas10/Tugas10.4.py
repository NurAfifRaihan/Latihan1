

text = "Nurul Fikri"
vocal =['a','i','u','e','o']

def hanyaKonsonan(kata):
    for huruf in vocal:
        kata = kata.replace(huruf,"")
    print(kata)

hanyaKonsonan(text)