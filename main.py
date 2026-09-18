# Sistem Pencatatan Hasil Panen Agroindustri
# Terdiri dari fungsi input, perhitungan, dan laporan.

def input_data_panen():
    komoditas = input("Masukkan nama komoditas (contoh: Kopi Arabika): ")
    berat = float(input("Masukkan berat panen (kg): "))
    return komoditas, berat
