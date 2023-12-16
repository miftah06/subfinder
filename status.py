import subprocess

def get_dns_info(hostname):
    try:
        # Scanning CNAME
        cname_result = subprocess.check_output(['nslookup', '-type=CNAME', hostname], universal_newlines=True)
        cname_values = [line.split(':')[-1].strip() for line in cname_result.splitlines() if 'canonical name' in line.lower()]
    except subprocess.CalledProcessError:
        cname_values = None

    try:
        # Scanning IPv4
        ipv4_result = subprocess.check_output(['nslookup', '-type=A', hostname], universal_newlines=True)
        ipv4_addresses = [line.split(':')[-1].strip() for line in ipv4_result.splitlines() if 'address' in line.lower()]
    except subprocess.CalledProcessError:
        ipv4_addresses = None

    try:
        # Scanning IPv6
        ipv6_result = subprocess.check_output(['nslookup', '-type=AAAA', hostname], universal_newlines=True)
        ipv6_addresses = [line.split(':')[-1].strip() for line in ipv6_result.splitlines() if 'address' in line.lower()]
    except subprocess.CalledProcessError:
        ipv6_addresses = None

    return cname_values, ipv4_addresses, ipv6_addresses

def bulk_dns_info(file_path, output_file="scan_result.txt"):
    with open(file_path, 'r') as file:
        urls = file.read().splitlines()

    with open(output_file, 'w') as output:
        for url in urls:
            hostname = url.replace("https://", "").split("/")[0]
            cname_values, ipv4_addresses, ipv6_addresses = get_dns_info(hostname)

            result_line = f"{url}: CNAME {cname_values}, IPv4 {ipv4_addresses}, IPv6 {ipv6_addresses}\n"
            output.write(result_line)
            print(result_line)

if __name__ == "__main__":
    file_path = "hasil.txt"  # Ganti dengan path file yang berisi daftar URL
    bulk_dns_info(file_path)
