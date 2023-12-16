import socket
import requests
import numpy as np
import tornado.gen
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient, HTTPRequest

# Fungsi untuk mendapatkan daftar URL dari file teks
def get_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

# Fungsi untuk mendapatkan alamat IP dari nama host menggunakan dnspython
def resolve_hostname(hostname):
    try:
        result = socket.gethostbyname(hostname)
        return result
    except socket.error as e:
        print(f"Error resolving {hostname}: {e}")
        return None

# Fungsi untuk melakukan HTTP request dan mendapatkan status code dan server DNS
@tornado.gen.coroutine
def fetch_url(url):
    hostname = url.replace("http://", "").split("/")[0]
    
    ip_address = resolve_hostname(hostname)
    if ip_address:
        try:
            response = yield AsyncHTTPClient().fetch(HTTPRequest(url, connect_timeout=10, request_timeout=20))
            status_code = response.code
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            status_code = None
    else:
        status_code = None
    
    raise tornado.gen.Return((url, ip_address, status_code))

# Fungsi utama untuk melakukan bulk HTTP status code check dengan informasi server DNS
def bulk_http_status_check(file_path):
    urls = get_urls_from_file(file_path)
    
    # Menggunakan Tornado IOLoop untuk operasi asynchronous
    loop = IOLoop.current()
    
    # Menggunakan numpy untuk shuffle daftar URL agar proses menjadi acak
    np.random.shuffle(urls)
    
    # Melakukan resolve hostname dan HTTP request untuk setiap URL secara asynchronous
    futures = [fetch_url(f"http://{url}") for url in urls]

    # Menunggu semua proses selesai
    results = loop.run_sync(lambda: tornado.gen.multi(futures))

    # Menampilkan hasil
    for url, ip_address, status_code in results:
        print(f"{url}: DNS {ip_address}, Status Code {status_code}")

if __name__ == "__main__":
    file_path = "hasil.txt"  # Ganti dengan path file yang berisi daftar URL
    bulk_http_status_check(file_path)
