import os:

Mengimpor modul os yang menyediakan fungsi untuk berinteraksi dengan sistem operasi, seperti membersihkan layar terminal.
def selection_sort_asc(arr)::

Mendefinisikan fungsi selection_sort_asc yang menerima satu parameter arr, yaitu array yang akan diurutkan.
os.system("clear"):

Memanggil perintah clear untuk membersihkan layar terminal agar tampilan lebih bersih setiap kali proses pengurutan berjalan.
n = len(arr):

Menghitung panjang array arr dan menyimpannya dalam variabel n.
print("Array awal:", arr, "\n"):

Menampilkan array awal sebelum proses pengurutan dimulai.
for i in range(n)::

Looping dari elemen pertama hingga elemen terakhir dalam array. Variabel i adalah indeks elemen yang sedang diproses.
min_idx = i:

Menginisialisasi indeks elemen terkecil saat ini dengan nilai i.
for j in range(i+1, n)::

Looping dari elemen setelah elemen i hingga elemen terakhir. Variabel j adalah indeks elemen yang akan dibandingkan dengan elemen pada min_idx.
if arr[j] < arr[min_idx]::

Memeriksa apakah elemen pada indeks j lebih kecil dari elemen pada min_idx.
min_idx = j:

Jika elemen pada indeks j lebih kecil, maka memperbarui min_idx dengan nilai j.
arr[i], arr[min_idx] = arr[min_idx], arr[i]:

Menukar elemen terkecil yang ditemukan dengan elemen pertama yang belum diurutkan.
print(f"Langkah {i+1}: Menukar elemen index {i} dengan elemen index {min_idx}, Array sekarang: {arr}\n"):

Menampilkan informasi tentang langkah pengurutan saat ini, termasuk elemen yang ditukar dan keadaan array setelah penukaran.
kon = input("klik enter >>"):

Menunggu input dari pengguna sebelum melanjutkan ke langkah berikutnya. Hal ini memungkinkan pengguna untuk melihat proses pengurutan langkah demi langkah.
os.system("clear"):

Membersihkan layar terminal setelah proses pengurutan selesai.
print("Array telah diurutkan:", arr):

Menampilkan array yang telah diurutkan.
angka = [64, 25, 15, 12, 22, 11]:

Mendefinisikan array angka yang akan diurutkan.
selection_sort_asc(angka):

Memanggil fungsi selection_sort_asc dengan array angka sebagai argumen untuk mengurutkannya dalam urutan menaik.
