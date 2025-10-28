age = int(input("masukkan umur: "))
gender = input("gender: ")

if age <= 1:
    print("bayi")
elif age >= 1 and age < 13:
    print("di bawah umur")
    if gender == "f":
        print("perempuan")
    else:
        print("laki-laki")
elif age < 20:
    print("remaja")
else:
    print("dewasa")