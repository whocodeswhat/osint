import requests

def check_profile(platform_name, url):
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            return f"{platform_name}: FOUND"
        elif response.status_code == 404:
            return f"{platform_name}: NOT FOUND"
        else:
            return f"{platform_name}: ERROR ({response.status_code})"

    except requests.RequestException:
        return f"{platform_name}: CONNECTION ERROR"