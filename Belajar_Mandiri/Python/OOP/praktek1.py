class Mahasiswa:
    
    def __init__(self, nama, energi = 100):
        self.nama = nama
        self.energi = energi
        
    def belajar(self, belajar = 15):
        self.energi -= belajar
        print(f"sedang belajar OOP, energi berkurang 15 menjadi {self.energi}")
    
    def tidur(self, tidur = 20):
        self.energi += tidur
        print(f"sedang istirahat, energi bertambah 20 menjadi {self.energi}")
        
    def info(self):
        print(f"nama saya adalah {self.nama}, energi saya tersisa {self.energi}")
        
kegiatan = Mahasiswa("Abiyyu")

kegiatan.belajar()
kegiatan.belajar()
kegiatan.tidur()
kegiatan.info()