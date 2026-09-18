# Program Penghitung Total Hasil Panen

def hitung_total_panen(panen):
    return sum(panen)


data_panen = [10, 15, 12, 20]

total = hitung_total_panen(data_panen)

print("Data hasil panen:", data_panen)
print("Total hasil panen:", total, "kg")
