def hitung_gaji(nama, jabatan, status_perkawinan):
    if jabatan == "Design" or jabatan == "Resource":
        gaji_pokok = 5000000
    elif jabatan == "Programmer":
        gaji_pokok = 10000000
    else:
        print("Jabatan tidak valid")
        return

    if status_perkawinan == "Y":
        tunjangan_keluarga = gaji_pokok*0.2
    else:
        tunjangan_keluarga = 0

    gaji_kotor = gaji_pokok + tunjangan_keluarga
    pajak = gaji_kotor*0.1
    total_pendapatan = gaji_kotor - pajak

    print("Nama Karyawan:", nama)
    print("Jabatan:", jabatan)
    print(f"Gaji Pokok: Rp{gaji_pokok:,}")
    if status_perkawinan == "Y":
        print(f"Tunjangan Keluarga: Rp{tunjangan_keluarga:,}")
    print(f"Gaji Kotor: Rp{gaji_kotor:,}")
    print(f"Pajak: Rp{pajak:,}")
    print(f"Total Pendapatan setelah pajak: Rp{total_pendapatan:,}")

print("="*50)
nama_karyawan = input("Masukkan nama karyawan: ").capitalize()
jabatan_karyawan = input("Masukkan jabatan karyawan (Design/Programmer/Resource): ").capitalize()
status_perkawinan = input("Masukkan status perkawinan (Y/T): ").capitalize()
print("="*50)
hitung_gaji(nama_karyawan, jabatan_karyawan, status_perkawinan)
