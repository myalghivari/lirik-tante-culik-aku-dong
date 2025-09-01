import sys
import time


def jalanin_lirik():
    # Ubah lirik lagu dan delay hurufnya sesuai yang kalian mau
    lirik = [
        ("Dunia pasti ada akhirnya...", 0.10),
        ("Bintang-bintang pun ada umurnya", 0.10),
        ("Maka tenang saja", 0.10),
        ("kita di sini berdua...", 0.15),
        ("Nikmati sementara yang ada...", 0.09),

    ]

    # Ubah delay dari setiap baris lagu (sesuaikan jumlah)
    delay = [2.8, 2.5, 0.5, 4.3, 3,0]
     # Ubah judul lagu
    print("\n== BERGEMA SAMPAI SELAMANYA :) ==")
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
    # Ganti nama pembuat
    print("===AL GHIVARI===")


jalanin_lirik()