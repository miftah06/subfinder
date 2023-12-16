import requests
from multiprocessing.dummy import Pool as ThreadPool

def scan_subdomain(domain):
    subdomains = []
    domain_results = []
    with open("subdomains.txt", "r") as subdomain_file:
        subdomains = subdomain_file.read().splitlines()

    for subdomain in subdomains:
        url = f"http://{subdomain}.{domain}"
        result = f"{subdomain}.{domain}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Subdomain found: {url}" + '\n')
                domain_results.append(url)
        except requests.RequestException:
            pass

    with open("output.txt", "w") as output_file:
        for domain_results in result:
            output_file.write(f"{result}" + '\n')
            
    return domain_results

def main():
    domains = []
    with open("domains.txt", "r") as domain_file:
        domains = domain_file.read().splitlines()

    pool = ThreadPool(10)  # You can adjust the number of threads based on your system's capacity
    results = pool.map(scan_subdomain, domains)
    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
