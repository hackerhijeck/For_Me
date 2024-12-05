import requests
import argparse
from colorama import init, Fore
from openpyxl import Workbook
import pyfiglet
import time
import re

ascii_banner = pyfiglet.figlet_format("Head3rs")
print(ascii_banner)
print("......................................................................")
print("|              For help -h         Designed by hackerhijeck | v1.0   |")
print("......................................................................")
print("")
# Initialize colorama module
init(autoreset=True)

def get_security_headers(domain):
    if not re.match(r'^https?://', domain):
        domain = f'https://{domain}'
    try:
        response = requests.get(domain)
        if response.status_code == 200:
            security_headers = {
                'Feature-Policy': response.headers.get('Feature-Policy'),
                'Referrer-Policy': response.headers.get('Referrer-Policy'),
                'X-Frame-Options': response.headers.get('X-Frame-Options'),
                'X-XSS-Protection': response.headers.get('X-XSS-Protection'),
                'X-Content-Type-Options': response.headers.get('X-Content-Type-Options'),
                'Content-Security-Policy': response.headers.get('Content-Security-Policy'),
                'Strict-Transport-Security': response.headers.get('Strict-Transport-Security')
            }
            return security_headers
        else:
            return f"Failed to fetch headers. Status code: {response.status_code}"
    except requests.RequestException as e:
        return f"Request exception: {str(e)}"

def check_vulnerability(headers):
    vulnerabilities = {}
    for header, value in headers.items():
        time.sleep(1.5)
        print(f"Checking: {header} \u2014\u2014", end=" ")
        if value is None:
            vulnerabilities[header] = 1
            print(f"{Fore.RED}Vulnerable")
        else:
            vulnerabilities[header] = 0
            print(f"{Fore.GREEN}Not Vulnerable")
    return vulnerabilities

def generate_excel(headers, output_filename):
    workbook = Workbook()
    worksheet = workbook.active

    # Set headers in Excel
    worksheet['A1'] = "S.L No"
    worksheet['B1'] = "Security Headers"
    worksheet['C1'] = "Vulnerable / Not Vulnerable"

    # Excel file with data
    for index, (header, status) in enumerate(headers.items(), start=2):
        worksheet[f'A{index}'] = index - 1
        worksheet[f'B{index}'] = header
        worksheet[f'C{index}'] = "Vulnerable" if status else "Not Vulnerable"

    return workbook

def main():
    parser = argparse.ArgumentParser(description="Fetch security headers of a website")
    parser.add_argument("-d", "--domain", help="Checking headers for a Domain", required=True)
    parser.add_argument("-sec", "--security", help="Fetching security headers", action="store_true")
    parser.add_argument("-o", "--output", help="Output filename for .xlsx")
    args = parser.parse_args()

    if not re.match(r'^https?://', args.domain):
        args.domain = f'https://{args.domain}'

    headers = get_security_headers(args.domain)
    print_headers = True

    if isinstance(headers, dict):
        if args.output:
            vulnerabilities = check_vulnerability(headers)
            output_filename = args.output or f"{args.domain.split('//')[1]}_security_headers.xlsx"
            workbook = generate_excel(vulnerabilities, output_filename)
            workbook.save(output_filename)
            print_headers = False
            print(f"{Fore.GREEN}File Successfully output.")

    if print_headers:
        for header, status in headers.items():
            print(f"Checking: {header} \u2014\u2014", end=" ")
            if status is None:
                print(f"{Fore.RED}Vulnerable")
            else:
                print(f"{Fore.GREEN}Not Vulnerable")

    if not args.output:
        print("Security header checks completed.")

if __name__ == "__main__":
    main()
