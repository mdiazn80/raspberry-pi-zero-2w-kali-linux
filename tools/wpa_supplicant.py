#!/usr/bin/env python3
import hashlib, binascii

def wpa_passphrase(ssid: str, passphrase: str) -> str:
    # Derivación PBKDF2-HMAC-SHA1, 4096 iteraciones, clave de 256 bits
    psk = hashlib.pbkdf2_hmac(
        'sha1',
        passphrase.encode('utf-8'),
        ssid.encode('utf-8'),
        4096,
        32
    )
    return binascii.hexlify(psk).decode('utf-8')

if __name__ == "__main__":
    ssid = input("SSID: ")
    passphrase = input("Passphrase: ")
    print("PSK:", wpa_passphrase(ssid, passphrase))