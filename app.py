import sys
import time


def jalanin_lirik():
    # Ubah lirik lagu dan delay hurufnya sesuai yang kalian mau
    lirik = [
        ("Sudah Terbiasa Tejadi Tante", 0.10),
        ("Teman Datang Ketika Lagi Butuh Saja", 0.08),
        ("Coba Kalau Lagi Susah", 0.08),
        ("Mereka Semua Menghilang...", 0.09),
        ("Apakah Spek Standar Seperti Ini Yang Para Pemirsa Inginkan?", 0.03),
        ("Tante...", 0.07),
        ("Tante...", 0.07),
        ("Tante...", 0.07),

    ]

    # Ubah delay dari setiap baris lagu (sesuaikan jumlah)
    delay = [1.0, 1.0, 1.0, 0.7, 1.0, 2.8, 2.5, 4.6]
    # Ubah judul lagu
    print("\n== TANTE CULIK AKU DONG ==")
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
    # Ganti nama pembuat
    print("===GANTI NAMA===")


jalanin_lirik()