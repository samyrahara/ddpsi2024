class Animal :
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def cetak(self):
        print("nama \t\t\t: ", self.nama,
              "\nmakanan  \t\t: ", self.makanan,
              "\nhidup \t\t\t:", self.hidup,
              "\nberkembang_biak\t\t: ", self.berkembang_biak,
            "\n------------------------")

object = Animal("kelinci", "rumput", "darat", "melahirkan")
object.cetak()

object = Animal("harimau", "daging", "darat", "melahirkan")
object.cetak() 
   