import requests
from multiprocessing.dummy import Pool as ThreadPool

def scan_subdomain(domain):
    subdomains = []
    domain_results = []

    with open("subdomains.txt", "r") as subdomain_file:
        subdomains = subdomain_file.read().splitlines()

    for subdomain in subdomains:
        url = f"https://{subdomain}.{domain}"
        try:
            response = requests.get(url)

            if response.status_code in [200, 301, 400, 409, 502, 401]:
                server_info = response.headers.get('Server', 'N/A')
                print(f"Subdomain found: {url} | Status Code: {response.status_code} | Server: {server_info}\n")
                domain_results.append(url)

        except requests.RequestException:
            pass

    with open("output.txt", "w") as output_file:
        for result in domain_results:
            output_file.write(f"{result}\n")
            
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
