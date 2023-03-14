# Haryo Dewantoro
# Aplikasi Perpustakaan

buku_keuangan = [
    {'id':'01', 'judul':'Rich Dad Poor Dad', 'tahun':1997, 'penulis':'Robert T. Kiyosaki', 'stok':5},
    {'id':'02', 'judul':'The Psychology of Money', 'tahun':2020, 'penulis':'Morgan Housel', 'stok':4},
    {'id':'03', 'judul':'Warren Buffett Wisdom', 'tahun':2013, 'penulis':'Lukas Setia Atmaja', 'stok':1},
    {'id':'04', 'judul':'Think and Grow Rich', 'tahun':1937, 'penulis':'Georde Goodman', 'stok':2}
]

# ================================================================================================
# untuk menu 1
def daftar_bukuKeuangan():
    print("\tDaftar Buku")
    print("ID\t| Judul \t\t\t\t| Tahun\t| Penulis\t\t Stok\t")
    for idx in range(len(buku_keuangan)):
        print(f"{buku_keuangan[idx]['id']} \t| {buku_keuangan[idx]['judul']} \t\t\t| {buku_keuangan[idx]['tahun']}\t| {buku_keuangan[idx]['penulis']}\t {buku_keuangan[idx]['stok']}")

# ================================================================================================
# untuk menu 2
def bukuTambahan():
    # print("ID\t| Judul \t\t\t\t| Tahun\t| Penulis\t\t Stok\t")
    for buku in buku_keuangan:
        print(f"{buku['id']} \t| {buku['judul']} \t\t| {buku['tahun']}\t| {buku['penulis']}\t {buku['stok']}")
    #     return True
    # return False

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
daftar_menuUtama = ('''
    Daftar Halaman :
    1. Tampilkan Semua Buku
    2. Temukan Buku Melalui ID
    3. Kembali
''')

# -----------------------------------------------------------------------------------
# untuk menu 3
Daftar_editKolom = ('''
    Perbaharui Kolom yang Tersedia :
    1. ID
    2. Judul
    3. Tahun
    4. Penulis
    5. Stok
''')

# -----------------------------------------------------------------------------------
# untuk menu 1
def hasil_buku_dariId(buku_keuangan, buku_id):
    for buku in buku_keuangan:
        if buku['id'] == buku_id:
            # print(f"ID \t Judul \t\t\t\t Tahun \t Penulis \t Stok")
            print(f"\n{buku['id']} \t {buku['judul']} \t {buku['tahun']} \t {buku['penulis']} \t {buku['stok']} \n")
    #         return True
    # return False

# -----------------------------------------------------------------------------------
# untuk menu 1
def menu_berdasarkanId():
    
    keyId = (input("Masukan ID Buku : "))

    list_id = []

    for buku in buku_keuangan:
        list_id.append(buku['id'])

    if keyId in list_id:
        for buku in buku_keuangan:
            if buku['id'] == keyId:
                hasil_buku_dariId(buku_keuangan, keyId)
            

    else:
        print('\nBuku tidak ditemukan, Pastikan ID benar')
    menu_pertama()

# -----------------------------------------------------------------------------------
# untuk menu 1
def menu_pertama():
    while True:
        print(daftar_menuUtama)
        inputan_user = input("Masukan angka (1-3) diantara daftar diatas : ")
        print()
        if inputan_user == '1':
            daftar_bukuKeuangan()
            menu_pertama()

        elif inputan_user == '2':
            daftar_bukuKeuangan()
            menu_berdasarkanId()
        # elif inputan_user != inputan_user:        
        elif inputan_user == '3':
            menu_utama()
        else:
            menu_pertama()
        break

# ================================================================================================
# untuk menu 2
Opsi_tambahBuku = (''''
    Halaman Tambah Buku :
    1. Tambah Buku Baru
    2. Kembali
''')

# -----------------------------------------------------------------------------------
# untuk menu 2
def menu_kedua():
    print(Opsi_tambahBuku)
    inputan_user = (input("Masukan data Buku, tolong pilih diantara (1/2) : "))
    if inputan_user == '1':
        print()
        menuKedua_tambahBuku()

    elif inputan_user == '2':
        menu_utama()
    else:
        print("Tolong masukan angka yang tersedia : ")
        menu_kedua()
        

    

# -----------------------------------------------------------------------------------
# untuk menu 2
def menuKedua_tambahBuku():
    id_baru = input("Masukan ID baru : ")

    list_id = []

    for buku in buku_keuangan:
        list_id.append(buku['id'])

    if id_baru in list_id:
        print('\nID Buku tersebut sudah tersedia, tolong masukan ID baru \n')
        menu_kedua()

    else:
        judul = input("Masukan Judul Buku : ")
        tahun = input("Masukan Tahun Buku : ")
        penulis = input("Masukan Penulis Buku : ")
        stok = input("Masukan Jumlah Buku : ")
        bukuBaru = {'id':id_baru, 'judul':judul, 'tahun': tahun, 'penulis': penulis, 'stok':stok}
        print(bukuBaru)
        inputan_user = input("Yakin ingin menambahkan(Ya/Tidak) : ")
        if inputan_user.lower() == 'ya':
            buku_keuangan.append(bukuBaru)
            print("Data Tersimpan")
            menu_kedua()
        elif inputan_user.lower() == 'tidak':
            menuKedua_tambahBuku()
# ================================================================================================
# untuk menu 3
opsi_editBuku = ('''
    Halaman Edit Buku : 
    1. Edit Informasi Buku
    2. Kembali

''')

# -----------------------------------------------------------------------------------
# untuk menu 3
def menu_ketiga():
    
        print(opsi_editBuku)
        inputan_user = int(input("Kamu memasukin Halaman Edit Buku, Tolong masukan angka diantara (1/2) : "))
            
        if inputan_user == 1:
            print(f"\n{menuKetiga_perbaharuiBuku()}")
        elif inputan_user == 2:
            menu_utama()
        else:
            print("\nPilihan Nomor Tidak Sesuai")

# -----------------------------------------------------------------------------------
# untuk menu 3
def menuKetiga_perbaharuiBuku():
    
    daftar_bukuKeuangan()
    buku_id = input("\nMasukan ID Buku yang ingin Kamu Perbaharui : ")
    print()
        

    list_id = []

    for buku in buku_keuangan:
        list_id.append(buku['id'])

    for idx,buku in enumerate(buku_keuangan):
            
        if buku_keuangan[idx]['id'] == buku_id:
            print(buku)
            validasi = input("\nKamu yakin ingin melanjutkan?(Ya/Tidak): ")
            if validasi.lower() == 'tidak':
                print("\nPembaharuan dibatalkan")
                menu_ketiga()
            elif validasi.lower() == 'ya':
                print(Daftar_editKolom)
                pilihan_editBuku = input(f"Pilih data kategori yang ingin Kamu ubah, (diantara 1 sampai 5) : ")
                # -------------------------------------------------------------------------
                if pilihan_editBuku == '1':
                    hasil_buku_dariId(buku_keuangan, buku_id)
                    data_id = input("Masukan ID Baru : ")
                    validasi_id = input("Kamu yakin ingin melanjutkan?(Ya/Tidak): ")
                    print()
                    if validasi_id.lower() == "ya":
                        for idx,baru in enumerate(buku_keuangan):
                            if buku_id == buku_keuangan[idx]['id']:
                                buku_keuangan[idx]['id'] = data_id
                                print (baru)
                                print("\nData Telah Diperbaharui")
                                menu_ketiga()
                    elif validasi_id.lower() == "tidak":
                        print("\nPembaharuan dibatalkan")
                        menu_ketiga()
                # -------------------------------------------------------------------------
                elif pilihan_editBuku == '2':
                    hasil_buku_dariId(buku_keuangan, buku_id)
                    data_id = input("Masukan Judul Baru : ")
                    validasi_id = input("Kamu yakin ingin melanjutkan?(Ya/Tidak): ")
                    print()
                    if validasi_id.lower() == "ya":
                        for idx,baru in enumerate(buku_keuangan):
                            if buku_id == buku_keuangan[idx]['id']:
                                buku_keuangan[idx]['judul'] = data_id
                                print (baru)
                                print("\nData Telah Diperbaharui")
                                menu_ketiga()
                    elif validasi_id.lower() == "tidak":
                        print("\nPembaharuan dibatalkan")
                        menu_ketiga()
                # -------------------------------------------------------------------------
                elif pilihan_editBuku == '3':
                    hasil_buku_dariId(buku_keuangan, buku_id)
                    data_id = int(input("Masukan Tahun Baru : "))
                    validasi_id = input("Kamu yakin ingin melanjutkan?(Ya/Tidak): ")
                    print()
                    if validasi_id.lower() == "ya":
                        for idx,baru in enumerate(buku_keuangan):
                            if buku_id == buku_keuangan[idx]['id']:
                                buku_keuangan[idx]['tahun'] = data_id
                                print (baru)
                                print("\nData Telah Diperbaharui")
                                menu_ketiga()
                    elif validasi_id.lower() == "tidak":
                        print("\nPembaharuan dibatalkan")
                        menu_ketiga()
                # -------------------------------------------------------------------------
                elif pilihan_editBuku == '4':
                    hasil_buku_dariId(buku_keuangan, buku_id)
                    data_id = input("Masukan Penulis Baru : ")
                    validasi_id = input("Kamu yakin ingin melanjutkan?(Ya/Tidak): ")
                    print()
                    if validasi_id.lower() == "ya":
                        for idx,baru in enumerate(buku_keuangan):
                            if buku_id == buku_keuangan[idx]['id']:
                                buku_keuangan[idx]['penulis'] = data_id
                                print (baru)
                                print("\nData Telah Diperbaharui")
                                menu_ketiga()
                    elif validasi_id.lower() == "tidak":
                        print("\nPembaharuan dibatalkan")
                        menu_ketiga()
                # -------------------------------------------------------------------------
                elif pilihan_editBuku == '5':
                    hasil_buku_dariId(buku_keuangan, buku_id)
                    data_id = int(input("Masukan Stok Baru : "))
                    validasi_id = input("Kamu yakin ingin melanjutkan?(Ya/Tidak): ")
                    print()
                    if validasi_id.lower() == "ya":
                        for idx,baru in enumerate(buku_keuangan):
                            if buku_id == buku_keuangan[idx]['id']:
                                buku_keuangan[idx]['stok'] = data_id
                                print (baru)
                                print("\nData Telah Diperbaharui")
                                menu_ketiga()
                    elif validasi_id.lower() == "tidak":
                        print("\nPembaharuan dibatalkan")
                        menu_ketiga()

# ================================================================================================
# untuk menu 4
Opsi_menghapusBuku = ('''
    Kamu Memasuki Halaman Hapus Buku :
    1. Menghapus Daftar Buku
    2. Kembali
''')

# -----------------------------------------------------------------------------------
# untuk menu 4
def menuKeempat_hapusBuku():
    while True:
        print(Opsi_menghapusBuku)
        inputan_user = int(input("\n Pilih angka diantara (1/2) : "))

        list_id = []

        if inputan_user == 1:
            daftar_bukuKeuangan()
            hapus_buku = input("\nTolong pilih Buku yang ingin Kamu Hapus, Masukan ID Buku : ")
            for buku in buku_keuangan:
                list_id.append(buku['id'])

            if hapus_buku in list_id:

                for item in buku_keuangan.copy():
                    if item.get('id') == hapus_buku:
                        verifikasi_hapus = input("Kamu yakin ingin melanjutkan?(Ya/Tidak): ")
                        if verifikasi_hapus.lower() == 'ya':
                            buku_keuangan.remove(item)
                            print("\n Data Sudah Berhasil Dihapus")
                            break
                        elif verifikasi_hapus.lower() == 'tidak':
                            print("\n Data Tidak Berhasil Dihapus")
                            break
                print('\n')
                menuKeempat_hapusBuku()
                break

            else:
                print("\n ID Buku tidak terdaftar, Pastikan masukan ID yang Benar")
                break
        
        elif inputan_user == 2:
            break
        else:
            continue

# ================================================================================================

def menu_utama():
    print(f'''
        ------------------------------------------------------------------
            Selamat Datang di Aplikasi Perpustakaan Literasi Keuangan
        ------------------------------------------------------------------
        ''')
    print(daftar_pilihan)

    inputan_user = int(input("Masukan angka diantara Daftar tersebut : "))
    print()

    if inputan_user == 1:
        menu_pertama()
    elif inputan_user == 2:
        menu_kedua()
    elif inputan_user == 3:
        menu_ketiga()
    elif inputan_user == 4:
        menuKeempat_hapusBuku()
    elif inputan_user == 5:
        print('Senang bisa membantu Kamu, Kritik Dan Saran Hub: 085773127388\n')
        global x
        x = False
    else:
        print('Menu Tidak Tersedia')

x = True
while x == True:
    menu_utama()