import re

def extract_iocs(file_path):
    with open(file_path, 'r', errors='ignore') as f:
        data = f.read()

    ips = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', data)
    domains = re.findall(r'\b[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', data)
    urls = re.findall(r'https?://[^\s]+', data)

    print(set(ips), set(domains), set(urls))

if __name__ == "__main__":
    extract_iocs("artifacts/headers.txt")
