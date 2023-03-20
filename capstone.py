# Haryo Dewantoro
# Aplikasi Perpustakaan

import math

daftar_buku_keuangan = [
    {'id':'01', 'judul':'Rich Dad Poor Dad', 'tahun':1997, 'penulis':'Robert T. Kiyosaki', 'stok':5},
    {'id':'02', 'judul':'Psychology of Money', 'tahun':2020, 'penulis':'Morgan Housel  ', 'stok':4},
    {'id':'03', 'judul':'cashflow quadrant', 'tahun':1998, 'penulis':'Robert T. Kiyosaki', 'stok':10},
    {'id':'04', 'judul':'Think and Grow Rich', 'tahun':1937, 'penulis':'Georde Goodman', 'stok':2}
]

salah_input = 'Tidak Terjadi Apapun'

# ================================================================================================
# untuk menu 1
def menampilkan_semua_buku():
    print("\tDaftar Buku")
    print("ID\t| Judul \t\t\t| Tahun\t| Penulis\t\t Stok\t")
    for idx in range(len(daftar_buku_keuangan)):
        print(f"{daftar_buku_keuangan[idx]['id']} \t| {daftar_buku_keuangan[idx]['judul']} \t\t| {daftar_buku_keuangan[idx]['tahun']}\t| {daftar_buku_keuangan[idx]['penulis']}\t {daftar_buku_keuangan[idx]['stok']}")
# ================================================================================================
# untuk menu 2
def bukuTambahan():
    print("ID\t| Judul \t\t\t\t| Tahun\t| Penulis\t\t Stok\t")
    for buku in daftar_buku_keuangan:
        print(f"{buku['id']} \t| {buku['judul']} \t\t| {buku['tahun']}\t| {buku['penulis']}\t {buku['stok']}")
        return True
    return False
# ================================================================================================
# menu utama bukan menu pilihan
daftar_pilihan = ('''
    Daftar Pilihan :
    1. Menampilkan Daftar Buku
    2. Menambah Buku
    3. Mengubah Data Buku
    4. Menghapus Buku
    5. Keluar Program\n''')

# -----------------------------------------------------------------------------------
# untuk menu 1
daftar_menu_baca_data = ('''
    Daftar Halaman :
    1. Tampilkan Semua Buku
    2. Temukan Buku Melalui ID
    3. Kembali
''')

# -----------------------------------------------------------------------------------
# untuk menu 3
daftar_edit_kolom = ('''
    Perbaharui Kolom yang Tersedia :
    1. ID
    2. Judul
    3. Tahun
    4. Penulis
    5. Stok
''')

# -----------------------------------------------------------------------------------
# untuk menu 1
def buku_dari_id(daftar_buku_keuangan, primary_key):
    for buku in daftar_buku_keuangan:
        if buku['id'] == primary_key:
            print(f"\nID \t Judul \t\t\t\tTahun \t Penulis \t\t Stok")
            print(f"{buku['id']} \t {buku['judul']}\t\t{buku['tahun']}\t {buku['penulis']} \t {buku['stok']} \n")
    #         return True
    # return False

# -----------------------------------------------------------------------------------
# untuk menu 1
def menampilkan_salahsatu_id():
    
    primary_key = (input("Masukan ID Buku : "))

    list_id = []

    for buku in daftar_buku_keuangan:
        list_id.append(buku['id'])

    if primary_key in list_id:
        for buku in daftar_buku_keuangan:
            if buku['id'] == primary_key:
                buku_dari_id(daftar_buku_keuangan, primary_key)
            

    else:
        if primary_key != primary_key.isdigit:
            print('\nBuku tidak ditemukan, Pastikan ID benar')
    menu_baca_data()

# -----------------------------------------------------------------------------------
# untuk menu 1
def menu_baca_data():
    while True:
        print(daftar_menu_baca_data)
        user_masukan_menu = input("Masukan angka (1-3) diantara daftar diatas : ")
        print()
        if user_masukan_menu == '1':
            menampilkan_semua_buku()
            menu_baca_data()

        elif user_masukan_menu == '2':
            menampilkan_semua_buku()
            menampilkan_salahsatu_id()  
        elif user_masukan_menu == '3':
            menu_utama()
        else:
            print()
            print('Tidak Ada Data')
            menu_baca_data()
        break

# ================================================================================================
# untuk menu 2
daftar_menu_menambah_data = ('''
    Halaman Tambah Buku :
    1. Tambah Buku Baru
    2. Kembali
''')

# -----------------------------------------------------------------------------------
# untuk menu 2
def menu_menambah_data():
    print(daftar_menu_menambah_data)
    user_masukan_menu = input("Masukan data Buku, tolong pilih diantara (1/2) : ")
    if user_masukan_menu == '1':
        print()
        menambah_data_buku()

    elif user_masukan_menu == '2':
        menu_utama()
    else:
        print
        print("Tolong masukan angka yang tersedia : ")
        menu_menambah_data()

# -----------------------------------------------------------------------------------
# untuk menu 2
def menambah_data_buku():
    new_primary_key = input("Masukan ID baru : ")
    while True:
        if new_primary_key.isdigit():

            list_id = []

            for buku in daftar_buku_keuangan:
                list_id.append(buku['id'])

            if new_primary_key in list_id:
                print('\nID Buku tersebut sudah tersedia, tolong masukan ID baru \n')
                menambah_data_buku()

            else:
                judul = input("Masukan Judul Buku : ")
                panjang_karakter = len(judul)
                if  panjang_karakter > 18:
                    print(f'\nKarakter Maksimal 18, Karakter Kalimat Kamu {panjang_karakter}')
                    menu_menambah_data()
                elif panjang_karakter <= 18:
                    hitungan = panjang_karakter - 18
                    pembulatan = math.fabs(hitungan)
                    spasi = ' ' * int(pembulatan)
                    hasil_judul = judul + spasi
                tahun = input("Masukan Tahun Buku : ")
                if len(tahun) > 4:
                    print(f'\nKarakter Maksimal 4, Karakter Kalimat Kamu {len(tahun)}')
                    menu_menambah_data()
                penulis = input("Masukan Penulis Buku : ")
                if len(penulis) > 18:
                    print(f'\nKarakter Maksimal 18, Karakter Kalimat Kamu {panjang_karakter}')
                    menu_menambah_data()
                elif len(penulis) < 18:
                    hitungan = len(penulis) - 18
                    pembulatan = math.fabs(hitungan)
                    spasi = ' ' * int(pembulatan)
                    hasil_penulis = penulis + spasi
                stok = input("Masukan Jumlah Buku : ")
                print()
                buku_baru = (f'ID : {new_primary_key} | Judul : {hasil_judul.title()} | Tahun : {tahun} | Penulis : {hasil_penulis.title()} | Stok : {stok}')
                print(buku_baru)
                buku_baru = {'id':new_primary_key, 'judul':hasil_judul.title(), 'tahun': tahun, 'penulis': hasil_penulis.title(), 'stok':stok}

                # --------------------------------------------------------------------------------
                user_masukan_menu = input("\nYakin ingin menambahkan(Ya/Tidak) : ")
                if user_masukan_menu.lower() == 'ya':
                    daftar_buku_keuangan.append(buku_baru)
                    print()
                    print("Data Tersimpan")
                    menu_menambah_data()
                elif user_masukan_menu.lower() == 'tidak':
                    menu_menambah_data()
            break
        else:
            print('\nPastikan Kamu memasukan Angka!\n')
            new_primary_key = input("Masukan ID baru : ")
            
# ================================================================================================
# untuk menu 3
daftar_menu_ubah_data = ('''
    Halaman Edit Buku : 
    1. Edit Informasi Buku
    2. Kembali

''')

# -----------------------------------------------------------------------------------
# untuk menu 3
def menu_ubah_data():
    
        print(daftar_menu_ubah_data)
        user_masukan_menu = input("Kamu memasukin Halaman Edit Buku, Tolong masukan angka diantara (1/2) : ")
            
        if user_masukan_menu == "1":
            mengubah_data_buku()
        elif user_masukan_menu == "2":
            menu_utama()
        else:
            print("\nPilihan Nomor Tidak Sesuai")
            menu_ubah_data()

# -----------------------------------------------------------------------------------
# untuk menu 3
def mengubah_data_buku():
    
    menampilkan_semua_buku()
    primary_key = input("\nMasukan ID Buku yang ingin Kamu Perbaharui : ")
    print()
        

    list_id = []

    for buku in daftar_buku_keuangan:
        list_id.append(buku['id'])

    for idx,buku in enumerate(daftar_buku_keuangan):
            
        if daftar_buku_keuangan[idx]['id'] == primary_key:
            print(buku)
            validasi = input("\nKamu yakin ingin melanjutkan?(Ya/Tidak): ")
            if validasi.lower() == 'tidak':
                print("\nPembaharuan dibatalkan")
                menu_ubah_data()
            elif validasi.lower() == 'ya':
                print(daftar_edit_kolom)
                pilihan_mengubah_buku = input(f"Pilih data kategori yang ingin Kamu ubah, (diantara 1 sampai 5) : ")
                # -------------------------------------------------------------------------
                if pilihan_mengubah_buku == '1':
                    buku_dari_id(daftar_buku_keuangan, primary_key)
                    new_primary_key = input("Masukan ID Baru : ")
                    if new_primary_key in list_id:
                        print('\nID Buku tersebut sudah tersedia, tolong masukan ID baru \n')
                        mengubah_data_buku()
                    
                    validasi_id = input("Kamu yakin ingin melanjutkan?(Ya/Tidak): ")
                    print()

                    if validasi_id.lower() == "ya":
                        for idx,baru in enumerate(daftar_buku_keuangan):
                            if primary_key == daftar_buku_keuangan[idx]['id']:
                                daftar_buku_keuangan[idx]['id'] = new_primary_key
                                print (baru)
                                print("\nData Telah Diperbaharui")
                                menu_ubah_data()
                    elif validasi_id.lower() == "tidak":
                        print("\nPembaharuan dibatalkan")
                        menu_ubah_data()
                    else:
                        print(salah_input)
                        menu_ubah_data()
                # -------------------------------------------------------------------------
                elif pilihan_mengubah_buku == '2':
                    buku_dari_id(daftar_buku_keuangan, primary_key)
                    data_judul = input("Masukan Judul Baru : ")
                    if len(data_judul) > 18:
                        print(f'\nKarakter Maksimal 18, Karakter Kalimat Kamu {len(data_judul)}')
                        menu_ubah_data()
                    elif len(data_judul) < 18:
                        hitungan = len(data_judul) - 18
                        pembulatan = math.fabs(hitungan)
                        spasi = ' ' * int(pembulatan)
                        hasil_judul = data_judul + spasi    
                    validasi_id = input("Kamu yakin ingin melanjutkan?(Ya/Tidak): ")
                    print()
                    if validasi_id.lower() == "ya":
                        for idx,baru in enumerate(daftar_buku_keuangan):
                            if primary_key == daftar_buku_keuangan[idx]['id']:
                                daftar_buku_keuangan[idx]['judul'] = hasil_judul.title()
                                print (baru)
                                print("\nData Telah Diperbaharui")
                                menu_ubah_data()
                    elif validasi_id.lower() == "tidak":
                        print("\nPembaharuan dibatalkan")
                        menu_ubah_data()
                    else:
                        print(salah_input)
                        menu_ubah_data()
                # -------------------------------------------------------------------------
                elif pilihan_mengubah_buku == '3':
                    buku_dari_id(daftar_buku_keuangan, primary_key)
                    data_tahun = input("Masukan Tahun Baru : ")
                    while True:
                        if data_tahun.isdigit():
                            if int(data_tahun) > 9999:
                                print(f'\nMaksimal 4 Angka')
                                menu_ubah_data()
                            elif int(data_tahun) < 9999:
                                validasi_id = input("Kamu yakin ingin melanjutkan?(Ya/Tidak): ")
                                print()
                            break
                        else :
                            print ("Data yang anda masukkan tidak valid")
                            data_tahun = input("Masukan Tahun Baru : ")

                    if validasi_id.lower() == "ya":
                        for idx,baru in enumerate(daftar_buku_keuangan):
                            if primary_key == daftar_buku_keuangan[idx]['id']:
                                daftar_buku_keuangan[idx]['tahun'] = int(data_tahun)
                                print (baru)
                                print("\nData Telah Diperbaharui")
                                menu_ubah_data()
                    elif validasi_id.lower() == "tidak":
                        print("\nPembaharuan dibatalkan")
                        menu_ubah_data()
                    else:
                        print(salah_input)
                        menu_ubah_data()
                # -------------------------------------------------------------------------
                elif pilihan_mengubah_buku == '4':
                    buku_dari_id(daftar_buku_keuangan, primary_key)
                    data_penulis = input("Masukan Penulis Baru : ")
                    if len(data_penulis) > 18:
                        print(f'Karakter Maksimal 18, Karakter Kalimat Kamu {len(data_penulis)}')
                        menu_ubah_data()
                    elif len(data_penulis) < 18:
                        hitungan = len(data_penulis) - 18
                        math_var = int(math.fabs(hitungan)) * ' '
                        hasil_penulis = data_penulis + math_var
                    validasi_id = input("Kamu yakin ingin melanjutkan?(Ya/Tidak): ")
                    print()
                    if validasi_id.lower() == "ya":
                        for idx,baru in enumerate(daftar_buku_keuangan):
                            if primary_key == daftar_buku_keuangan[idx]['id']:
                                daftar_buku_keuangan[idx]['penulis'] = hasil_penulis.title()
                                print (baru)
                                print("\nData Telah Diperbaharui")
                                menu_ubah_data()
                    elif validasi_id.lower() == "tidak":
                        print("\nPembaharuan dibatalkan")
                        menu_ubah_data()
                    else:
                        print(salah_input)
                        menu_ubah_data()
                # -------------------------------------------------------------------------
                elif pilihan_mengubah_buku == '5':
                    buku_dari_id(daftar_buku_keuangan, primary_key)
                    data_stok = input("Masukan Stok Baru : ")
                    while not data_stok.isdigit():
                        data_stok = input("Masukan Stok Baru : ")
                    data_stok = int(data_stok)

                    validasi_id = input("Kamu yakin ingin melanjutkan?(Ya/Tidak): ")
                    print()
                    if validasi_id.lower() == "ya":
                        for idx,baru in enumerate(daftar_buku_keuangan):
                            if primary_key == daftar_buku_keuangan[idx]['id']:
                                daftar_buku_keuangan[idx]['stok'] = data_stok
                                print (baru)
                                print("\nData Telah Diperbaharui")
                                menu_ubah_data()
                    elif validasi_id.lower() == "tidak":
                        print("\nPembaharuan dibatalkan")
                        menu_ubah_data()
                    else:
                        menu_ubah_data()
    print('Data yang anda cari tidak ada')
    menu_ubah_data()

# ================================================================================================
# untuk menu 4
daftar_menu_hapus_data = ('''
    Kamu Memasuki Halaman Hapus Buku :
    1. Menghapus Daftar Buku
    2. Kembali
''')

# -----------------------------------------------------------------------------------
# untuk menu 4
def menu_hapus_data():
    while True:
        print(daftar_menu_hapus_data)
        user_masukan_menu = input("\n Pilih angka diantara (1/2) : ")

        list_id = []

        if user_masukan_menu == "1":
            menampilkan_semua_buku()
            hapus_buku = input("\nTolong pilih Buku yang ingin Kamu Hapus, Masukan ID Buku : ")
            for buku in daftar_buku_keuangan:
                list_id.append(buku['id'])

            if hapus_buku in list_id:

                for barang in daftar_buku_keuangan.copy():
                    if barang.get('id') == hapus_buku:
                        verifikasi_hapus = input("Kamu yakin ingin melanjutkan?(Ya/Tidak): ")
                        if verifikasi_hapus.lower() == 'ya':
                            daftar_buku_keuangan.remove(barang)
                            print("\n Data Sudah Berhasil Dihapus")
                            break
                        elif verifikasi_hapus.lower() == 'tidak':
                            print("\n Data Tidak Berhasil Dihapus")
                            break
                print('\n')
                menu_hapus_data()
                break

            else:
                print("\n ID Buku tidak terdaftar, Pastikan masukan ID yang Benar")
                break
        
        elif user_masukan_menu == "2":
            break
        else:
            # continue
            menu_hapus_data()

# ================================================================================================

def menu_utama():
    print(f'''
        ------------------------------------------------------------------
            Selamat Datang di Aplikasi Perpustakaan Literasi Keuangan
        ------------------------------------------------------------------
        ''')
    print(daftar_pilihan)

    user_masukan_menu = input("Masukan angka diantara Daftar tersebut : ")
    print()

    if user_masukan_menu == "1":
        menu_baca_data()
    elif user_masukan_menu == "2":
        menu_menambah_data()
    elif user_masukan_menu == "3":
        menu_ubah_data()
    elif user_masukan_menu == "4":
        menu_hapus_data()
    elif user_masukan_menu == "5":
        print('Senang bisa membantu Kamu, Kritik Dan Saran Hub: 085773127388\n')
        global x
        x = False
    else:
        print('Pilihan yang anda masukan salah')

x = True
while x == True:
    menu_utama()