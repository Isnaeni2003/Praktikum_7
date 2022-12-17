# Praktikum_7
## Apa Itu Def Init?
Pada pemrograman python terdapat sebuah method dengan nama __init__(), Fungsi Method Init Pada Pemrograman Python yaitu merupakan method yang pertama kali di jalankan atau di proses sebelum method-method yang lainnya dan method __init__() berguna untuk melakukan inisialisasi pembuatan object dari class.
## Penggunaan Def Init
![image](https://user-images.githubusercontent.com/115929351/208215616-aa6c0dda-0d96-4f69-8b68-4dd05869066f.png)

Function di dalam sebuah class disebut sebagai sebuah metode class tersebut. Di sini kita buat sebuah metode bernama __init__. Metode dengan nama ini sudah direservasi oleh Python sebagai metode yang dipanggil saat kita membuat sebuah objek. Di setiap metode class harus selalu ada self sebagai parameter pertamanya. Variabel self merujuk kepada objek dari class tersebut. Di metode ini kita tambah sebuah parameter bernama nama_gadget. Di metode ini juga kita membuat properti nama dengan sintaks self.nama dan memberikan nilai dari nama_gadget.
## Latihan Membuat Program Menampilkan Daftar Menu Mahasiswa
Tugas Praktikum

Buatlah program sederhana dengan mengaplikasikan penggunaan class. Buatlah class untuk menampilkan daftar nilai mahasiswa dengan ketentuan :

a. Method tambah() untuk menambah data

b. Method tampilkan() untuk menampilkan data

c. Method ubah() untuk mengubah data

c. Method hapus() untuk menghapus data

d. Buat diagram class, flowchart dan penjelasannya pada README.md

e. Commit dan push repository ke github

## Flowchart
![Flowcharts](https://user-images.githubusercontent.com/115929351/208222109-41f7d3ef-859a-47d8-aaca-b0aac00c5525.png)

## Membuat Program Menampilkan Daftar Menu Mahasiswa
![codinginit](https://user-images.githubusercontent.com/115929351/208216527-06289375-9eed-41df-84b9-2f228e3535cc.png)
Pada pertemuan kali ini saya akan mengaplikasin fungsi def init dalam menampilkan nilai mahasiswa, def init merupakan inisialisasi object pada sebuah class. Class dapat dikatakan sebagai object constructor atau “blueprint” untuk membuat sebuah object.
## Step by Step
![carbon(5)](https://user-images.githubusercontent.com/115929351/208216874-7907eb46-0ea7-4ab1-8e86-8a2f6cf2e4a3.png)
1. Tahap pertama yaitu saya membuat class bernama person lalu kita mengaplikasikan fungsi def init, kemudian Keyword self sendiri digunakan untuk merepresentasikan setiap objek yang dibuat.

2. Next saya membuat menu tambah, seperti biasa saya menggunakan method append untuk mengganbungkan beberapa variabel, dan ini yang berbeda yaitu kita memanggil self.data karena self ini merupakan variabel yang mempresentasikan dalam class yang kita buat, jadi setiap kita memanggil fungsi def, self ini harus terus diikutsertakan.

3. Disini saya membuat menu tampil, saya menggunakan fungsi for untuk melakukan perulangan data.

4. Selanjutnya menu ubah, saya membuat inputan Nama , NIM serta Nilai, dan membuat ketiga variabel tersebut untuk mengubah data  berdasarkan nama dan value lainnya, dan memakai indeks integer yang nantinya akan diinput user, baris keberapa yang ingin diubah. Tidak lupa menggunakan for untuk mengulang kembali data tersebut.

5. Menu selanjutnya adalah hapus, saya membuat inputan Nama serta NIM yang ingin user hapus dan menggunakan method del untuk menghapus 1 baris data tersebut dan tidak lupa mengikutsertan self.data.

6. Kemudian, ialah menu keluar pada menu looping di showmenu saya menyertakan break ketika user memutuskan untuk keluar.

7. Terakhir, saya membuat daftar menu untuk user menginput menu apa yang ingin dijalankan, dan pada masing-masing menu saya sertakan self dilanjutkan dengan memanggil masing-masing fungsi def, seperti tambah(), tampil(), ubah(), hapus(), keluar(). Dan saya membuat object baru yang mendeklarasikan class yaitu person, kemudian object tersebut saya gunakan untuk mencetak showmenu yang artinya untuk terus menjalankan daftar menu.

## Hasil Output Program Menampilkan Daftar Menu Mahasiswa
![cover menu](https://user-images.githubusercontent.com/115929351/208218001-82df8862-bd63-454b-aef6-b74158a2248c.png)
Ini merupakan hasil output dari tampilan awal menu , terdapat menu [1]tambah, [2]tampil, [3]ubah. [4]hapus, dan [5]keluar
![tambah](https://user-images.githubusercontent.com/115929351/208218070-5ed1a6db-b6ec-4ba6-9c8b-3084f5b92f0f.png)
Dan berikut adalah tampilan dari menu tambah, seperti biasa disini user akan menginput Nama, NIM, serta Nilai yang akan dijadikan daftar tabel. 
![lihut](https://user-images.githubusercontent.com/115929351/208218389-b830fe21-1bb9-4f5f-8f6f-959db49b1cb4.png)
Berikutnya ini merupakan hasil output dari menu tampil, disini user telah menambahkan 2 buah data mahasiswa yaitu Khalisa dengan NIM 312210008 dan Nilai 89 serta Meizaya dengan NIM 312210005 serta Nilai 90. Dan user ingin mencoba menampilkan kedua data tersebut dalam tabel dengan menginput pilihan no 2
![ubahubih](https://user-images.githubusercontent.com/115929351/208218498-a0a0a0ed-9ca2-4d2c-aa95-91873803be6e.png)
Selanjutnya adalah output dari hasil menu ubah, disini user menginput baris yang ingin diubah dengan melihat indeks pada data dilanjutkan dengan menginput perubahan Nama yang akan diubah, NIM yang akan diubah, serta Nilai yang akan diubah. Pada data sebelumnya saya mempunyai 3 data Mahasiswa yaitu, Khalisa, Meizaya dan Katrina. Dan saya memutuskan untuk mengubah data Meizaya pada indeks 1, saya mengubah nama Meizaya menjadi Zaynale diikuti dengan NIM serta Nilai yang juga diubah.
![nampil](https://user-images.githubusercontent.com/115929351/208219175-bb3ac3a7-0916-48ec-bf6c-879d8942729b.png)
Menu berikutnya adalah tampilan dari menu hapus, yaitu disini user akan menginput Nama yang akan dihapus, serta baris (indeks) yang ingin dihapus, dan akan memunculkan data telah dihapus dan untuk mengecek apakah data yang saya hapus benar-benar terhapus maka saya memilih no 2 pada show menu untuk menampilkan data.
![out](https://user-images.githubusercontent.com/115929351/208219524-9af92920-cf90-479b-85ae-a0c5ef7ae599.png)
Tampilan terakhir ialah output dari menu keluar, dan program akan menanyakan apakah ingin menampilkan menu kembali jika 't' maka program akan otomatis keluar.
## Diagram Class
![Untitled Workspace](https://user-images.githubusercontent.com/115929351/208222046-e22f0a4e-19e9-491c-a733-b9cc13849547.png)

# Thanks For Read Everyone







