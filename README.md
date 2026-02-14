📱 TNEH TERMUX SETUP TOOL

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color=00FF00&center=true&vCenter=true&width=435&lines=TNEH+GROUP;TERMUX+SETUP+TOOL;BY+NOMAN" alt="Typing SVG" />
</p>

<p align="center">
  <a href="https://t.me/+QkMGTxBpqftkNDU1">
    <img src="https://img.shields.io/badge/Join-Telegram%20Group-blue?style=for-the-badge&logo=telegram" alt="Telegram Group">
  </a>
  <a href="https://t.me/tneh_owner">
    <img src="https://img.shields.io/badge/Contact-Admin%20Noman-green?style=for-the-badge&logo=telegram" alt="Contact Admin">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0.0-brightgreen?style=flat-square">
  <img src="https://img.shields.io/badge/Python-3.8+-yellow?style=flat-square&logo=python">
  <img src="https://img.shields.io/badge/Platform-Termux-red?style=flat-square&logo=android">
  <img src="https://img.shields.io/badge/License-MIT-purple?style=flat-square">
</p>

---

📋 Description

TNEH TERMUX SETUP TOOL is a comprehensive Python-based utility designed to simplify Termux setup and management on Android devices. Created by Noman and the TNEH Group, this tool provides an all-in-one solution for installing packages, managing storage, and configuring your Termux environment with ease.

---

✨ Features

# Feature Description
01 📦 Package Management Update, upgrade, and install essential packages
02 🔧 Basic Tools Install git, wget, curl, nano, vim, and more
03 🐍 Python Setup Install Python, pip, and upgrade pip
04 📱 Storage Access Setup and manage internal storage permissions
05 🌐 Network Tools Install nmap, hydra, wireshark, and networking utilities
06 🎨 Customization Install Zsh, Oh-My-Zsh, figlet, and themes
07 📁 File Manager Install Midnight Commander, Ranger, and file tools
08 🔐 Security Tools Install Metasploit, hydra, nmap, john, and security apps
09 🚀 Programming Languages Install Node.js, PHP, Perl, Ruby, Go, Rust, Java
10 📊 System Info Display device and system information
11 🔄 Repository Fix Fix Termux repositories and update sources
12 📝 Config Editor Edit bashrc and zshrc configurations
13 📂 Storage Browser Browse and access internal storage folders
14 🧹 Cache Cleaner Clear package cache and temp files
15 📱 Termux API Install and use Termux API tools
16 🎮 Fun Tools Install cmatrix, sl, fortune, cowsay, and games
17 🔍 Device Info Check detailed device information
18 🌍 Web Servers Install Nginx, Apache, PHP-FPM, Flask
19 📖 Help Guide View command reference and usage tips

---

📸 Screenshots

```
┌─────────────────────────────────────────┐
│  ████████╗███╗   ██╗███████╗██╗  ██╗    │
│  ╚══██╔══╝████╗  ██║██╔════╝██║  ██║    │
│     ██║   ██╔██╗ ██║█████╗  ███████║    │
│     ██║   ██║╚██╗██║██╔══╝  ██╔══██║    │
│     ██║   ██║ ╚████║███████╗██║  ██║    │
│     ╚═╝   ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝    │
│                                          │
│       TNEH TERMUX SETUP TOOL v1.0        │
│       ============================        │
│       👤 Admin: Noman                     │
│       📱 Contact: t.me/tneh_owner         │
│       👥 Group: t.me/+QkMGTxBpqftkNDU1    │
│       ============================        │
└─────────────────────────────────────────┘
```

---

🔧 Requirements

Minimum Requirements

· Android 7.0 or higher
· Termux app installed
· 100MB free storage
· 1GB RAM
· Internet connection

Recommended Requirements

· Android 9.0 or higher
· 500MB free storage
· 2GB+ RAM
· Stable internet connection

---

📥 Installation

Method 1: Quick Install (Recommended)

```bash
# Update packages
pkg update && pkg upgrade -y

# Install git
pkg install git -y

# Clone repository
git clone https://github.com/tnehgroup/tneh-termux-setup

# Navigate to directory
cd tneh-termux-setup

# Run installer
chmod +x install.sh
./install.sh
```

Method 2: Manual Installation

```bash
# Update packages
pkg update && pkg upgrade -y

# Install Python
pkg install python python-pip -y

# Download tool
wget -O tneh_tool.py https://raw.githubusercontent.com/tnehgroup/tneh-termux-setup/main/tneh_tool.py

# Make executable
chmod +x tneh_tool.py

# Install requirements
pip install colorama rich tqdm requests psutil

# Run tool
python tneh_tool.py
```

Method 3: Create File Manually

```bash
# Create new file
nano tneh_tool.py

# Copy the code from repository and paste
# Save with Ctrl+X, then Y, then Enter

# Make executable
chmod +x tneh_tool.py

# Run
python tneh_tool.py
```

---

🚀 Usage

```bash
# Basic usage
python tneh_tool.py

# Or if made executable
./tneh_tool.py
```

Menu Navigation

· Enter numbers (1-19) to select options
· Enter 0 to exit
· Press Enter to continue after each operation

---

📦 Package List

Basic Tools

```
git wget curl nano vim openssh htop neofetch unzip zip tar
```

Network Tools

```
nmap net-tools traceroute dnsutils hydra wireshark tshark nethogs
```

Security Tools

```
metasploit hydra nmap sqlmap john aircrack-ng wpscan
```

Programming Languages

```
nodejs php perl ruby golang rust openjdk-17
```

Fun Tools

```
cmatrix sl fortune cowsay toilet boxes lolcat
```

Web Servers

```
nginx apache2 php-fpm python-flask
```

---

⚙️ Configuration

Storage Setup

After first run, ensure storage permission:

```bash
termux-setup-storage
```

Customize Prompt

Edit bashrc or zshrc through option 12:

```bash
# Add custom aliases
alias ll='ls -la'
alias update='pkg update && pkg upgrade'
```

---

🔍 Troubleshooting

Common Issues

Issue Solution
Python not found pkg install python
Permission denied chmod +x tneh_tool.py
Storage access denied termux-setup-storage
Package installation fails pkg update first
Module not found pip install [module]

Error Codes

· Exit 0: Successful execution
· Exit 1: General error
· Exit 2: Permission denied
· Exit 3: Network error

---

👥 Contributing

1. Fork the repository
2. Create feature branch (git checkout -b feature/AmazingFeature)
3. Commit changes (git commit -m 'Add AmazingFeature')
4. Push to branch (git push origin feature/AmazingFeature)
5. Open Pull Request

---

📞 Contact & Support

· 👤 Admin: Noman
· 📱 Telegram: @tneh_owner
· 👥 Group: TNEH Group
· 📧 Email: tneh.group@protonmail.com
· 🌐 Website: Coming Soon

---

📜 License

This project is licensed under the MIT License - see below:

```
MIT License

Copyright (c) 2024 TNEH Group

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

🙏 Acknowledgments

· Termux Development Team
· Python Community
· All TNEH Group Members
· Open Source Contributors

---

📊 Project Status

· ✅ Active Development
· ✅ Stable Release
· ✅ Community Support
· 🔄 Regular Updates

---

⭐ Support Us

If you find this tool useful:

· ⭐ Star this repository
· 📢 Share with friends
· 👥 Join our Telegram group
· 🔁 Fork and contribute

---

<p align="center">
  <b>Made with ❤️ by Noman & TNEH Group</b><br>
  <img src="https://img.shields.io/badge/Made%20with-Python-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/For-Termux-red?style=for-the-badge&logo=android">
</p>

<p align="center">
  <a href="https://t.me/+QkMGTxBpqftkNDU1">
    <img src="https://img.shields.io/badge/Join%20Us%20On-Telegram-blue?style=for-the-badge&logo=telegram">
  </a>
</p>

---

© 2024 TNEH Group. All Rights Reserved.
