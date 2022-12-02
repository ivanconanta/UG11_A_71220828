#1.A. Test case 1
print("===== Program Manipulasi String =====")
print("Pilihan Menu:")
print("1. Hitung kata")
print("2. Ubah kata")
a = int(input("Pilihan anda: "))
b = input("Masukkan sebuah kalimat/kata: ")
def hitung_kata():
    c = input("Masukkan kata yang ingin di hitung: ")
    x.count(c)
    print('terdapat sebanyak',x,'kata',c,'di dalam kalimat')
def ubah_kata():
    c = input("Masukkan sebuah kalimat/kata: ")
    d = input("Masukkan kata yang ingin di ubah: ")
    e = input("Masukkan kata pengganti: ")
    print(c.replace(d,e))
print("String berhasil diubah menjadi :") 

if a=='1':
    hitung_kata()
elif a=='2':
    ubah_kata()
else:
    print("Pilihan yang anda input tidak terdaftar di daftar pilihan")
   