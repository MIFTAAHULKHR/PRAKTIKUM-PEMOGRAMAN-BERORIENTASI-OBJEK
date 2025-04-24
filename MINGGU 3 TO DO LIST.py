def tampilkan_menu():
    print("\nPilih aksi:")
    print("1. Tambah tugas")
    print("2. Hapus tugas")
    print("3. Tampilkan daftar tugas")
    print("4. Keluar")

def tampilkan_daftar(tugas):
    if not tugas:
        print("Daftar tugas kosong.")
    else:
        print("Daftar Tugas:")
        for i, t in enumerate(tugas, 1):
            print(f"{i}. {t}")

def tambah_tugas(tugas):
    try:
        isi = input("Masukkan tugas yang ingin ditambahkan: ").strip()
        if not isi:
            raise ValueError("Tugas tidak boleh kosong.")
        tugas.append(isi)
        print("Tugas berhasil ditambahkan!")
    except ValueError as ve:
        print(f"Error: {ve}")

def hapus_tugas(tugas):
    try:
        nomor = input("Masukkan nomor tugas yang ingin dihapus: ").strip()
        if not nomor.isdigit():
            raise ValueError("Input harus berupa angka.")
        index = int(nomor) - 1
        if index < 0 or index >= len(tugas):
            raise IndexError(f"Tugas dengan nomor {nomor} tidak ditemukan.")
        tugas.pop(index)
        print("Tugas berhasil dihapus!")
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")

# Program utama
tugas = []

while True:
    tampilkan_menu()
    try:
        pilihan = input("Masukkan pilihan (1/2/3/4): ").strip()
        if pilihan not in ['1', '2', '3', '4']:
            raise ValueError("Pilihan tidak valid. Harap masukkan 1, 2, 3, atau 4.")
        
        if pilihan == '1':
            tambah_tugas(tugas)
        elif pilihan == '2':
            hapus_tugas(tugas)
        elif pilihan == '3':
            tampilkan_daftar(tugas)
        elif pilihan == '4':
            print("Keluar dari program.")
            break
    except ValueError as ve:
        print(f"Error: {ve}")
