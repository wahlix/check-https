import requests

def check_https(url):
    # Om användaren inte inkluderade "http://" eller "https://", lägger vi till det
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url
    
    try:
        response = requests.get(url, timeout=5)
        # Kontrollera om den slutliga URL:en använder HTTPS
        if response.url.startswith('https://'):
            print(f"Webbplatsen {url} använder HTTPS.")
        else:
            print(f"Webbplatsen {url} använder INTE HTTPS.")
    except requests.exceptions.RequestException as e:
        print(f"Fel vid åtkomst till {url}: {e}")

# Be användaren mata in en webbadress
user_input = input("Ange webbadressen som ska testas (utan 'http://' eller 'https://'): ")
check_https(user_input)
