package main

import (
	"bufio"
	"fmt"
	"net"
	"net/http"
	"os"
	"strings"
	"sync"
)

func getNSRecords(domain string) []string {
	nsRecords := []string{"ns1", "ns2", "ns3"}
	var nsIPs []string

	for _, ns := range nsRecords {
		nsIP, err := lookupNS(domain, ns)
		if err == nil {
			nsIPs = append(nsIPs, nsIP)
		}
	}

	return nsIPs
}

func lookupNS(domain string, ns string) (string, error) {
	nsAddress, err := lookupAddress(fmt.Sprintf("%s.%s", ns, domain))
	if err != nil {
		return "", err
	}
	return nsAddress, nil
}

func lookupAddress(host string) (string, error) {
	ips, err := net.LookupHost(host)
	if err != nil {
		return "", err
	}
	return ips[0], nil
}

func scanSubdomains(domain string, output chan string, wg *sync.WaitGroup) {
	defer wg.Done()

	subdomains, err := readLines("subdomains.txt")
	if err != nil {
		fmt.Println("Error reading subdomains:", err)
		return
	}

	for _, subdomain := range subdomains {
		url := fmt.Sprintf("http://%s.%s", subdomain, domain)
		resp, err := http.Get(url)
		if err == nil && resp.StatusCode == 200 {
			nsRecords := getNSRecords(domain)
			output <- fmt.Sprintf("Subdomain found: %s\nNS Records: %s\n\n", url, strings.Join(nsRecords, ", "))
		}
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

func main() {
	domains, err := readLines("domains.txt")
	if err != nil {
		fmt.Println("Error reading domains:", err)
		return
	}

	var wg sync.WaitGroup
	output := make(chan string)

	for _, domain := range domains {
		wg.Add(1)
		go scanSubdomains(domain, output, &wg)
	}

	go func() {
		wg.Wait()
		close(output)
	}()

	resultFile, err := os.Create("output.txt")
	if err != nil {
		fmt.Println("Error creating output file:", err)
		return
	}
	defer resultFile.Close()

	for result := range output {
		resultFile.WriteString(result)
		fmt.Print(result)
	}
}
