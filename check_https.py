import requests
import ssl
import socket
import certifi
from datetime import datetime, timezone
from OpenSSL import SSL

def check_https(url):
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url
    
    try:
        response = requests.get(url, timeout=5)
        if response.url.startswith('https://'):
            print(f"Webbplatsen {url} använder HTTPS.")
            check_ssl_certificate(response.url)
        else:
            print(f"Webbplatsen {url} använder INTE HTTPS.")
    except requests.exceptions.RequestException as e:
        print(f"Fel vid åtkomst till {url}: {e}")

def check_ssl_certificate(url):
    hostname = url.split("://")[1].split("/")[0]
    port = 443

    try:
        context = SSL.Context(SSL.TLS_CLIENT_METHOD)
        context.load_verify_locations(certifi.where())
        
        connection = socket.create_connection((hostname, port))
        ssl_connection = SSL.Connection(context, connection)
        ssl_connection.set_tlsext_host_name(hostname.encode())
        ssl_connection.set_connect_state()
        ssl_connection.do_handshake()

        cert = ssl_connection.get_peer_certificate()
        ssl_connection.close()

        # Konvertera datum till timezone-aware objekt och formatera
        start_date = datetime.strptime(cert.get_notBefore().decode('ascii'), '%Y%m%d%H%M%SZ').replace(tzinfo=timezone.utc)
        end_date = datetime.strptime(cert.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ').replace(tzinfo=timezone.utc)
        current_date = datetime.now(timezone.utc)

        # Formaterat datum utan tidszon
        formatted_end_date = end_date.strftime('%Y-%m-%d %H:%M:%S')

        if current_date < start_date:
            print(f"Certifikatet för {hostname} är inte giltigt än. Det blir giltigt från: {start_date}")
        elif current_date > end_date:
            print(f"Certifikatet för {hostname} har gått ut. Det gick ut: {formatted_end_date}")
        else:
            print(f"Certifikatet för {hostname} är giltigt. Det går ut: {formatted_end_date}")

        # Utfärdare - bättre formatering
        issuer = cert.get_issuer()
        issuer_info = f"/C={issuer.countryName}, O={issuer.organizationName}, CN={issuer.commonName}"
        print(f"Utfärdare: {issuer_info}")

    except Exception as e:
        print(f"Kunde inte kontrollera SSL-certifikatet för {hostname}:{port}: {e}")

user_input = input("Ange webbadressen som ska testas (utan 'http://' eller 'https://'): ")
check_https(user_input)
