# Program Python OOP Nama-nama Buah
class Buah:
    def aromaSegar(self):
        print("Nama Buah")
        
    def jenis(self):
        print("Hampir semua buah dapat di makan, tapi ada juga beberapa yang tidak dapat di makan dan beracun")
        
class Apel(Buah):
    def jenis(self):
        print("Buah apel ini dapat di makan dan sangat bergizi")
        
class BuahBintaro(Buah):
    def jenis(self):
        print("Buah bintaro ini tidak dapat di makan dan beracun")
        
nama_buah = Buah()
nama_apel = Apel()
nama_buah_bintaro = BuahBintaro()

nama_buah.aromaSegar()
nama_buah.jenis()

nama_apel.aromaSegar()
nama_apel.jenis()

nama_buah_bintaro.aromaSegar()
nama_buah_bintaro.jenis()