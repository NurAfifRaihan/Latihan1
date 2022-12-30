class Hewan :

    def __init__(self, nama, makanan, hidup, berkembang_biak) :
        self.nama = nama
        self.makanan = makanan
        self.habitat = hidup
        self.cara = berkembang_biak

    def cek_bio(self): 
        print('\n===========================',
            '\nNama Hewan \t: ',self.nama,
            '\nMakanan \t: ',self.makanan,
            '\nHabitat \t: ',self.habitat,
            '\nBerkembang Biak\t: ',self.cara,
            '\n-----------------------------')

    
