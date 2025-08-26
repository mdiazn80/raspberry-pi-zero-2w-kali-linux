# raspberry-pi-zero-2w-kali-linux

## 📌 About the Project

This repository provides a **step-by-step guide to installing and configuring Kali Linux on a Raspberry Pi Zero 2 W**.  
The goal is to create a lightweight, portable, and affordable **cybersecurity lab** for **ethical hacking, pentesting, and learning**.  

⚠️ **Disclaimer:** This project is for **educational purposes only**. Use it responsibly in controlled environments. The misuse of these tools may be illegal. The author is not responsible for any misuse of this project.

## 🚀 Features

- Step-by-step installation of Kali Linux ARM.  
- Initial setup: SSH, VNC, and network configuration.  
- Performance optimization for the Pi Zero 2 W.  
- Installation of essential pentesting tools.  
- Example use cases:
  - WiFi auditing (with external USB WiFi adapter).  
  - Network scanning with `nmap` / `masscan`.  
  - Lightweight honeypots.  
  - Portable sniffer.  
  - BadUSB (HID attacks).  

## Requirements

### Hardware

- [Raspberry PI Zero 2W](https://www.amazon.es/dp/B09KLVX4RT?ref=ppx_yo2ov_dt_b_fed_asin_title)

- [Kingston Canvas Select Plus microSD Card, SDCS2/128GB Class 10 with SD Adapter, Lifetime Warranty with Manufacturer.](https://www.amazon.es/dp/B07YGZ7JD5?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1)

- OPTIONAL [GeeekPi USB Dongle Expansion Card with Case for Raspberry Pi Zero/Zero W, both front and back sides can be inserted](https://www.amazon.es/dp/B098JP79ZX?ref=ppx_yo2ov_dt_b_fed_asin_title)

- OPTIONAL [GeeekPi for Raspberry Pi Zero/Zero W Box, with 20 Pin GPIO Header, OTG Cable, Switch Cable, HDMI Adapter, Heat Sink and Screwdriver (Transparent)](https://www.amazon.es/-/en/gp/product/B07MGFRHHR/ref=ewc_pr_img_1?smid=A187Y4UVM6ZA0X&psc=1)

- Optional: External WiFi adapter with monitor mode support

### Images

<img src="images/hardware/raspberry.jpg" alt="drawing" width="200"/>
<img src="images/hardware/box.jpg" alt="drawing" width="200"/>
<img src="images/hardware/usb.jpg" alt="drawing" width="200"/>
<img src="images/hardware/microsd.jpg" alt="drawing" width="200"/>
<img src="images/hardware/boxlight.png" alt="drawing" width="200"/>
<img src="images/hardware/boxdark.png" alt="drawing" width="200"/>

### Software

- [Raspberry Imager](https://www.raspberrypi.com/software/)
- [Kali Linux](https://www.kali.org)
- [Cloud Init](https://cloudinit.readthedocs.io/en/latest/)
- [Netplan](https://netplan.io/)

## Installation

- [Install](./docs/install.md)
- [Login](./docs/login.md)
- [Config and update](./docs/config.md)

## Projects

- [Install hotspot (TBD)](./docs/hotspot.md)
