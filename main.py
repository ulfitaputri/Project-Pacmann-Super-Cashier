"""
Module ini berisi daftar menu dari sistem kasir Pacmart
"""
# import modul Transaksi
from transaction import *

# mendefinisikan variabel
tr = Transaction()

# looping menu
while True:
    print(" ")
    print("-" * 60)
    print("SELAMAT DATANG DI PACMART")
    print("-" * 60)
    print("1. Tambah Item")
    print("2. Ubah Nama Item")
    print("3. Ubah Harga Item")
    print("4. Ubah Jumlah Item")
    print("5. Hapus Item")
    print("6. Reset Transaksi")
    print("7. Cek Order")
    print("8. Pembayaran")
    print("9. Keluar")

    try:
        choice = int(input("\nInput nomor : "))
        print("-" * 60)
        if choice == 1:
            print("TAMBAH ITEM")
            print("-" * 60)
            item_name = str(input("Input nama item : "))
            price = float(input("Input harga item : "))
            qty = int(input("Input jumlah item: "))
            tr.add_item(item_name, price, qty)
        elif choice == 2:
            if len(tr.item) != 0:
                print("UBAH NAMA ITEM")
                print("-" * 60)
                print(" ")
                print(" " * 22 + "DAFTAR BELANJA\n")
                tr.check_order()
                print(" " * 60)
                print("-" * 60)
                item_name = str(input("Input nama item : "))
                new_item_name = str(input("Input nama baru item : "))
                tr.update_item_name(item_name, new_item_name)
            else:
                print("Daftar belanja Anda kosong")
                print(" ")
        elif choice == 3:
            if len(tr.item) != 0:
                print("UBAH HARGA ITEM")
                print("-" * 60)
                print(" ")
                print(" " * 22 + "DAFTAR BELANJA\n")
                tr.check_order()
                print(" " * 60)
                print("-" * 60)
                item_name = str(input("Input nama item: "))
                new_price = float(input("Input harga baru item : "))
                tr.update_item_price(item_name, new_price)
            else:
                print("Daftar belanja Anda kosong")
                print(" ")
        elif choice == 4:
            if len(tr.item) != 0:
                print("UBAH JUMLAH ITEM")
                print("-" * 60)
                print(" ")
                print(" " * 22 + "DAFTAR BELANJA\n")
                tr.check_order()
                print(" " * 60)
                print("-" * 60)
                item_name = str(input("Input nama item : "))
                new_qty = int(input("Input jumlah baru item : "))
                tr.update_item_qty(item_name, new_qty)
            else:
                print("Daftar belanja Anda kosong")
                print(" ")
        elif choice == 5:
            if len(tr.item) != 0:
                print("HAPUS ITEM")
                print("-" * 60)
                print(" ")
                print(" " * 22 + "DAFTAR BELANJA\n")
                tr.check_order()
                print(" " * 60)
                print("-" * 60)
                item_name = str(input("Input nama item : "))
                answer = str(input("Anda yakin? (y/t) : "))
                if answer.lower() == "t":
                    print("-" * 60)
                    print("Penghapusan item dibatalkan")
                    print(" ")
                elif answer.lower() == "y":
                    tr.delete_item(item_name)
                    print(" ")
                else:
                    print("-" * 60)
                    print("Item gagal dihapus, inputan salah")
                    print(" ")
            else:
                print("Daftar belanja Anda kosong")
                print(" ")
        elif choice == 6:
            if len(tr.item) != 0:
                print("RESET TRANSAKSI")
                print("-" * 60)
                print(" ")
                print(" " * 22 + "DAFTAR BELANJA\n")
                tr.check_order()
                print(" " * 60)
                print("-" * 60)
                answer = str(input("Anda yakin? (y/t) : "))
                if answer.lower() == "t":
                    print("-" * 60)
                    print("Reset transaksi dibatalkan")
                    print(" ")
                elif answer.lower() == "y":
                    tr.reset_transaction()
                    print(" ")
                else:
                    print("-" * 60)
                    print("Reset transaksi gagal, inputan salah")
                    print(" ")
            else:
                print("Daftar belanja Anda kosong")
                print(" ")
        elif choice == 7:
            if len(tr.item) != 0:
                print("CEK ORDER")
                print("-" * 60)
                print(" ")
                print(" " * 22 + "DAFTAR BELANJA\n")
                tr.check_order()
                print(" " * 60)
                print("-" * 60)
                tr.total_price()
            else:
                print("Daftar belanja Anda kosong")
                print(" ")
        elif choice == 8:
            if len(tr.item) != 0:
                print("PEMBAYARAN")
                print("-" * 60)
                print(" ")
                print(" " * 22 + "Daftar Belanja\n")
                tr.check_order()
                print(" " * 60)
                print("-" * 60)
                tr.total_price()
                money = float(input("Nominal Uang : "))
                tr.payment(money)
            else:
                print("Daftar belanja Anda kosong")
                print(" ")
        elif choice == 9:
            print("TERIMA KASIH")
            break
        else:
            print(f"Pilihan nomor {choice} tidak ditemukan")
    except ValueError:
        print("-" * 60)
        print("Ada kesalahan inputan")
