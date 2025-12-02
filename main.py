# main.py

import sys
import requests
from core.extractor import extract_forms
from core.scanner import test_form, test_query_params
from core.reporter import print_form_results, print_query_results
from core.banner import   show_banner
from core.utils import blue, yellow, red, green

show_banner()
requests.packages.urllib3.disable_warnings()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <url>")
        return

    url = sys.argv[1]
    print(green(f"[+] Target: {url}"))

    # Download page
    try:
        resp = requests.get(url, timeout=10, verify=False)
    except Exception as e:
        print(red("[!] Could not connect:", e))
        return

    html = resp.text

    # Query parameter testing
    q_results = test_query_params(url)
    print_query_results(q_results)

    # Form extraction + testing
    forms = extract_forms(html, url)
    print(yellow(f"\n[+] Found {len(forms)} form(s)"))

    for form in forms:
        result = test_form(form)
        print_form_results(form["action"], result)


if __name__ == "__main__":
    main()
