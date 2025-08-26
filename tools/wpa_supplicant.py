'''
wpa_supplicant
'''
import hashlib
import binascii

def wpa_passphrase(ssid:str, passphrase:str) -> str:
    '''
    Genera una clave precompartida (PSK) para WPA/WPA2 a partir de un SSID y una Passphrase.
    '''
    psk = hashlib.pbkdf2_hmac(
        'sha1',
        passphrase.encode('utf-8'),
        ssid.encode('utf-8'),
        4096,
        32
    )
    return binascii.hexlify(psk).decode('utf-8')

if __name__ == "__main__":
    wifi_ssid: str = input("SSID: ")
    passwd: str = input("Passphrase: ")
    print("PSK:", wpa_passphrase(ssid=wifi_ssid, passphrase=passwd))
