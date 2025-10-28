b = {
    "nama" : ["d", "e", "f"],
    "usia" : [31, 15, 27],
    "alamat" : ["medan", "bandung", "surabaya"]
}

def ekstrak_data(data):
    for i, j in data.items():
        print(i)
        for k in j:
            print("- {} (tipe data = {})".format(k, type(k)))

ekstrak_data(data = b)