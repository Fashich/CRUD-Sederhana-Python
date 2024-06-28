data_fashich = []
def create():
    input_data_fashich = input("Masukkan Data Baru: ")
    data_fashich.append(input_data_fashich)
    print("Data Berhasil Ditambahkan!")
def read():
    print("Data Saat Ini: ")
    for i, data in enumerate(data_fashich):
        print(f"{i}: {data}")
def update():
    try:
        index_fashich = int(input("Masukkan Indeks Data yang ingin diupdate: "))
        if 0 <= index_fashich < len(data_fashich):
            input_data_fashich = input("Masukkan Data Baru: ")
            data_fashich[index_fashich] = input_data_fashich
            print("Data Berhasil Di Update!")
        else:
            print("Indeks Tidak Valid!, Mohon Coba Lagi!")
    except ValueError:
        print("Indeks Tidak Valid!, Mohon Coba Lagi!")
def delete():
    try:
        index_fashich = int(input("Masukkan Indeks Data Yang Ingin Dihapus: "))
        if 0 <= index_fashich < len(data_fashich):
            data_fashich.pop(index_fashich)
            print("Data Berhasil Dihapus!")
        else:
            print("Indeks Tidak Valid!, Silakan Coba Lagi")
    except ValueError:
        print("Indeks Tidak Valid!, Silakan Coba Lagi")
def main():
    keluar = False
    while not keluar:
        print("Pilih Operasi:")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Keluar")
        try:
            pilihan = int(input("Masukkan Pilihan: "))
            if pilihan == 1:
                create()
            elif pilihan == 2:
                read()
            elif pilihan == 3:
                update()
            elif pilihan == 4:
                delete()
            elif pilihan == 5:
                keluar = True
            else:
                print("Pilihan Anda Tidak Valid!, Mohon Pilih Yang Tersedia")
        except ValueError:
            print("Pilihan Anda Tidak Valid!, Mohon Pilih Yang Tersedia")
if __name__ == "__main__":
    main()
