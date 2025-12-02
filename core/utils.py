# core/utils.py

from urllib.parse import urljoin, urlparse

def normalize_url(base, link):
    """
    Converts relative links to absolute URLs.
    """
    return urljoin(base, link)

def same_domain(url1, url2):
    """
    Returns True if two URLs share the same domain.
    Used later for the crawler.
    """
    d1 = urlparse(url1).netloc
    d2 = urlparse(url2).netloc
    return d1 == d2

def clean_url(url):
    """
    Removes fragments (#section) from URL.
    Keeps URLs consistent during crawling.
    """
    parsed = urlparse(url)
    cleaned = parsed._replace(fragment="").geturl()
    return cleaned

def unique_list(items):
    """
    Returns a list with duplicates removed while preserving order.
    """
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

# core/utils.py

from colorama import Fore, Style, init
init(autoreset=True)

def blue(text):
    return f"{Fore.CYAN}{text}{Style.RESET_ALL}"

def yellow(text):
    return f"{Fore.YELLOW}{text}{Style.RESET_ALL}"

def red(text):
    return f"{Fore.RED}{text}{Style.RESET_ALL}"

def green(text):
    return f"{Fore.GREEN}{text}{Style.RESET_ALL}"
