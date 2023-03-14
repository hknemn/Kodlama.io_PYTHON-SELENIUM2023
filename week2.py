#odev1

students = ["Hakan Unal", "Esra Deniz"]

def add(fullName):
    students.append(fullName)

def remove(fullName):
    students.remove(fullName)

def printStudents():
    for student in students:
        print(student)
  
def getStudentId(fullName):
    i = 0
    while i<len(students):
        if students[i] == fullName:
            return i
        i += 1
    return "Ogrenci bulunamadi!"

add(input("Eklemek istediginiz ogrencinin adi soyadi: "))
print("Kayit eklendi")
printStudents()

remove(input("Silmek istediginiz ogrencinin adi soyadi: "))
print("Kayit silindi")
printStudents()

print("Ogrenci numarasi: " + str(getStudentId(input("Ogrenci numarasini ogrenmek istediginiz ogrencinin adi soyadi: "))))

eklenecekOgrenciSayisi = int(input("Kac ogrenci eklemek istiyorsunuz: "))
for i in range(eklenecekOgrenciSayisi):
    add(input("Eklemek istediginiz ogrencinin adi soyadi: "))
    print("Kayit eklendi")
printStudents()

silinecekOgrenciSayisi = int(input("Kac ogrenci silmek istiyorsunuz: "))
i=0
while(i<silinecekOgrenciSayisi):
    remove(input("Silmek istediginiz ogrencinin adi soyadi: "))
    print("Kayit silindi")
    i += 1
printStudents()

