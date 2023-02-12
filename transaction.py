class Transaction:
    """
    kelas yang merepresentasikan sebuah transaksi

    Attributes:
        item (dict): sebuah dictionary yang menyimpan data items transaksi
        final_price (float): sejumlah uang yang harus dibayarkan

    Methods:
        add_item(self, item_name, price, qty): menambah barang ke dalam daftar belanja
        update_item_name(self, item_name, new_item_name): mengubah nama item yang ada di daftar belanja
        update_item_qty(self, item_name, new_qty): mengubah jumlah item yang ada di daftar belanja
        update_item_price(self, item_name, new_price): mengubah harga item yang ada di daftar belanja
        delete_item(self, item_name): menghapus item yang ada di daftar belanja
        reset_transaction(self): menghapus semua item yang ada di daftar belanja
        check_order(self): menampilkan daftar belanja
        total_price(self): menampilkan total belanja
        payment(self): melakukan pembayaran
    """

    def __init__(self):
        """
        berisi semua atribut yang diperlukan oleh objek transaksi

        Parameters:
            item (dict): sebuah dictionary yang menyimpan data items transaksi
            final_price (float): sejumlah uang yang harus dibayarkan
        """
        self.item = {}
        self.final_price = 0

    def add_item(self, item_name, price, qty):
        """
        Method untuk menambahkan item ke dalam daftar belanja

        Parameters:
            item_name (str): nama item
            price (float): harga item
            qty (int): jumlah item

        Returns:
            Tidak ada

        Raises:
            ValueError: jika harga dan jumlah item yang diinputkan kurang dari sama dengan 0

        Prints:
            Pesan jika item berhasil ditambahkan
            Pesan jika terjadi kesalahan pada penginputan
            Pesan jika item gagal ditambahkan
        """
        if item_name not in self.item:
            try:
                if qty <= 0 or price <= 0:
                    raise ValueError
                else:
                    self.item[item_name] = [price, qty]
                    print(" ")
                    print("Item berhasil ditambahkan")
                    print(" ")
            except ValueError:
                print(" ")
                print("Harga atau jumlah item tidak boleh kurang dari 0")
                print(" ")
        else:
            print(" ")
            print(
                f"Item gagal ditambahkan\n{item_name} sudah ada di daftar belanja Anda"
            )
            print(" ")

    def update_item_name(self, item_name, new_item_name):
        """
        Method untuk mengubah nama item yang ada di daftar balanja

        Parameters:
            item_name (str): nama item yang akan diubah
            new_item_name (str): nama baru untuk item

        Returns:
            Tidak ada

        Raises:
            KeyError: Jika nama item yang akan diubah tidak ditemukan di daftar belanja

        Prints:
            Pesan jika nama item berhasil diubah
            Pesan jika nama item gagal diubah
        """
        try:
            self.item.update({new_item_name: self.item.pop(item_name)})
            print(" ")
            print("Nama item berhasil diubah")
            print(" ")
        except KeyError:
            print(" ")
            print(
                f"Nama item gagal diubah\n{item_name} tidak ada di daftar belanja Anda"
            )
            print(" ")

    def update_item_qty(self, item_name, new_qty):
        """
        Method untuk mengubah jumlah item yang ada di daftar belanja

        Parameters:
            item_name (str): nama item yang akan diubah jumlah pembeliannya
            new_qty (int): jumlah pembelian yang baru

        Returns:
            Tidak ada

        Raises:
            ValueError: Jika jumlah pembelian item kurang dari sama dengan 0
            KeyError: Jika item tidak ditemukan di daftar belanja

        Prints:
            Pesan jika jumlah item berhasil diubah
            Pesan jika terjadi kesalahan pada penginputan
            Pesan jika jumlah item gagal diubah
        """
        try:
            if new_qty <= 0:
                raise ValueError
            else:
                self.item[item_name][1] = new_qty
                print(" ")
                print(f"Jumlah {item_name} berhasil diubah")
        except ValueError:
            print(" ")
            print(
                f"Jumlah {item_name} gagal diubah\nJumlah item tidak boleh kurang dari 0"
            )
            print("")
        except KeyError:
            print(" ")
            print(
                f"Jumlah {item_name} gagal diubah\n{item_name} tidak ada di daftar belanja Anda"
            )
            print(" ")

    def update_item_price(self, item_name, new_price):
        """
        Method untuk mengubah harga item

        Parameters:
            item_name (str): nama item yang harganya akan diubah
            new_price (float): harga baru item

        Returns:
            Tidak ada

        Raises:
            ValueError: Jika harga baru item kurang dari sama dengan 0
            KeyError: Jika item tidak ditemukan di daftar belanja

        Prints:
            Pesan jika harga item berhasil diubah
            Pesan jika terjadi kesalahan pada penginputan
            Pesan jika harga item gagal diubah
        """
        try:
            if new_price <= 0:
                raise ValueError
            else:
                self.item[item_name][0] = new_price
                print(" ")
                print(f"Harga {item_name} berhasil diubah")
        except ValueError:
            print(" ")
            print(
                f"Harga {item_name} gagal diubah\nHarga item tidak boleh kurang dari 0"
            )
            print(" ")
        except KeyError:
            print(" ")
            print(
                f"Harga {item_name} gagal diubah\n{item_name} tidak ada di daftar belanja ANda"
            )
            print(" ")

    def delete_item(self, item_name):
        """
        Method untuk menghapus item yang ada di daftar belanja

        Parameters:
            item_name (str): nama item yang akan dihapus

        Returns:
            Tidak ada

        Raises:
            KeyError: Jika nama item tidak ditemukan di daftar belanja

        Prints:
            Pesan jika item berhasil dihapus
            Pesan jika item gagal dihapus
        """
        try:
            del self.item[item_name]
            print(" ")
            print(f"{item_name} berhasil dihapus")
            print(" ")
        except KeyError:
            print(" ")
            print(
                f"{item_name} gagal dihapus\n{item_name} tidak ada di daftar belanja Anda"
            )
            print(" ")

    def reset_transaction(self):
        """
        Method untuk menghapus semua item yang ada di daftar belanja

        Prints:
            Pesan jika semua item berhasil dihapus
        """
        self.item.clear()
        print(" ")
        print("Reset transaksi berhasil")
        print(" ")

    def check_order(self):
        """
        Method untuk menampilkan daftar belanja

        Prints:
            Tabel daftar belanja
        """
        key = [key for key in self.item.keys()]
        value1 = [value[0] for value in self.item.values()]
        value2 = [value[1] for value in self.item.values()]
        tot_price = [value1[i] * value2[i] for i in range(len(value1))]
        col_width = [15, 15, 15, 15]
        print(
            "Nama Item".ljust(col_width[0])
            + "Jumlah".ljust(col_width[1])
            + "Harga".ljust(col_width[2])
            + "Total Harga".ljust(col_width[3])
        )
        print("-" * (col_width[0] + col_width[1] + col_width[2] + col_width[3]))
        for i in range(len(key)):
            print(
                key[i].ljust(col_width[0])
                + str(value2[i]).ljust(col_width[1])
                + str(value1[i]).ljust(col_width[2])
                + str(tot_price[i]).ljust(col_width[3])
            )

    def total_price(self):
        """
        Method untuk menampilkan total harga dan harga akhir yang harus dibayarkan

        Jika total harga >= 500000 akan mendapat diskon 10%
        Jika total harga >= 300000 akan mendapat diskon 8%
        Jika total harga >= 200000 akan mendapat diskon 5%

        Prints:
            Total harga
            diskon
            harga akhir yang harus dibayarkan
        """
        total = 0
        discount = 0
        for name, value in self.item.items():
            total += value[0] * value[1]
        if total >= 500000:
            discount = total * 10 / 100
        elif total >= 300000:
            discount = total * 8 / 100
        elif total >= 200000:
            discount = total * 5 / 100
        self.final_price = total - discount
        print(f"Total harga sebelum diskon : {total}")
        print(f"Diskon : {discount}")
        print(f"Total harga setelah diskon : {self.final_price}")

    def payment(self, money):
        """
        Method untuk melakukan proses pembayaran

        Parameters:
            money (int): Jumlah uang yang dibayarkan

        Returns:
            Tidak ada

        Raises:
            ValueError: Jika jumlah uang kurang dari sama dengan 0

        Prints:
            Jumlah uang kembalian
            Pesan jika pembayaran berhasil
            Pesan jika terjadi salah penginputan
            Pesan jika pembayaran gagal
        """
        try:
            if money < 0:
                raise ValueError
            elif money < self.final_price:
                print(" ")
                print("Pembayaran gagal\nNominal uang tidak cukup")
            else:
                change = money - self.final_price
                print(f"Kembalian : {change}")
                print("Status : Lunas")
                print(" ")
                print(" " * 27 + "Terima Kasih")
                print(" ")
                self.item.clear()
        except ValueError:
            print(" ")
            print("Pembayaran gagal\nNominal uang tidak boleh kurang dari 0")
            print(" ")
