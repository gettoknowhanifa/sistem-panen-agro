# Program Penghitung Total Hasil Panen

def hitung_total_panen(panen):
    return sum(panen)


def hitung_diskon(total_harga, persentase_diskon):
    diskon = total_harga * persentase_diskon / 100
    return total_harga - diskon


data_panen = [10, 15, 12, 20]

total = hitung_total_panen(data_panen)

harga = 100000
harga_setelah_diskon = hitung_diskon(harga, 10)

print("Data hasil panen:", data_panen)
print("Total hasil panen:", total, "kg")
print("Harga awal:", harga)
print("Harga setelah diskon:", harga_setelah_diskon)
