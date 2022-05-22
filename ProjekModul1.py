daftarPasien = [
    {"id" : 1,
    "nama":"Jeffrey ",
    "umur":22,
    "alamat":"Jl Karet ",
    "penyakit":"Batuk" },
    {"id" : 2,
    "nama":"Faris",
    "umur":25,
    "alamat":"Jl semanggi timur",
    "penyakit":"Pilek" }
    ]

def readData():
    while True:
        pilihan1 = int(input('''
        Data Pasien Rumah Sakit Siloam

        1. Data Seluruh Pasien
        2. Data Pasien Tertentu
        3. Kembali ke Menu Utama

        Masukkan pilihan menu : '''))
        print()
        if pilihan1 == 1:
            if len(daftarPasien)==0:
                print("Tidak Ada Data Pasien")
            else:
                for i in range(len(daftarPasien)):
                    print(f'ID Pasien\t : {daftarPasien[i]["id"]}\nNama\t\t : {daftarPasien[i]["nama"]}\nUmur\t\t : {daftarPasien[i]["umur"]}\nAlamat\t\t : {daftarPasien[i]["alamat"]}\nPenyakit\t : {daftarPasien[i]["penyakit"]}\n')
        elif pilihan1 == 2:
            id = int(input("Masukkan ID Pasien : "))
            print()
            while True:
                for j in range(len(daftarPasien)):
                    if id == daftarPasien[j]["id"]:
                        print(f'ID Pasien\t : {daftarPasien[j]["id"]}\nNama\t\t : {daftarPasien[j]["nama"]}\nUmur\t\t : {daftarPasien[j]["umur"]}\nAlamat\t\t : {daftarPasien[j]["alamat"]}\nPenyakit\t : {daftarPasien[j]["penyakit"]}\n')
                        break
                    elif j == len(daftarPasien)-1:
                        print("Maaf ID Pasien Tidak Ada")
                        break   
                break 
        elif pilihan1 == 3:
            yakinKeluar = input("Apakah anda ingin kembali ke menu utama? (Y/N) : ")
            yakinKeluar = yakinKeluar.upper()
            if yakinKeluar == 'Y':
                break
            elif yakinKeluar == 'N':
                continue
            else:
                print("Harapa pilih menu 'Y' jika ingin melanjutkan atau 'N' untuk menggagalkan")
                continue
            
        else:
            print("Pilihan menu yang anda pilih tidak ada")

def createData():
    while True:
        pilihan2 = int(input('''
        Menambah Data Pasien Rumah Sakit Siloam
        
        1. Tambah Data Pasien
        2. Kembali ke Menu Utama
        
        Masukkan pilihan menu : '''))
        print()
        if pilihan2 == 1:
            id = int(input('''
            Masukkan ID Pasien : '''))
            print()
            while True:
                for j in range(len(daftarPasien)):
                    if id == daftarPasien[j]["id"]:
                        print("Data pasien dengan ID tersebut sudah ada")
                        break
                    elif j == len(daftarPasien)-1:
                        nama = input("Masukkan nama pasien : ")
                        umur = int(input("Masukkan umur pasien : "))
                        alamat = input("Masukkan alamat pasien : ")
                        penyakit = input("Masukkan penyakit pasien : ")
                        yakin = input("Apakah anda yakin menambahkan data? (Y/N) : ")
                        print()
                        yakin = yakin.upper()
                        if yakin == 'Y':
                            daftarPasien.append({"id":id,"nama":nama,"umur":umur,"alamat":alamat,"penyakit":penyakit})
                            print("Data telah tersimpan")
                            break   
                        elif yakin == 'N':
                            print("Data tidak tersimpan")
                            break
                        else:
                            print("Harapa pilih menu 'Y' jika ingin lanjut atau 'N' menggagalkan ubah data")
                            break
                break
        elif pilihan2 == 2:
            yakinKeluar = input("Apakah anda ingin kembali ke menu utama? (Y/N) : ")
            yakinKeluar = yakinKeluar.upper()
            if yakinKeluar == 'Y':
                break
            elif yakinKeluar == 'N':
                continue
            else:
                print("Harapa pilih menu 'Y' jika ingin melanjutkan atau 'N' menggagalkan")
                continue
        else:
            print("Pilihan menu yang anda pilih tidak ada")

def updateData():
    while True:
        pilihan3 = int(input('''
        Mengubah Data Pasien Rumah Sakit Siloam
        
        1. Ubah Data Pasien
        2. Kembali ke Menu Utama
        
        Masukkan pilihan menu : '''))
        print()
        if pilihan3 == 1:
            id = int(input("Masukkan ID Pasien : "))
            print()
            for i in range(len(daftarPasien)):
                if id == daftarPasien[i]["id"]:
                    print(f'ID Pasien\t : {daftarPasien[i]["id"]}\nNama\t\t : {daftarPasien[i]["nama"]}\nUmur\t\t : {daftarPasien[i]["umur"]}\nAlamat\t\t : {daftarPasien[i]["alamat"]}\nPenyakit\t : {daftarPasien[i]["penyakit"]}\n')
                    yakin = input("Apakah ingin lanjut ubah data pasien? (Y/N) : ")
                    yakin = yakin.upper()
                    print()
                    if yakin == 'Y':
                        kolom = input("Masukkan kolom atau bagian yang ingin diubah : ")
                        kolom = kolom.lower()
                        if kolom == 'id':
                            print("Maaf, kolom ID tidak bisa diubah")
                            break
                        elif kolom in daftarPasien[i]:
                            newValue = input(f"Masukkan {kolom} baru : ")
                            yakin2 = input(f"Apakah anda yakin ingin mengubah kolom '{kolom}'? (Y/N) : ")
                            yakin2 = yakin2.upper()
                            if yakin2 == "Y":
                                daftarPasien[i][kolom] = newValue
                                print()
                                print(f"Kolom '{kolom}' berhasil di diubah")
                                break
                            elif yakin2 == "N":
                                print(f"Kolom {kolom} tidak jadi diubah")
                                break
                            else:
                                print("Harapa pilih menu 'Y' jika ingin lanjut atau 'N' menggagalkan simpan data")
                                break
                        else:
                            print(f"Maaf kolom '{kolom}' tidak ada")
                            break
                    elif yakin == 'N':
                        print("Data tidak jadi diubah")
                        break
                    else:
                        print("Harapa pilih menu 'Y' jika ingin lanjut atau 'N' menggagalkan simpan data")
                        break

                elif i == len(daftarPasien)-1:
                    print("Maaf ID Pasien Tidak Ada")
                    break
        elif pilihan3 == 2:
            yakinKeluar = input("Apakah anda ingin kembali ke menu utama? (Y/N) : ")
            yakinKeluar = yakinKeluar.upper()
            if yakinKeluar == 'Y':
                break
            elif yakinKeluar == 'N':
                continue
            else:
                print("Harapa pilih menu 'Y' jika ingin melanjutkan atau 'N' menggagalkan")
                continue
        else:
            print("Pilihan menu yang anda pilih tidak ada")

def deleteData():
    while True:
        pilihan4 = int(input('''
        Menghapus Data Pasien Rumah Sakit Siloam
        
        1. Hapus Data Pasien
        2. Kembali ke menu utama
        
        Masukkan pilihan menu : '''))
        print()
        if pilihan4 == 1 : 
            id = int(input("Masukkan ID Pasien yang ingin di hapus : "))
            for i in range(len(daftarPasien)):
                if id == daftarPasien[i]["id"]:
                    print(f'ID Pasien\t : {daftarPasien[i]["id"]}\nNama\t\t : {daftarPasien[i]["nama"]}\nUmur\t\t : {daftarPasien[i]["umur"]}\nAlamat\t\t : {daftarPasien[i]["alamat"]}\nPenyakit\t : {daftarPasien[i]["penyakit"]}\n')
                    yakin = input("Apakah ingin lanjut menghapus data pasien? (Y/N) : ")
                    yakin = yakin.upper()
                    print()
                    if yakin == 'Y':
                        print("Data berhasil dihapus")
                        del daftarPasien[i]
                        break
                    elif yakin == 'N':
                        print("Data tidak jadi dihapus")
                        break
                    else:
                        print("Harapa pilih menu 'Y' jika ingin lanjut atau 'N' menggagalkan hapus data")
                        break
                elif i == len(daftarPasien)-1:
                    print()
                    print("Pasien yang anda cari tidak ada")
                    break
                
        elif pilihan4 == 2:
            yakinKeluar = input("Apakah anda ingin kembali ke menu utama? (Y/N) : ")
            yakinKeluar = yakinKeluar.upper()
            if yakinKeluar == 'Y':
                break
            elif yakinKeluar == 'N':
                continue
            else:
                print("Harapa pilih menu 'Y' jika ingin melanjutkan atau 'N' menggagalkan")
                continue
        else:
            print("Pilihan menu yang anda pilih tidak ada")
    
while True:
    pilihan = int(input('''
    Selamat Datang di Rumah Sakit Siloam

    1. Lihat data pasien
    2. Menambahkan data pasien
    3. Mengubah data pasien
    4. Menghapus data pasien
    5. Keluar dari program

    Masukkan pilihan menu : '''))
    print()
    if (pilihan == 1):
        readData()
    
    elif(pilihan == 2):
        createData()
    
    elif(pilihan == 3):
        updateData()
    
    elif(pilihan == 4):
        deleteData()
        
    elif (pilihan == 5):
        yakinKeluar = input("Apakah anda ingin keluar dari program? (Y/N) : ")
        yakinKeluar = yakinKeluar.upper()
        if yakinKeluar == 'Y':
            print("Anda telah keluar dari program")
            break
        elif yakinKeluar == 'N':
            continue
        else:
            print("Harapa pilih menu 'Y' jika ingin melanjutkan atau 'N' untuk menggagalkan")
            continue
    else:
        print("Maaf pilihan menu yang anda masukkan salah ")