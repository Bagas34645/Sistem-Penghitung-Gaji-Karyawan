def hitung_gaji(jabatan, status_perkawinan):
    # Aturan gaji pokok dan tunjangan
    skala_gaji = {"Design": 5000000, "Programmer": 10000000, "Resource": 5000000}
    gaji_pokok = skala_gaji.get(jabatan, 0)
    tunjangan_keluarga = 0.2 * gaji_pokok if status_perkawinan == "Y" else 0

    # Menghitung gaji kotor dan pajak
    gaji_kotor = gaji_pokok + tunjangan_keluarga
    pajak = 0.1 * gaji_kotor

    # Menghitung total pendapatan
    total_pendapatan = gaji_kotor - pajak
    return {
        "gaji_pokok": gaji_pokok,
        "tunjangan_keluarga": tunjangan_keluarga,
        "gaji_kotor": gaji_kotor,
        "pajak": pajak,
        "total_pendapatan": total_pendapatan
    }

nama = input("👤 Masukkan nama karyawan: ").capitalize()
jabatan = input("💼 Masukkan jabatan karyawan (Design/Programmer/Resource): ").capitalize()
status_perkawinan = input("💍 Masukkan status perkawinan (Y/T): ").capitalize()

if jabatan not in ["Design", "Programmer", "Resource"]:
    print("⚠️ Jabatan tidak dikenal.")
else:
    hasil_gaji = hitung_gaji(jabatan, status_perkawinan)

    # Menampilkan hasil dalam bentuk tabel yang lebih rapi
    print("\n📋" + "="*7 +"Rincian Gaji Karyawan" + "="*7 + "📋")
    print(f"{'Keterangan':<20} | {'Jumlah':>15}")
    print("-" * 38)
    print(f"{'Nama Karyawan':<20} | {nama:>15}")
    print(f"{'Jabatan':<20} | {jabatan:>15}")
    print(f"{'Gaji Pokok':<20} | {'Rp ' + format(hasil_gaji['gaji_pokok'], ',.2f'):>15}")
    if hasil_gaji["tunjangan_keluarga"] > 0:
        print(f"{'Tunjangan Keluarga':<20} | {'Rp ' + format(hasil_gaji['tunjangan_keluarga'], ',.2f'):>15}")
    print(f"{'Gaji Kotor':<20} | {'Rp ' + format(hasil_gaji['gaji_kotor'], ',.2f'):>15}")
    print(f"{'Pajak':<20} | {'Rp ' + format(hasil_gaji['pajak'], ',.2f'):>15}")
    print(f"{'Total Pendapatan':<20} | {'Rp ' + format(hasil_gaji['total_pendapatan'], ',.2f'):>15}")
    print("=" * 38)
    print("Terima kasih telah menggunakan layanan kami 🙏")
    print("=" * 38)

