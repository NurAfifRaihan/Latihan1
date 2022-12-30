from Bank import *
#ciptakan object
raihan = Bank("001","Cortois", 500000000)
yanto = Bank('007','Marcello', 600000000)
yatni = Bank('010','Pepe', 9000000000)
asep = Bank('011','Benzema', 1200000000)
#yang pake member class
raihan.nabung(100000000)
yanto.nabung(200000000)
yatni.tarik(250000000)
asep.tarik(780000000)
print(Bank.BANK,
    "\n============================")

raihan.cetak()
yanto.cetak()
yatni.cetak()
asep.cetak()
print('Jumlah Nasabah: %i orang' %Bank.jmlNasabah)