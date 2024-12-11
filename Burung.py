from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.bunyi = bunyi

    def cetak_burung(self):
        super().cetak()
        print("jenis \t\t\t: ", self.jenis,
            "\nbunyi \t\t\t: ", self.bunyi)
        
Hantu = Burung("hantu", "daging", "hutan tropis", "Bertelur", "Barn Owl", "hoo-hoo")
Hantu.cetak_burung()

