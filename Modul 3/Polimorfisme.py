from abc import ABCMeta, abstractmethod
class DuaDimensi(metaclass=ABCMeta):
    @abstractmethod
    def luas(self):
        pass

class SegiEmpat(DuaDimensi):
    def __init__(self, p, l):
        self.panjang = p
        self.lebar = l

    def luas(self):
        return self.panjang * self.lebar

class Segitiga(DuaDimensi):
    def __init__(self, a, t):
        self.alas = a
        self.tinggi = t

    def luas(self):
        return (self.alas * self.tinggi) / 2

class Lingkaran(DuaDimensi):
    def __init__(self, r):
        self.jari2 = r

    def luas(self):
        import math
        return math.pi * (self.jari2 ** 2)

# membuat list kosong
mylist = []

# menambahkan objek segiEmpat ke dalam mylist
mylist.append(SegiEmpat(10, 8))

# menambahkan objek Segitiga ke dalam mylist
mylist.append(Segitiga(3, 5))

# menambahkan objek Lingkaran ke dalam mylist
mylist.append(Lingkaran(4))

# mengecek semua elemen mylist dan memanggil metode luas dari setiap objek yang ada di dalam mylist
for obj in mylist:
    if not issubclass(obj.__class__, DuaDimensi):
        raise TypeError('objek harus turunan dari Dua Dimensi')
    if isinstance(obj, SegiEmpat):
        print('Luas Segi Empat = ', end='')
    elif isinstance(obj, Segitiga):
        print('Luas Segitiga = ', end='')
    else:
        print('Luas Lingkaran = ', end='')
    print(obj.luas())
