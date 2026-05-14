# Tugas 3 Praktikum PPL - Website Katalog Sederhana (NazTech)

## Identitas
- Nama: Muhammad Nazlul Ramadhyan
- NIM: 2308107010036

---

## Penjelasan Singkat Program
Program ini merupakan sebuah website katalog produk sederhana bertema toko elektronik bernama yang dibangun menggunakan framework Django dan Tailwind CSS. Website ini tidak menggunakan database relasional, melainkan menggunakan hardcoded data berupa list dictionary pada file `views.py`.

Website dirancang dengan tampilan modern dan responsive menggunakan Tailwind CSS CDN serta tambahan icon dari Font Awesome.

---

## Fitur Website

### Homepage (/)
Menampilkan halaman utama berupa hero section sederhana yang berisi deskripsi singkat website serta tombol navigasi menuju halaman produk dan kontak.

### Daftar Produk (/produk/)
Menampilkan daftar produk elektronik dalam bentuk grid card dengan desain modern dan responsive. Setiap produk memiliki nama, harga, icon produk, dan tombol menuju halaman detail.

### Detail Produk (/produk/<id>/)
Menampilkan detail produk berdasarkan ID, lengkap dengan nama produk, harga, deskripsi, dan tampilan UI yang lebih fokus terhadap informasi produk.

### Kontak (/kontak/)
Menampilkan informasi kontak sederhana seperti email, nomor telepon, dan alamat toko.

---

## Teknologi yang Digunakan
- Python
- Django
- Tailwind CSS
- Font Awesome
