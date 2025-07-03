# 🛠️ Home Assistant Wi-Fi Onboarding Add-on

A **plug-and-play captive portal** add-on for Home Assistant OS, allowing users to configure Wi-Fi on first boot using a web-based interface.

> ✅ Designed for Raspberry Pi 5 running Home Assistant OS  
> ✅ Uses `wlan0` for hotspot and Wi-Fi switching  
> ✅ No USB adapter required  
> ✅ Works out-of-the-box on first boot  

---

## 🚀 Features

- Starts a Wi-Fi hotspot (`SSID: HomeAssistant-Setup`)
- Serves a local web interface via Flask
- Allows users to scan and select available Wi-Fi networks
- Stores credentials and switches the device to the selected network
- Automatically disables hotspot after successful connection

---

## 🧩 How It Works

1. On first boot, no Wi-Fi is configured.
2. The add-on creates a hotspot using `wlan0` via `hostapd` and `dnsmasq`.
3. A captive portal (Flask) is served at `192.168.4.1` where the user inputs Wi-Fi credentials.
4. The add-on shuts down the hotspot, connects to the selected Wi-Fi, and stores the configuration.

---

## 📦 Installation

### Step 1: Add Repository

In Home Assistant UI:

1. Go to **Settings → Add-ons → Add-on Store**
2. Click **“⋮” → Repositories**
3. Add GitHub repo URL:

https://github.com/DhanushM-IT-Programmer/ha-wifi-onboarding


4. Click **Add**. The add-on will appear in the list.

---

### Step 2: Install & Start

1. Open the add-on: **Wi-Fi Onboarding**
2. Click **Install**
3. Enable:
   - [x] Start on boot
   - [x] Watchdog
4. Click **Start**

---

## 🖥️ Captive Portal Access

Once the hotspot is active:

- Connect your phone/laptop to: `HomeAssistant-Setup`
- Visit: `http://192.168.4.1`
- Enter your Wi-Fi credentials
- The system will switch to your Wi-Fi

---

## 🛑 Notes & Limitations

- This add-on **only works with `wlan0`** (onboard Wi-Fi)
- Do **not use USB Wi-Fi adapters** — they are not supported in this version
- For best results, use on fresh boot without existing Wi-Fi

---

## 📁 File Structure Overview

ha-wifi-onboarding/
├── wifi_onboarding_addon/
│ ├── Dockerfile
│ ├── config.json
│ ├── run.sh
│ ├── app.py
│ ├── hostapd.conf
│ ├── dnsmasq.conf
│ └── www/
│ └── index.html


---

## 🧪 Testing

- Test on fresh install of Home Assistant OS
- Ensure `wlan0` is not already connected
- Check logs via add-on panel for connectivity debug

---

## 🙋‍♂️ Maintainer

**Dhanush M**  
GitHub: [@DhanushM-IT-Programmer](https://github.com/DhanushM-IT-Programmer)

---




