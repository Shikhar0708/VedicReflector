# core/reporter.py

from core.utils import blue, yellow, red, green

def print_form_results(action, results):
    print(blue(f"\n[+] Form: {action}"))

    if not results:
        print(red("    [-] No reflections found."))
        return

    for field, payloads in results.items():
        print(yellow(f"    [!] {field} → {', '.join(payloads)}"))


def print_query_results(results):
    print(blue("\n[+] Query Parameter Testing"))

    if not results:
        print(red("    [-] No reflected parameters."))
        return

    for param, payloads in results.items():
        print(yellow(f"    [!] {param} → {', '.join(payloads)}"))
