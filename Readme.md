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


# Penjelasan Tugas 2

## 1.

### Dalam membuat aplikasi, jelas kita perlu berinteraksi dengan data. Mulai dari data sederhana seperti apakah pengguna sudah login, hingga data kompleks, kita tidak bisa lepas dari data. Dengan dmeikian, data delivery merupakan sesuatu yang sangat penting dalam membuat aplikasi

## 2.

### Saya rasa, sebagai praktisi, JSON lebih baik daripada XML karena JSON lebih populer digunakan yang mengakibatkan pembelajarannya menjadi lebih mudah dibanding XML. Semenjak javascript sangat banyak digunakan dalam pengembangan front end, penggunaan JSON menjadi sangat populer karena JSON berasal dari object javascript.

## 3.

### is_valid() digunakan untuk mengecek apakah data / form yang dikirim user merupakan form yang valid sesuai dengan peraturan yang kita tulis di forms.py (Untuk kasus di sini, forms.py mengikuti aturan yang ada di models.py seperti max length dan sebagainya).

## 4.

### Kita perlu menambahkan "csrf_token" dalam form. Ini untuk mencegah adanya penyerang yang mengirim request menggunakan cookie yang dimiliki oleh user tanpa sepengetahuan user. Penyerang dapat memanfaatkan ini dengan membuat sebuah tombol untuk mengirim request jahat ke aplikasi. csrf_token menangkal ini dengan membuat sebuah token yang nantinya nilai token ini akan dibandingkan dengan nilai token saat user mengirim request.

## 5.

### 

## 6.

### Tidak ada

