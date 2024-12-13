from Animal import *

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, corak):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.corak = corak

    def cetak_ikan(self):
        super().cetak()
        print("jenis \t\t\t: ", self.jenis,
            "\ncorak \t\t\t: ", self.corak,
            "\n------------------------")
        
    
        
Mujair = Ikan("mujair", "plankton", "sungai", "Bertelur", "Cichlidae", "kecoklatan")
Mujair.cetak_ikan()

Nila = Ikan("nila", "plankton", "sungai", "Bertelur", "Nila Merah ", "pink keemasan")
Nila.cetak_ikan()
