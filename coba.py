#masukan
a = input().split()

#copy isi list a ke list b sekalligus casting setiap elemen di a menjadi int
b = [int(i) for i in a]

#mengurutkan isi list
b = sorted(b);

print(b);

print(b[1])
print(b[2])

print(b[1]+ b[2])

