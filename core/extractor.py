# core/extractor.py

from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, parse_qs

def extract_forms(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    forms = []

    for form in soup.find_all("form"):
        action = form.get("action") or base_url
        method = (form.get("method") or "get").lower()

        inputs = []
        for inp in form.find_all("input"):
            name = inp.get("name")
            if not name:
                continue
            inputs.append(name)

        if inputs:
            forms.append({
                "method": method,
                "action": urljoin(base_url, action),
                "inputs": inputs
            })

    return forms


def extract_query_params(url):
    parsed = urlparse(url)
    if not parsed.query:
        return {}
    return parse_qs(parsed.query)
