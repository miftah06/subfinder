# Subdomain Scanner

## Deskripsi
Proyek ini adalah alat sederhana untuk melakukan pemindaian subdomain menggunakan Golang dan Python. Proyek ini terdiri dari dua skrip utama:
- `main.go`: Skrip Golang untuk membaca daftar subdomain dari file `subdomains.txt` dan `list.txt`, menggabungkannya dengan domain utama yang diinputkan oleh pengguna, dan kemudian memindai setiap subdomain.
- `process_results.py`: Skrip Python yang digunakan oleh Golang untuk memproses hasil pemindaian subdomain.

## Cara Penggunaan
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
	go mod init subdomain_scanner
	go mod tidy
	go build subfinder.go
	./subfinder domains.txt subdomains.txt
    go run subfinder.go
    ```

6. Ikuti instruksi untuk memasukkan domain utama.

7. Tunggu hingga pemindaian selesai dan periksa hasilnya.

## Instalasi Golang
Pastikan Anda telah menginstal Golang di sistem Anda. Jika belum, Anda dapat mengunduh dan menginstalnya dari [situs resmi Golang](https://golang.org/dl/).

    ```Pada TERMUX
	pkg install python3
    pkg install golang
	apt install python-requests
	pip3 install httpx
	pip3 install beautifulsoup4
	pip3 install requests
	go run subfinder.go domains.txt subdomains.txt

	atau 
	pip3 install -r requirements.txt
	python3 subfinder.py	
    ```
	

## Kontribusi
Jika Anda menemui masalah atau memiliki ide perbaikan, jangan ragu untuk membuka "issues" atau mengajukan "pull requests".

## Catatan
- Proyek ini hanya sebagai contoh dan mungkin perlu disesuaikan dengan kebutuhan spesifik Anda.
- Pastikan untuk menyesuaikan skrip dan file dengan keamanan terbaik dan mematuhi hukum setempat saat melakukan pemindaian subdomain.