from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Tentukan nama file penyimpanan
FILE_CATATAN = "catatan_harian.txt"
FILE_PENGELUARAN = "pengeluaran.txt"

# Fungsi bantuan Python untuk membaca isi file jika file-nya ada
def baca_file(nama_file):
    if os.path.exists(nama_file):
        with open(nama_file, "r", encoding="utf-8") as f:
            return f.readlines()
    return []

@app.route('/', methods=['GET', 'POST'])
def home():
    notifikasi = None
    
    if request.method == 'POST':
        # 1. Ambil data dari input HTML
        tipe_data = request.form.get('tipe_data') # Nilainya: 'catatan' atau 'pengeluaran'
        isi_data = request.form.get('isi_data', '').strip()
        
        if isi_data:
            # 2. LOGIKA PYTHON: Simpan data berdasarkan pilihan user
            if tipe_data == 'catatan':
                # Buka file catatan_harian.txt lalu tulis di baris baru
                with open(FILE_CATATAN, "a", encoding="utf-8") as f:
                    f.write(isi_data + "\n")
                notifikasi = "✅ Catatan harian berhasil disimpan!"
                
            elif tipe_data == 'pengeluaran':
                # Buka file pengeluaran.txt lalu tulis di baris baru
                with open(FILE_PENGELUARAN, "a", encoding="utf-8") as f:
                    f.write(isi_data + "\n")
                notifikasi = "💰 Data pengeluaran berhasil disimpan!"

    # 3. PYTHON MEMBACA SEMUA DATA UNTUK DITAMPILKAN KE WEB
    semua_catatan = baca_file(FILE_CATATAN)
    semua_pengeluaran = baca_file(FILE_PENGELUARAN)
    
    # Kirim semua data ke HTML
    return render_template(
        'index.html', 
        notif=notifikasi, 
        catatan=semua_catatan, 
        pengeluaran=semua_pengeluaran
    )

if __name__ == '__main__':
    app.run(debug=True)