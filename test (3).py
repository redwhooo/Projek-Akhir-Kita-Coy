import csv
import getpass
import os

def logIn(username, password):
    sukses = False
    try:
        with open("datauser (1).csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # Lewati baris header
            for row in reader:
                if len(row) < 2:  # Abaikan baris yang tidak valid
                    continue
                a, b = row[0].strip(), row[1].strip()  # Bersihkan whitespace
                if a == username and b == password:
                    sukses = True
                    break
    except FileNotFoundError:
        print("\nFile datauser.csv tidak ditemukan.")
        return
    except Exception as e:
        print(f"\nTerjadi kesalahan: {e}")
        return

    if sukses:
        if username == 'Admin' and password == 'AdminProPlayer':
            os.system('cls' if os.name == 'nt' else 'clear')  # Bersihkan layar (Windows/Linux)
            akses_admin()  # Masuk ke menu admin
        else:
            akses_pelanggan()  # Masuk ke menu pelanggan
    else:
        input('\nUsername atau password salah atau tidak terdaftar.\nJika belum memiliki akun, silahkan Sign Up terlebih dahulu.')
        akses(1)  # Kembali ke menu login


def signUp(username, password, email):
    try:
        with open("datauser (1).csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([username.strip(), password.strip(), email.strip()])
        print("\nAkun berhasil dibuat!")
    except Exception as e:
        print(f"\nTerjadi kesalahan saat membuat akun: {e}")


def akses(opsi):
    if opsi == 1:
        username = input('\nMasukkan Username: ').strip()
        password = getpass.getpass('Masukkan Password: ')
        logIn(username, password)
    elif opsi == 2:
        username = input('\nMasukkan Username Baru: ').strip()
        password = input('Masukkan Password Baru: ').strip()
        email = input('Masukkan alamat email: ').strip()
        signUp(username, password, email)
        input('Sign Up berhasil, silahkan masuk.')
        akses(1)  # Kembali ke login setelah sign up
    elif opsi == 3:
        print('\nTerima kasih sudah berkunjung!\n')
        exit()


def akses_admin():
    while True:
        print('\nHalo Admin!\nMau ngapain hari ini?')
        print('=' * 50)
        print('1. Data Petani\n2. Data Pesanan\n3. Data Pengguna\n4. Keluar')
        print('=' * 50)
        try:
            opsi_admin = int(input('Silahkan pilih menu (1/2/3/4): '))
            if opsi_admin == 1:
                print('Fitur Data Petani belum tersedia.')  # nama petani, alamat petani, skill (5)
            elif opsi_admin == 2:
                print('Fitur Data Pesanan belum tersedia.')
            elif opsi_admin == 3:
                try:
                    with open("datauser (1).csv", "r") as file:
                        reader = csv.reader(file)
                        print("\nData Pengguna:")
                        for row in reader:
                            print(row)
                except FileNotFoundError:
                    print('\nFile datauser.csv tidak ditemukan.')
            elif opsi_admin == 4:
                print('Kembali ke menu utama.')
                awal()
                break
            else:
                input('\nHarap pilih menu yang ada.')
        except ValueError:
            input('\nHarap masukkan angka yang valid.')


def akses_pelanggan():
    print('\nLogin berhasil. Selamat datang, pengguna!\n')


def awal():
    print('\nSelamat datang di Smart Farm!')
    print('=' * 50)
    print('1. Log In (Masuk ke akun yang sudah ada.)\n2. Sign Up (Untuk mendaftar akun baru.)\n3. Keluar')
    print('=' * 50)
    try:
        opsi = int(input('Silahkan pilih menu untuk masuk ke aplikasi (1/2/3): '))
        if opsi in [1, 2, 3]:
            akses(opsi)
        else:
            input('\nHarap pilih menu yang ada.')
            awal()
    except ValueError:
        input('\nHarap masukkan angka saja.')
        awal()


awal()
