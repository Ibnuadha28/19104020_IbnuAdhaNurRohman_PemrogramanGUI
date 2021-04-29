class persegiPanjang:

    # Atribut Statis
    counter = 0
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
        print('Luas persegi Panjang = %.2f' % self.hitungLuas())

    def cetakKeliling(self):
        print('Keliling persegi Panjang = %.2f' % self.hitungKeliling())

objekpp1 = persegiPanjang(10, 8)
objekpp2 = persegiPanjang(9, 8)
objekpp3 = persegiPanjang(8, 8)

objekpp1.cetakLuas()
objekpp1.cetakKeliling()
objekpp1.counter = 10

print(objekpp1.counter)
print(objekpp2.counter)
print(objekpp3.counter)