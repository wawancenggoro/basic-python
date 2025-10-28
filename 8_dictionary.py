a = {
    "nama" : ["a", "b", "c"],
    "usia" : [30, "76", 27],
    "alamat" : ["jakarta", "bandung", "bali"]
}

print(a.keys())
print(a.values())

for i, j in a.items():
    print(i)
    for k in j:
        print(f"- {k} (tipe data = {type(k)})")