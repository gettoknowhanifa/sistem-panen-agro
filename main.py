# Sistem Pencatatan Hasil Panen Agroindustri
# Terdiri dari fungsi input, perhitungan, dan laporan.


def input_data_panen():
    komoditas = input("Masukkan nama komoditas (contoh: Kopi Arabika): ")
    berat = float(input("Masukkan berat panen (kg): "))
    return komoditas, berat
    fitur-input

def hitung_pendapatan(berat_kg, harga_per_kg=5000):
    total = berat_kg * harga_per_kg
    return total

def cetak_laporan(komoditas, berat, total_pendapatan):
    print("\n" + "="*40)
    print("      STRUK HASIL PANEN AGRO")
    print("="*40)
    print(f"Komoditas     : {komoditas}")
    print(f"Berat         : {berat} kg")
    print(f"Total Estimasi: Rp {total_pendapatan:,.0f}")
    print("="*40)


# --- BLOK EKSEKUSI PROGRAM UTAMA ---
if __name__ == "__main__":
    print("Selamat datang di Sistem Pencatatan Panen Agroindustri!")
    komoditas_input, berat_input = input_data_panen()
    pendapatan = hitung_pendapatan(berat_input)
    cetak_laporan(komoditas_input, berat_input, pendapatan)


