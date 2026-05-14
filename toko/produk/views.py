from django.shortcuts import render

produk_list = [
    {
        'id': 1,
        'nama': 'Laptop',
        'harga': 'Rp 8.000.000',
        'deskripsi': 'Laptop untuk kebutuhan kuliah dan kerja'
    },
    {
        'id': 2,
        'nama': 'Smartphone',
        'harga': 'Rp 4.000.000',
        'deskripsi': 'Smartphone dengan kamera berkualitas'
    },
    {
        'id': 3,
        'nama': 'Headset',
        'harga': 'Rp 500.000',
        'deskripsi': 'Headset gaming dengan suara jernih'
    },
]

def home(request):
    return render(request, 'produk/home.html')

def daftar_produk(request):
    context = {
        'produk': produk_list
    }

    return render(request, 'produk/daftar_produk.html', context)

def detail_produk(request, id):
    produk = None

    for p in produk_list:
        if p['id'] == id:
            produk = p
            break

    context = {
        'produk': produk
    }

    return render(request, 'produk/detail_produk.html', context)

def kontak(request):
    return render(request, 'produk/kontak.html')