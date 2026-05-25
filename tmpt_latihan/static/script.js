// 1. Tunggu sampai tombol diklik
document.getElementById('btnKirim').addEventListener('click', async () => {
    
    // 2. Ambil elemen input dan teks di dalamnya
    const inputElemen = document.getElementById('inputTeks');
    const teksUser = inputElemen.value;

    // Validasi singkat kalau input kosong
    if (!teksUser) {
        alert('Ketik sesuatu dulu ya!');
        return;
    }

    // Ubah teks sementara jadi 'Loading...' biar interaktif
    document.getElementById('tempatHasil').innerText = "Sedang diproses Python...";

    try {
        // 3. Kirim data ke Python (Endpoint: /proses-data)
        const response = await fetch('/proses-data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ teks: teksUser }) // Data diubah ke format JSON string
        });

        // 4. Ambil respons balasan dari Python
        const dataBalasan = await response.json();

        // 5. Tampilkan hasil olahan Python ke tag HTML <p id="tempatHasil">
        document.getElementById('tempatHasil').innerText = dataBalasan.hasil;

    } catch (error) {
        console.error("Error saat menghubungi Python:", error);
        document.getElementById('tempatHasil').innerText = "Gagal terhubung ke server.";
    }
});