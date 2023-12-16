package main

import (
	"bufio"
	"fmt"
	"net/http"
	"os"
	"sync"
	"time"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Usage: subfinder <domain>")
		os.Exit(1)
	}

	domain := os.Args[1]
	subdomains := make(chan string)
	var wg sync.WaitGroup

	// Read common subdomains from a file
	file, err := os.Open("subdomains.txt")
	if err != nil {
		fmt.Println("Error reading subdomains file:", err)
		os.Exit(1)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		wg.Add(1)
		go checkSubdomain(domain, scanner.Text(), subdomains, &wg)
	}

	go func() {
		wg.Wait()
		close(subdomains)
	}()

	for subdomain := range subdomains {
		fmt.Println(subdomain)
	}
}

func checkSubdomain(domain, subdomain string, subdomains chan string, wg *sync.WaitGroup) {
	defer wg.Done()
	url := fmt.Sprintf("http://%s.%s", subdomain, domain)
	client := http.Client{
		Timeout: 2 * time.Second,
	}
	resp, err := client.Get(url)
	if err == nil && resp.StatusCode < 400 {
		subdomains <- subdomain
	}

	// You can add additional checks or validation here if needed
}

