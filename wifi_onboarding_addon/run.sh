#!/usr/bin/env bash
set -e

echo "[INFO] Starting WiFi onboarding…"

# Clean reset of wlan0
ip link set wlan0 down || true
ip addr flush dev wlan0 || true
ip link set wlan0 up   || true

# Start hotspot services
hostapd /etc/hostapd.conf &
sleep 2
dnsmasq -C /etc/dnsmasq.conf &

# Captive portal
python3 /onboarding.py
