import urllib.request
import argparse
from tabulate import tabulate

def get_headers(url):
    if not url.startswith('http://') and not url.startswith('https://'):
        url = f'https://{url}'
    try:
        response = urllib.request.urlopen(url)
        return response.headers
    except Exception as e:
        return f"Error occurred: {str(e)}"

def extract_header(headers, header_name):
    return headers[header_name] if header_name in headers else "Not found"

def main(domain):
    headers = get_headers(domain)

    server_header = extract_header(headers, 'Server')
    powered_by_header = extract_header(headers, 'X-Powered-By')
    generator_header = extract_header(headers, 'X-Generator')

    table_data = [
        ["Header", "Value"],
        ["Server", server_header],
        ["X-Powered-By", powered_by_header],
        ["X-Generator", generator_header]
    ]

    print(f"Domain: {domain}")
    print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch headers for a domain")
    parser.add_argument("-u","--url", help="Domain to fetch headers", required=True)
    args = parser.parse_args()

    main(args.url)