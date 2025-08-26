# Config

## Network Configuration

After installing **Kali Linux** on the Raspberry Pi Zero 2W, the next step is to configure the network so the device can be accessed remotely.  
There are two main options:

1. **Connect to an existing Wi-Fi network**  
   Configure the network interface to automatically join a wireless network already available in the environment.

2. **Set up a Wi-Fi hotspot**  
   Configure the network interface to create its own hotspot, allowing other devices to connect directly to the Raspberry Pi.

### Option 1: Connect to an existing Wi-Fi network

To configure the Raspberry Pi Zero 2W to connect to an existing Wi-Fi network, we use **Netplan** and **Cloud-init**.  

On the visible partition of the microSD card, there is a file called **`network-config`** that must be modified.  
A **template file** has been uploaded to this repository for reference.

Steps:

1. Copy the template content from this repository into the [`network-config`](../templates/network-config) file located on the microSD card.

    ```yaml
    version: 2
    wifis:
    renderer: networkd
    wlan0:
        dhcp4: true
        optional: true
        access-points:
        "WIFI_SSID":
            password: wpa_supplicant(PASSWD)
    ```

2. Make the following modifications:
    - Replace **`WIFI_SSID`** with the SSID of the Wi-Fi network you want the Raspberry Pi to connect to.

    - In the **`password`** field, add the **PSK key** for WPA/WPA2.
    This PSK must be generated from the SSID and the Wi-Fi passphrase.

   To simplify this process, a **Python script** has been provided in this repository.  
   Run the script to generate the PSK and copy the result into the `network-config` file.

   ```sh
   python tools/wpa_supplicant.py
   ```

### Set up a Wi-Fi hotspot (TBD)

## Login and Upgrade

- Login

    ```bash
    ssh kali@"ip"
    ```

⚠️ **Note:** Default password "kali"

- Update and upgrade

    ```bash
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get dist-upgrade
    sudo apt-get autoremove
    ```
