FROM python:3.11-slim

# Install AP + network tools
RUN apt-get update && apt-get install -y --no-install-recommends \
        hostapd dnsmasq iproute2 \
    && pip install --no-cache-dir flask \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy add‑on files
COPY run.sh /run.sh
COPY hostapd.conf /etc/hostapd.conf
COPY dnsmasq.conf /etc/dnsmasq.conf
COPY onboarding.py /onboarding.py
COPY www /www

RUN chmod +x /run.sh
CMD ["/run.sh"]
