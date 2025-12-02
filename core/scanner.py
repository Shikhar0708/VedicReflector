# core/scanner.py

import requests
from urllib.parse import urlencode, urlparse
from core.payloads import PAYLOADS

MARKER = "VEDICXSS"

def send_request(url, method, data=None):
    try:
        if method == "get":
            resp = requests.get(url, params=data, timeout=10, verify=False)
        else:
            resp = requests.post(url, data=data, timeout=10, verify=False)
        return resp.text
    except:
        return ""


def check_reflection(body, payload):
    """
    Check if unencoded payload appeared
    """
    if MARKER not in body:
        return False

    encoded = "&lt;" in body or "&gt;" in body

    return not encoded


def test_form(form):
    vulns = {}

    for field in form["inputs"]:
        vulns[field] = []
        for p_name, payload in PAYLOADS.items():

            # prepare form
            data = {i: "test" for i in form["inputs"]}
            data[field] = payload

            body = send_request(form["action"], form["method"], data)

            if check_reflection(body, payload):
                vulns[field].append(p_name)

    # cleanup
    return {k: v for k, v in vulns.items() if v}


def test_query_params(url):
    from core.extractor import extract_query_params

    parsed = urlparse(url)
    base = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

    params = extract_query_params(url)
    vulns = {}

    for key in params:
        vulns[key] = []
        for p_name, payload in PAYLOADS.items():

            test_params = {k: (payload if k == key else "test") for k in params}
            test_url = base + "?" + urlencode(test_params)

            body = send_request(test_url, "get")

            if check_reflection(body, payload):
                vulns[key].append(p_name)

    return {k: v for k, v in vulns.items() if v}
