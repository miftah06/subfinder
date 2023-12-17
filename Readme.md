# Subdomain Scanner

## Deskripsi
Proyek ini adalah alat sederhana untuk melakukan pemindaian subdomain menggunakan Golang dan Python. Proyek ini terdiri dari dua skrip utama:
- `subfinder.go`: Skrip Golang untuk membaca daftar subdomain dari file `subdomains.txt` dan `domains.txt`, menggabungkannya dengan domain utama yang diinputkan oleh pengguna, dan kemudian memindai setiap subdomain.
- `subfinder.py`: Skrip Python yang sama tapi menggunakan python untuk memproses hasil pemindaian subdomain.
- untuk `hasil.txt`: scan dulu menggunakan https://www.ipvoid.com/domain-extractor/ lalu cantumkan hasil ke hasil.txt.

6. Ikuti instruksi untuk memasukkan domain utama.

7. Tunggu hingga pemindaian selesai dan periksa hasilnya.

## Instalasi
Pastikan Anda telah menginstal Golang di sistem Anda. Jika belum, Anda dapat mengunduh dan menginstalnya dari [situs resmi Golang](https://golang.org/dl/).

    ```Pada TERMUX
	pkg install python3
    pkg install golang
	apt install python-requests
	pip3 install httpx
	pip3 install beautifulsoup4
	pip3 install requests

	atau 
	pip3 install -r requirements.txt
	python3 subfinder.py	
    ```

## Cara Penggunaan KHUSUS PC
1. Pastikan Anda telah menginstal Golang dan Python di sistem Anda.

2. Clone repositori ini:
    ```bash
    git clone https://github.com/miftah06/subfinder.git
    ```

3. Ganti direktori ke proyek ini:
    ```bash
    cd subfinder
    ```

4. Ubah file `subdomains.txt` dan `list.txt` sesuai kebutuhan Anda.

5. Jalankan skrip Golang:
    ```bash
    apt install golang -y
	go mod init subdomain_scanner
	go mod tidy
	go build subfinder.go
	./subfinder domains.txt subdomains.txt
    go run subfinder.go
    ```
	
## Scanning

```python untuk win64
python3 status.py	
    
```

## Membuat subdomain

```python untuk win64
python3 generator.py	
    
```

## perhatian buat scan!
untuk scanning scan dulu menggunakan https://www.ipvoid.com/domain-extractor/ lalu cantumkan hasil ke hasil.txt.

## Kontribusi
Jika Anda menemui masalah atau memiliki ide perbaikan, jangan ragu untuk membuka "issues" atau mengajukan "pull requests".

## Catatan
- Proyek ini hanya sebagai contoh dan mungkin perlu disesuaikan dengan kebutuhan spesifik Anda.
- Pastikan untuk menyesuaikan skrip dan file dengan keamanan terbaik dan mematuhi hukum setempat saat melakukan pemindaian subdomain.
