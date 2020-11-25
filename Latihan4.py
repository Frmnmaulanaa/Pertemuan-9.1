nilai = [2,6,8,10,12]
print ("-------------------------------")
print ("Nilai :",nilai)
print ("Nilai ke 3 :",nilai [2])
print ("Nilai ke 2 - ke 4 :", nilai [1:4])
print ("Nilai terakhir :", nilai [-1])
print ("------------------------------")
#########################################
A = [2,6,8,10,12]
print ("--------------------------")
print ("Nilai :", A)
A [3] = 99
print ("Ubah nilai ke 4 :", A)
A [3:4] = [24, 25]
print ("Ubah nilai ke 4 - terakhir :", A)
print ("--------------------------")
########################################
list = nilai [0:2] + A
print ("list 2:", list)
list = nilai [0:2] + A
list.extend(["aku","kamu","kita"])
print ("list 2 + string :", list)
list = nilai [0:2] + A
list.extend([5,4,3])
print ("list 2 + nilai :", list)
gabung = nilai + list
list.extend(list)
print ("gabungan :", gabung)

