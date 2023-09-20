def create_element(elements):
    elem = input("Masukkan elemen baru: ")
    elements.append(elem)
    print("Elemen berhasil ditambahkan.")

def read_elements(elements):
    print("Elemen dalam list:")
    for i, elem in enumerate(elements):
        print(f"{i+1}. {elem}")

def update_element(elements):
    index = int(input("Masukkan indeks elemen yang ingin diubah: "))
    if 0 <= index < len(elements):
        new_value = input(f"Masukkan nilai baru untuk elemen ke-{index+1}: ")
        elements[index] = new_value
        print("Elemen berhasil diubah.")
    else:
        print("Indeks tidak valid.")

def delete_element(elements):
    index = int(input("Masukkan indeks elemen yang ingin dihapus: "))
    if 0 <= index < len(elements):
        removed_elem = elements.pop(index)
        print(f"Elemen '{removed_elem}' pada indeks {index+1} berhasil dihapus.")
    else:
        print("Indeks tidak valid.")

def main():
    elements = []

    while True:
        print("\nMenu:")
        print("1. Create (Tambah elemen)")
        print("2. Read (Tampilkan elemen)")
        print("3. Update (Ubah elemen)")
        print("4. Delete (Hapus elemen)")
        print("5. Keluar")

        choice = int(input("Pilih menu (1/2/3/4/5): "))

        if choice == 1:
            create_element(elements)
        elif choice == 2:
            read_elements(elements)
        elif choice == 3:
            update_element(elements)
        elif choice == 4:
            delete_element(elements)
        elif choice == 5:
            print("Program selesai.")
            break
        else:
            print("Menu tidak valid. Pilih lagi.")

if __name__ == "__main__":
    main()
