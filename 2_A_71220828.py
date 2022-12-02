#2.A. Test case 1
kata = input("Masukkan kata:")
def left(kata):
    x=kata[2:5]
    return x
X=left(kata)
print("Huruf yang diambil pada kata", kata ,'adalah', X)

#2.B. Test case 2
kata = input("Masukkan kata:")
def left(kata):
    a=kata[0:3]
    return a
A=left(kata)
def left(kata):
    b=kata[5:8]
    return b
B=left(kata)
print("Huruf yang diambil pada kata", kata ,'adalah', A ,'dan', B)


