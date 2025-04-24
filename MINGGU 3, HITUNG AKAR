import math

while True:
    try:
        user_input = input("Masukkan angka: ")
        angka = float(user_input)

        if angka < 0:
            print("Input tidak valid. Harap masukkan angka positif.")
        elif angka == 0:
            raise ValueError("Akar kuadrat dari nol tidak diperbolehkan.")
        else:
            akar = math.sqrt(angka)
            print(f"Akar kuadrat dari {angka} adalah {akar}")
            break  # keluar dari loop jika input valid
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception:
        print("Input tidak valid. Harap masukkan angka yang valid.")
