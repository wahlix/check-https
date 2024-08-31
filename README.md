# SSL Certificate Checker

## Beskrivning

Detta verktyg är en enkel Python-applikation utvecklad för att kontrollera om en webbplats använder HTTPS och verifiera giltigheten av dess SSL-certifikat. Verktyget kontrollerar om webbplatsen använder HTTPS, samt ger information om certifikatets giltighetsperiod och utfärdare.

Detta projekt skapades som en del av min utbildning till IT-säkerhetsspecialist på [EC Utbildning YH](https://ecutbildning.se/). Syftet var att fördjupa mina kunskaper inom IT-säkerhet och praktiskt tillämpa dem genom utveckling av ett verktyg som kan användas för att säkerställa webbplatsers säkerhet.

## Funktioner

- Kontrollera om en webbplats använder HTTPS.
- Verifiera giltigheten av SSL-certifikatet.
- Visa certifikatets utgångsdatum och utfärdare.

## Installation

För att använda detta verktyg behöver du Python 3 och några Python-bibliotek. Följ dessa steg för att installera nödvändiga beroenden:

1. Klona detta repository:
   ```bash
   git clone https://github.com/ditt-användarnamn/ssl-certificate-checker.git

2. Navigera till projektmappen:
    ```bash
    cd ssl-certificate-checker

3. Installera de nödvändiga Python-biblioteken:
    ```bash
    pip install -r requirements.txt

# Användning

För att köra verktyget, kör följande kommando:

    ```bash
    python check_https.py


När du uppmanas, ange webbadressen som du vill testa utan http:// eller https://. Verktyget kommer att visa om webbplatsen använder HTTPS och ge information om SSL-certifikatet.