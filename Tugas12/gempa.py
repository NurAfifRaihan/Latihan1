class Gempa:
    def __init__(self, lokasi, skala) -> None:
        self.lokasi = lokasi
        self.skala = skala

        if skala < 2:
            dampak = "Tidak terasa"
        elif skala >= 2 and skala <= 4:
            dampak = "Bangunan retak-retak"
        elif skala >= 4 and skala <= 6:
            dampak = "Bangunan roboh"
        elif skala >= 6:
            dampak = "Bangunan roboh dan berpotensi tsunami"
        

        self.dampak = dampak

    def info(self):
        print(self.lokasi)
        print(self.skala)
        print(self.dampak)