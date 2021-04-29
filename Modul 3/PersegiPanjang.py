class PersegiPanjang :

    # Constructor
    def __init__(self, p, l):
        self.panjang = p
        self.lebar = l

# Encapsulation
    # Setter
    def ubahPanjang(self, p):
        self.panjang = p

    def ubahLebar(self, l):
        self.lebar = l
# End Encapsulation

    def hitungLuas(self):
        return self.panjang * self.lebar

    def hitungKeliling(self):
        return  2 * (self.panjang + self.lebar)

    def cetakLuas(self):
        print('Luas Persegi Panjang = %.2f' % self.hitungLuas())

    def cetakKeliling(self):
        print('Keliling Persegi Panjang = %.2f' % self.hitungKeliling())

objekPP = PersegiPanjang(12, 9)
print(objekPP.panjang)
print(objekPP.lebar)
objekPP.cetakLuas()
objekPP.cetakKeliling()