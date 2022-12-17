print("___________Khaerunnisa Isnaeni Lestari____________")
print("__________________Kelas TI 22 C1__________________")
print("________Program Menu Daftar Nilai Mahasiswa_______ ")


data = []
class Person():
	def __init__(self):
		self.data  = data

	def tambah(self):
		print("==== HALAMAN TAMBAH DATA MAHASISWA =====")
		nama = input("Masukkan Nama Mahasiswa : ")
		nim = input("Masukkan NIM Mahasiswa : ")
		nilai = input("Masukkan Nilai Mahasiswa : ")
		main = {"Nama":nama, "NIM":nim, "Nilai":nilai}
		self.data.append(main)
		print("=================================")
		print("  No  |  Nama  |  NIM  |  Nilai  |")
		print("==================================")
		for i, x in enumerate (data):
			print(f" {i}   |   {x['Nama']}   |   {x['NIM']}   |   {x['Nilai']}   |")

	def tampil(self):
		print("======== HALAMAN TAMPIL DATA MAHASISWA =======")
		for x in self.data :
			print("=================================")
			print("  No  |  Nama  |  NIM  |  Nilai  |")
			print("==================================")
			for i, x in enumerate (data):
				print(f" {i}   |   {x['Nama']}   |   {x['NIM']}   |   {x['Nilai']}   |")

	def ubah(self):
		print("========= HALAMAN UBAH DATA MAHASISWA ========")
		baris = int(input("Masukkan baris yang ingin diubah : "))
		edit_nama = input("Masukkan Nama : ")
		edit_nim = input("Masukkan NIM : ")
		edit_nilai = input("Masukkan Nilai : ")
		data[baris]['Nama'] = edit_nama
		data[baris]['NIM'] = edit_nim
		data[baris]['Nilai'] = edit_nilai
		for x in data :
			print("=================================")
			print("  No  |  Nama  |  NIM  |  Nilai  |")
			print("==================================")
			for i, x in enumerate (data):
				print(f" {i}   |   {x['Nama']}   |   {x['NIM']}   |   {x['Nilai']}   |")


	def hapus(self):
		a = input("Nama yang ingin dihapus : ")
		b = int(input("Masukkan baris yang ingin dihapus : "))
		del self.data[b]
		print("DATA TELAH DIHAPUS")

	def keluar(self):
		print("====== HALAMAN KELUAR =======")

	def showmenu(self):
		while True:
			print("\n")
			print("_________Tampilan Menu________")
			print("[1] Tambah Data")
			print("[2] Tampilkan Data")
			print("[3] Ubah Data")
			print("[4] Hapus Data")
			print("[5] Keluar Data")
			menu = int(input("SILAHKAN PILIH MENU : "))
			print("\n")
			if menu == 1:
				self.tambah()
			if menu == 2:
				self.tampil()
			if menu == 3:
				self.ubah()
			if menu == 4:
				self.hapus()
			if menu == 5:
				self.keluar()
			x = input("TAMPILKAN MENU KEMBALI (y/t) : ")
			if x == "t":
				break


		
op1 = Person()
op1.showmenu()
