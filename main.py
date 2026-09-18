# Sistem Pencatatan Hasil Panen Agroindustri
# Terdiri dari fungsi input, perhitungan, dan laporan.

def cetak_laporan(komoditas, berat, total_pendapatan):
    print("\n" + "="*40)
    print("      STRUK HASIL PANEN AGRO")
    print("="*40)
    print(f"Komoditas     : {komoditas}")
    print(f"Berat         : {berat} kg")
    print(f"Total Estimasi: Rp {total_pendapatan:,.0f}")
    print("="*40)
