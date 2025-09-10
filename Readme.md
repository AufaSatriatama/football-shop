# Web

https://aufa-daffa-footballshop.pbp.cs.ui.ac.id/

# Penjelasan

## 1. 

### Pertama-tama, kita dapat membuat sebuah folder baru, jalankan virtual environment, kemudian, kita buat sebuah file requirements.txt yang berisi dependencies untuk proyek Django kita. Lalu, kita bisa menginstal dependencies tersebut lalu kita buat proyek Django dengan perintah ` django-admin startproject football_news . `

### Setelah itu, kita dapat membuat file .env, .env.prod dan  .gitignore agar mengatur environment variable kita dan agar file tersebut tidak terkena push ke github. 

### Kemudian, kita akan membuat sebuah app dengan nama 'main' 

` 
python manage.py startapp main
`

Kemudian, kita daftarkan 'main' tadi ke settings.py di bagian INSTALLED_APPS

### Pada football_shop/urls.py, kita tambahkan root url ke app main

### Buka berkas models.py yang ada di app main kita. Lalu, modifikasi sesuai dengan apa saja data/atribut yang akan dimiliki. Ada satu atribut yang wajib, yaitu id. 

### Selanjutnya, buka file views.py, di sana, kita definisikan method baru untuk dikembalikan ke html. Kita dapat mengisinya dengan data yang akan ditampilkan di html nanti

### Selanjutnya, buka urls.py di bagian app, lalu kita isi dengan endpoint dan apa nama method yang telah kita definisikan di views.py tadi. Jangan lupa untuk melakukan import terlebih dahulu

### Terakhir, kita akan melakukan deployment ke pws. Pertama tama, kita sambungkan dulu proyek lokal kita ke proyek github. Kita inisialisasi terlebih dahulu git

`
git init
git remote add origin <url proyek github>
git add . 
git commit -m "<isi comment>
git push origin master
`

### Selanjutnya, kita akan mendeploy ke pws. Ikuti petunjuk yang ada di pws, jangan lupa untuk konfigurasi settings.py agar bisa diakses oleh pws, dan edit environs di pws dengan data yang ada di .env.prod yang kita miliki

## 2. 

### Pada halaman utama, ada sebuah tombol bertuliskan "Ke Dashboard" yang akan mengalihkan tampilan halaman pengguna ke halaman dashboard. Pertama, kita bisa membuat satu file html baru yang kita beri nama dashboard.html, kemudian, kita tambahkan file dashboard.html tadi ke file urls.py. Di sana, kita tambahkan endpoint untuk dashboard.html tadi, contohnya kita menggunakan dashboard/. models.py dapat kita gunakan jika kita ingin menambahkan model untuk dashboard.html

## 3. 

### settings.py di django berguna untuk mengatur konfigurasi proyek Django, seperti pengaturan database, middleware, aplikasi mana yang di-install, siapa saja yang bisa mengakses (ALLOWED_HOSTS), internalization, static files, authentication, dan lain-lain. 

## 4. 

### Saat kita menulis model di models.py, kita sebenarnya akan menulis object untuk SQL. Akan tetapi, untuk mempermudah, kita dapat menggunakan bahasa python. Migrasi ini bertujuan untuk mengubah model yang kita tulis dalam bahasa python untuk di-eksekusi dan dicatat di SQL. Mekanismenya adalh dengan kita menjalankan perintah untuk migrasi sehingga django akan bikin file di folder migrations/.

## 5. 

### Saya mendengar bahwa django merupakan framework yang ramah untuk pemula web development dibandingkan dengan framework yang lain, seperti spring, axum, dan lain-lain.

## 6. 

### Saya rasa masih tidak ada perlu yang dikoreksi. Mungkin ini dikarenakan topik yang masih tidak membingungkan, cukup ikuti saja tutorial yang ada di dokumentasi yang tersedia.
