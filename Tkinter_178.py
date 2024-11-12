import tkinter as tk  # Import the tkinter module for creating GUI applications
from tkinter import messagebox  # Import the messagebox module for showing pop-up dialogs

# Fungsi untuk memvalidasi input dan menampilkan hasil prediksi
def hasil_prediksi():
    try:
        # Loop melalui semua entry widget untuk validasi input
        for entry in entries: 
            nilai = int(entry.get())  # Mengambil nilai dari setiap entry widget dan mengonversinya ke integer
            # Mengecek apakah nilai berada dalam rentang yang valid (0-100)
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")  # Menaikkan kesalahan jika nilai tidak valid
        # Menampilkan hasil prediksi jika input valid
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi", fg="black")  # Menampilkan teks hasil prediksi dengan warna hitam
    except ValueError:  # Menangani kesalahan jika input tidak valid
        # Menampilkan pesan error menggunakan messagebox jika terjadi kesalahan input
        messagebox.showerror("Kesalahan Input", "Pastikan semua input adalah angka antara 0 dan 100.")  # Pesan error yang akan ditampilkan

# Pengaturan jendela utama Tkinter
root = tk.Tk()  # Membuat objek jendela utama Tkinter
root.title("Aplikasi Prediksi Prodi Pilihan")  # Menetapkan judul jendela utama aplikasi
root.geometry("500x600")  # Menetapkan ukuran jendela aplikasi (lebar 500px, tinggi 600px)
root.configure(bg="#FFB6C1")  # Mengubah warna latar belakang jendela utama menjadi warna pink muda (hex code #FFB6C1)


# Label Judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Times New Roman", 16), bg="#E6E6FA", fg="black")  
# Membuat label untuk judul aplikasi dengan teks "Aplikasi Prediksi Prodi Pilihan", font Times New Roman ukuran 16, 
# latar belakang warna lavender (#E6E6FA), dan teks berwarna hitam.
judul_label.pack(pady=20)  
# Menampilkan label judul di jendela utama dengan jarak vertikal 20px (pady) agar tidak terlalu rapat dengan elemen lain.

# Frame untuk memasukkan nilai
frame_input = tk.Frame(root, bg="#E6E6FA")  # Warna latar belakang frame
# Membuat sebuah frame yang berfungsi untuk menampung elemen input (seperti entry) dengan latar belakang warna lavender (#E6E6FA)
frame_input.pack(pady=10)  
# Menampilkan frame di jendela utama dengan jarak vertikal 10px agar terlihat terpisah dari elemen lain

# Membuat entri untuk nilai mata pelajaran
entries = []  # Membuat list kosong untuk menyimpan widget entri

for i in range(10):  # 10 mata pelajaran
    # Membuat label untuk setiap mata pelajaran, dengan teks yang menunjukkan "Nilai Mata Pelajaran 1", "Nilai Mata Pelajaran 2", dll.
    tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i+1}:", font=("Times New Roman", 12), bg="#d9f2e6", fg="black").grid(row=i, column=0, padx=10, pady=5)
    # Membuat entry widget untuk memasukkan nilai, dengan lebar 10 karakter dan gaya font "Times New Roman" ukuran 12
    entry = tk.Entry(frame_input, width=10, font=("Times New Roman", 12), bg="#E6E6FA", fg="black")  # Warna latar dan teks entri
    # Menempatkan entry pada grid di baris yang sesuai (baris i) dan kolom 1, dengan padding horizontal (padx) 10 dan padding vertikal (pady) 5
    entry.grid(row=i, column=1, padx=10, pady=5)
    # Menambahkan entry ke dalam list 'entries' agar bisa diakses untuk validasi input nantinya
    entries.append(entry)


# Tombol untuk prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Times New Roman", 12), bg="#FFFDD0", fg="black")  
# Membuat tombol dengan teks "Hasil Prediksi", yang saat ditekan akan memanggil fungsi hasil_prediksi
# Tombol ini menggunakan font "Times New Roman" ukuran 12, latar belakang warna krem (#FFFDD0), dan teks berwarna hitam
prediksi_button.pack(pady=30)  
# Menampilkan tombol pada jendela utama dengan jarak vertikal 30px (pady) untuk memberi ruang di sekitar tombol

# Label untuk menampilkan hasil
hasil_label = tk.Label(root, text="", font=("Times New Roman", 14, "italic", "bold"), fg="black", bg="#ADD8E6")  
# Membuat label kosong untuk menampilkan hasil prediksi setelah pengguna memasukkan nilai
# Label ini menggunakan font "Times New Roman" ukuran 14 dengan gaya italic dan bold, teks berwarna hitam, dan latar belakang biru muda (#ADD8E6)
hasil_label.pack(pady=20)  
# Menampilkan label di jendela utama dengan jarak vertikal 20px (pady) agar tidak terlalu rapat dengan elemen lain

# Menjalankan loop utama
root.mainloop()  
# Menjalankan loop utama Tkinter untuk menunggu dan merespons interaksi pengguna (seperti klik tombol dan input)
