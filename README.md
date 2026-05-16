# Heimdall OS

Heimdall OS is a lightweight Debian-based cybersecurity and digital forensics operating system designed for Blue Team operations, SOC environments, network analysis, and incident response workflows.

---

# Features

- Lightweight XFCE desktop
- Custom Heimdall branding
- Wireshark packet analysis
- tcpdump network capture
- Suricata IDS integration
- Autopsy forensic framework
- nftables firewall rules
- auditd system auditing
- Debian Live-Build architecture
- Live boot ISO support

---

# Included Security Tools

| Tool | Purpose |
|------|----------|
| Wireshark | Packet analysis |
| tcpdump | CLI packet capture |
| Suricata | Intrusion detection system |
| Autopsy | Digital forensics |
| auditd | System activity auditing |
| nftables | Firewall and filtering |

---

# Project Architecture

```text
Debian 12 Base
        │
        ├── XFCE Desktop
        ├── Wireshark
        ├── tcpdump
        ├── Suricata IDS
        ├── Autopsy
        ├── nftables Firewall
        └── auditd Monitoring
```

---

# Build Environment Setup

## Install Docker

### Ubuntu/Debian

```bash
sudo apt update
sudo apt install docker.io -y
```

---

# Start Builder Container

```bash
docker run -it --name heimdall-builder debian:12 bash
```

---

# Install Build Dependencies

```bash
apt update

apt install -y \
live-build \
systemd-container \
debootstrap \
curl \
sudo \
git
```

---

# Clone Repository

```bash
git clone https://github.com/Abhaii11/Heimdall-OS.git

cd Heimdall-OS
```

---

# Build Heimdall OS

```bash
lb clean
lb config
lb build
```

Generated ISO:

```text
live-image-amd64.hybrid.iso
```

---

# Running in VirtualBox

## Recommended VM Settings

| Resource | Value |
|---|---|
| RAM | 4 GB |
| CPU | 2 Cores |
| Storage | 20 GB |
| Video Memory | 128 MB |

---

# Default Login

| Username | Password |
|---|---|
| user | live |

---

# Boot ISO

1. Create VirtualBox VM
2. Select Debian (64-bit)
3. Attach ISO
4. Boot VM

---

# Screenshots

## Heimdall Desktop

![Desktop](screenshots/Screenshot%202026-02-24%20234554.png)

---

## Wireshark Packet Analysis

![Wireshark](screenshots/Screenshot%202026-02-24%20235626.png)

---

## Autopsy Forensics

![Autopsy](screenshots/Screenshot%202026-02-25%20000107.png)

---

## Directory

![Directory](screenshots/Screenshot%202026-02-25%20000233.png)

---

# Repository Structure

```text
Heimdall-OS/
│
├── config/
├── docs/
├── wallpapers/
├── heimdall-dashboard/
├── README.md
├── LICENSE
└── scripts/
```

---

# Current Version

```text
v0.1-alpha
```

---

# Roadmap

- Guardian Dashboard
- Cloud log sync
- Persistent storage
- Threat intelligence feeds
- SOC monitoring panel
- Custom installer
- ISO optimization

---

## Author

Abhay Raut
Atharv Pandhare
Harshal Dhawn
---

## License

MIT License
