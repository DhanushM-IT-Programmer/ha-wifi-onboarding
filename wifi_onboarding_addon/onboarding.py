from flask import Flask, request, render_template_string
import os, subprocess, time, sys

app = Flask(__name__)

FORM = """
<!DOCTYPE html><html><body>
<h2>WiFi Onboarding</h2>
<form method="post">
SSID: <input name="ssid"><br>
PSK:  <input name="password" type="password"><br>
<input type="submit" value="Connect">
</form>
</body></html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ssid = request.form["ssid"]
        psk  = request.form["password"]
        # Write minimal wpa_supplicant file
        with open("/tmp/wpa_supplicant.conf", "w") as f:
            f.write(f"""
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=IN

network={{
 ssid="{ssid}"
 psk="{psk}"
}}
""")
        # Stop hotspot services
        subprocess.run(["pkill", "hostapd"])
        subprocess.run(["pkill", "dnsmasq"])
        # Apply the new Wi‑Fi config
        subprocess.run(["ip", "link", "set", "wlan0", "down"])
        subprocess.run(["ip", "link", "set", "wlan0", "up"])
        subprocess.run(["wpa_supplicant", "-B", "-i", "wlan0", "-c", "/tmp/wpa_supplicant.conf"])
        subprocess.run(["udhcpc", "-i", "wlan0"])
        return "Attempting to connect… You can unplug Ethernet and look for the device on your network."
    return render_template_string(FORM)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
