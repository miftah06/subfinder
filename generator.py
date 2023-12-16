import random
import string

def generate_random_subdomains(num_subdomains):
    subdomains = []
    for _ in range(num_subdomains):
        subdomain_length = random.randint(1, 5)  # Ganti batasan panjang subdomain sesuai kebutuhan
        subdomain = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(subdomain_length))
        subdomains.append(subdomain)
    return subdomains

def save_to_file(subdomains, file_path="subdomains.txt"):
    with open(file_path, 'w') as file:
        for subdomain in subdomains:
            file.write(f"{subdomain}\n")  # Ganti dengan domain yang sesuai

if __name__ == "__main__":
    num_subdomains = 100
    subdomains = generate_random_subdomains(num_subdomains)
    save_to_file(subdomains)
    print(f"{num_subdomains} subdomains telah disimpan dalam subdomains.txt")
