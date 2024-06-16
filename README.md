[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/4hPMH1rV)

# API DOCS ZOO & Employees

   berisikan tentang nama nama hewan dan karyawan yang bekerja di kebun binatang

## setup API use get put post delete
   Dalam konteks pengembangan aplikasi web, GET, POST, PUT, dan DELETE adalah metode HTTP yang digunakan untuk mengirim permintaan (request) ke server. Setiap metode HTTP memiliki fungsi dan tujuan yang berbeda. Berikut adalah penjelasan tentang masing-masing metode tersebut:

1. GET
   Fungsi: Mengambil data dari server.
   Kapan Digunakan: Saat Anda ingin membaca atau mengambil sumber daya tanpa memodifikasinya.
 
2. POST
   Fungsi: Mengirim data ke server untuk membuat sumber daya baru.
   Kapan Digunakan: Saat Anda ingin membuat sumber daya baru atau mengirim data ke server untuk pemrosesan.

3. PUT
   Fungsi: Mengirim data ke server untuk memperbarui atau mengganti sumber daya yang ada.
   Kapan Digunakan: Saat Anda ingin memperbarui seluruh sumber daya yang ada di server.
   
4. DELETE
   Fungsi: Menghapus sumber daya dari server.
   Kapan Digunakan: Saat Anda ingin menghapus sumber daya yang ada di server.

5. PATCH
   Fungsi: Mengirim data ke server untuk memperbarui sebagian sumber daya yang ada.
   Kapan Digunakan: Saat Anda ingin memperbarui sebagian dari sumber daya yang ada di server.
## Middleware
   Middleware adalah komponen penting dalam pengembangan aplikasi web yang bertindak sebagai lapisan penghubung antara permintaan klien dan tanggapan server. Middleware memungkinkan Anda untuk memproses permintaan (request) sebelum mencapai handler utama, dan juga memproses tanggapan (response) sebelum dikirim kembali ke klien. Ini memungkinkan untuk menambahkan fungsionalitas seperti autentikasi, logging, pengelolaan sesi, pengaturan CORS, dan lainnya.

 ### Fungsi Middleware
   - Autentikasi dan Otorisasi: Memeriksa apakah pengguna memiliki hak akses yang diperlukan.
   - Logging: Merekam informasi tentang permintaan dan tanggapan untuk tujuan debugging atau analisis.
   - Pengaturan CORS: Mengelola kebijakan Cross-Origin Resource Sharing.
   - Pengelolaan Sesi: Menangani sesi pengguna.
   - Pemrosesan Data: Memproses atau memodifikasi data permintaan atau tanggapan.

## Setup Proyek dengan Pipenv dan Membangun Dockerfile
1. Menginstal Dependensi Menggunakan Pipenv
   - `pip install pipenv`
   Pipenv adalah alat yang membantu mengelola dependensi proyek Python. Ini menggabungkan pip dan virtualenv dalam satu alat. 
   - `pip install --user pipenv`
   memungkinkan Anda untuk menginstal Pipenv di level pengguna, memudahkan pengelolaan dependensi dan virtual environment tanpa memerlukan izin administrator

2. Menginstal Flask
   Flask adalah kerangka kerja web ringan untuk Python.
   - `pipenv install flask`

3. Menginstal Blueprint
   Blueprint adalah ekstensi Flask yang membantu mengorganisir aplikasi Flask Anda ke dalam modul-modul. (route)
   - `pipenv install blueprint`

4. Menginstal Flasgger
   Flasgger adalah ekstensi Flask untuk membuat dokumentasi OpenAPI untuk API Flask Anda.
   - `pipenv install flasgger`

5. Menginstal Gunicorn
   Gunicorn adalah server HTTP WSGI Python untuk UNIX. Ini menggunakan model pekerja pre-fork dan memungkinkan Anda menjalankan aplikasi Flask Anda dalam produksi.
   - `pipenv install gunicorn`

6. Menginstal Coverage
   Coverage.py adalah alat untuk mengukur cakupan kode dari program Python. Ini memantau program Anda, mencatat bagian mana dari kode yang telah dieksekusi.
   - `pipenv install coverage`

7.  - ### Membangun Dockerfile
      Dockerfile adalah dokumen teks yang berisi semua perintah untuk merakit sebuah image. Menggunakan docker build, Anda dapat membuat build otomatis yang menjalankan beberapa instruksi baris perintah secara berturut-turut.

    - ### Membangun Image Docker
      Untuk membangun image Docker, jalankan perintah berikut di direktori yang sama dengan Dockerfile Anda:
    `docker build -t 'nama-image' -f 'Dockerfile' .`
    - ### Menjalankan Kontainer Docker
      Setelah image dibangun, Anda dapat menjalankannya menggunakan:
      `docker run -p 5000:5000 nama-image`
    - ### Membangun dari Shell Script
      Jika Anda memiliki proses build yang didefinisikan dalam shell script (build.sh), Anda dapat memasukkan perintah untuk membangun dan menjalankan image Docker Anda. (disini aku tidak menggunakannya)
      Contoh : 
      -  buat file build.sh dengan isi file :
       `docker build -t nama-image .`
       `docker run -p 5000:5000 nama-image`
      - Menjalankan Script
        Buat script menjadi executable (jika belum), dan kemudian jalankan pada terminal:   
        `chmod +x build.sh`
        `./build.sh`