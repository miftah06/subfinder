package main

import (
	"bufio"
	"fmt"
	"net/http"
	"os"
	"sync"
)

func main() {
	if len(os.Args) != 3 {
		fmt.Println("Usage: subfinder <domains_file> <subdomains_file>")
		os.Exit(1)
	}

	domainsFile := os.Args[1]
	subdomainsFile := os.Args[2]

	// Baca domain dan subdomain dari file
	domains, err := readLines(domainsFile)
	if err != nil {
		fmt.Println("Error reading domains file:", err)
		os.Exit(1)
	}

	subdomains, err := readLines(subdomainsFile)
	if err != nil {
		fmt.Println("Error reading subdomains file:", err)
		os.Exit(1)
	}

	// Inisialisasi WaitGroup untuk menunggu selesainya semua goroutine
	var wg sync.WaitGroup

	// Pemindaian subdomain
	for _, domain := range domains {
		for _, subdomain := range subdomains {
			wg.Add(1)
			go scanSubdomain(domain, subdomain, &wg)
		}
	}

	// Tunggu selesainya semua goroutine
	wg.Wait()
}

func scanSubdomain(domain, subdomain string, wg *sync.WaitGroup) {
	defer wg.Done()

	// Bentuk URL dengan subdomain
	url := fmt.Sprintf("http://%s.%s", subdomain, domain)

	// Coba kirim permintaan HTTP ke subdomain
	resp, err := http.Get(url)
	if err != nil {
		// Gagal terhubung, subdomain mungkin tidak ada
		return
	}
	defer resp.Body.Close()

	// Periksa status kode untuk menentukan apakah subdomain ada
	if resp.StatusCode != http.StatusNotFound {
		fmt.Printf("Subdomain found: %s\n", url)
	}
}

func readLines(filename string) ([]string, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}
