#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TNEH TERMUX SETUP TOOL
Termux Basic Command Tool
Developed by TNEH Group
"""

import os
import sys
import subprocess
import time
import platform

# Colors for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear_screen():
    """Clear the terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')

def print_banner():
    """Display the TNEH Group banner"""
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
████████╗███╗   ██╗███████╗██╗  ██╗    ██████╗ ██████╗  ██████╗ ██╗   ██╗██████╗ 
╚══██╔══╝████╗  ██║██╔════╝██║  ██║   ██╔════╝ ██╔══██╗██╔═══██╗██║   ██║██╔══██╗
   ██║   ██╔██╗ ██║█████╗  ███████║   ██║  ███╗██████╔╝██║   ██║██║   ██║██████╔╝
   ██║   ██║╚██╗██║██╔══╝  ██╔══██║   ██║   ██║██╔══██╗██║   ██║██║   ██║██╔═══╝ 
   ██║   ██║ ╚████║███████╗██║  ██║   ╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║     
   ╚═╝   ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     
{Colors.ENDC}
{Colors.GREEN}{Colors.BOLD}            TNEH TERMUX SETUP TOOL v1.0{Colors.ENDC}
{Colors.YELLOW}{Colors.BOLD}            ================================{Colors.ENDC}
{Colors.CYAN}            👤 Admin: Noman{Colors.ENDC}
{Colors.CYAN}            📱 Contact: t.me/tneh_owner{Colors.ENDC}
{Colors.CYAN}            👥 Group: t.me/+QkMGTxBpqftkNDU1{Colors.ENDC}
{Colors.YELLOW}{Colors.BOLD}            ================================{Colors.ENDC}
"""
    print(banner)

def print_menu():
    """Display the main menu"""
    menu = f"""
{Colors.GREEN}{Colors.BOLD}[ TNEH TERMUX COMMAND TOOL ]{Colors.ENDC}

{Colors.CYAN}[01]{Colors.ENDC} 📦 Update & Upgrade Packages
{Colors.CYAN}[02]{Colors.ENDC} 🔧 Install Basic Tools
{Colors.CYAN}[03]{Colors.ENDC} 🐍 Install Python & pip
{Colors.CYAN}[04]{Colors.ENDC} 📱 Install Storage Permission Tools
{Colors.CYAN}[05]{Colors.ENDC} 🌐 Install Network Tools
{Colors.CYAN}[06]{Colors.ENDC} 🎨 Install Customization Tools
{Colors.CYAN}[07]{Colors.ENDC} 📁 File Manager Tools
{Colors.CYAN}[08]{Colors.ENDC} 🔐 Install Security Tools
{Colors.CYAN}[09]{Colors.ENDC} 🚀 Install Programming Languages
{Colors.CYAN}[10]{Colors.ENDC} 📊 System Information
{Colors.CYAN}[11]{Colors.ENDC} 🔄 Fix Termux Repository
{Colors.CYAN}[12]{Colors.ENDC} 📝 Edit Bashrc/Zshrc
{Colors.CYAN}[13]{Colors.ENDC} 📂 Access Internal Storage
{Colors.CYAN}[14]{Colors.ENDC} 🧹 Clear Cache & Temp Files
{Colors.CYAN}[15]{Colors.ENDC} 📱 Install Termux API
{Colors.CYAN}[16]{Colors.ENDC} 🎮 Install Fun Tools
{Colors.CYAN}[17]{Colors.ENDC} 🔍 Check Device Info
{Colors.CYAN}[18]{Colors.ENDC} 🌍 Install Web Servers
{Colors.CYAN}[19]{Colors.ENDC} 📖 Show Help
{Colors.CYAN}[00]{Colors.ENDC} 🚪 Exit

{Colors.GREEN}Group: t.me/+QkMGTxBpqftkNDU1{Colors.ENDC}
{Colors.YELLOW}Admin: t.me/tneh_owner (Noman){Colors.ENDC}
"""
    print(menu)

def run_command(command, description):
    """Run a shell command with error handling"""
    print(f"{Colors.YELLOW}[*] {description}...{Colors.ENDC}")
    try:
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        for line in process.stdout:
            print(f"{Colors.CYAN}{line.strip()}{Colors.ENDC}")
        
        process.wait()
        
        if process.returncode == 0:
            print(f"{Colors.GREEN}[✓] Successfully completed!{Colors.ENDC}")
            return True
        else:
            error = process.stderr.read()
            print(f"{Colors.FAIL}[✗] Error: {error}{Colors.ENDC}")
            return False
            
    except Exception as e:
        print(f"{Colors.FAIL}[✗] Failed: {str(e)}{Colors.ENDC}")
        return False

def check_termux():
    """Check if running in Termux"""
    if 'com.termux' not in os.environ.get('PREFIX', ''):
        print(f"{Colors.WARNING}[!] Warning: This tool is designed for Termux{Colors.ENDC}")
        response = input(f"{Colors.YELLOW}Continue anyway? (y/n): {Colors.ENDC}")
        return response.lower() == 'y'
    return True

def update_packages():
    """Update and upgrade packages"""
    print(f"{Colors.GREEN}[*] Updating package lists...{Colors.ENDC}")
    run_command("pkg update -y", "Updating packages")
    run_command("pkg upgrade -y", "Upgrading packages")

def install_basic_tools():
    """Install basic Termux tools"""
    tools = [
        "git", "wget", "curl", "nano", "vim", "openssh",
        "htop", "neofetch", "unzip", "zip", "tar"
    ]
    
    print(f"{Colors.GREEN}[*] Installing basic tools...{Colors.ENDC}")
    for tool in tools:
        run_command(f"pkg install {tool} -y", f"Installing {tool}")

def install_python():
    """Install Python and pip"""
    run_command("pkg install python -y", "Installing Python")
    run_command("pkg install python-pip -y", "Installing pip")
    run_command("pip install --upgrade pip", "Upgrading pip")

def setup_storage():
    """Setup storage permission"""
    run_command("termux-setup-storage", "Setting up storage access")
    print(f"{Colors.GREEN}[✓] Storage access granted!{Colors.ENDC}")

def install_network_tools():
    """Install network tools"""
    tools = [
        "nmap", "net-tools", "traceroute", "dnsutils",
        "hydra", "wireshark", "tshark", "nethogs"
    ]
    
    print(f"{Colors.GREEN}[*] Installing network tools...{Colors.ENDC}")
    for tool in tools:
        run_command(f"pkg install {tool} -y", f"Installing {tool}")

def install_customization():
    """Install customization tools"""
    run_command("pkg install zsh -y", "Installing Zsh")
    run_command("pkg install oh-my-zsh -y", "Installing Oh-My-Zsh")
    run_command("pkg install figlet -y", "Installing Figlet")
    run_command("pkg install lolcat -y", "Installing Lolcat")

def file_manager():
    """Install file manager tools"""
    run_command("pkg install mc -y", "Installing Midnight Commander")
    run_command("pkg install ranger -y", "Installing Ranger")

def install_security():
    """Install security tools"""
    tools = [
        "metasploit", "hydra", "nmap", "sqlmap",
        "john", "aircrack-ng", "wpscan"
    ]
    
    print(f"{Colors.GREEN}[*] Installing security tools...{Colors.ENDC}")
    for tool in tools:
        run_command(f"pkg install {tool} -y", f"Installing {tool}")

def install_programming():
    """Install programming languages"""
    languages = [
        "nodejs", "php", "perl", "ruby",
        "golang", "rust", "openjdk-17"
    ]
    
    print(f"{Colors.GREEN}[*] Installing programming languages...{Colors.ENDC}")
    for lang in languages:
        run_command(f"pkg install {lang} -y", f"Installing {lang}")

def system_info():
    """Display system information"""
    run_command("neofetch", "Displaying system info")

def fix_repository():
    """Fix Termux repository"""
    commands = [
        "termux-change-repo",
        "pkg update -y"
    ]
    
    for cmd in commands:
        run_command(cmd, f"Running: {cmd}")

def edit_bashrc():
    """Edit bashrc or zshrc"""
    print(f"{Colors.GREEN}[*] Choose file to edit:{Colors.ENDC}")
    print("1. .bashrc")
    print("2. .zshrc")
    choice = input(f"{Colors.YELLOW}Enter choice (1/2): {Colors.ENDC}")
    
    if choice == "1":
        run_command("nano $HOME/.bashrc", "Editing .bashrc")
    elif choice == "2":
        run_command("nano $HOME/.zshrc", "Editing .zshrc")
    else:
        print(f"{Colors.FAIL}[!] Invalid choice{Colors.ENDC}")

def access_storage():
    """Access internal storage"""
    print(f"{Colors.GREEN}[*] Available storage paths:{Colors.ENDC}")
    run_command("ls ~/storage", "Listing storage")
    
    print("\n1. Access Downloads")
    print("2. Access Documents")
    print("3. Access Pictures")
    print("4. Access Music")
    print("5. Access Videos")
    print("6. Access External SD")
    print("7. Custom path")
    
    choice = input(f"{Colors.YELLOW}Enter choice: {Colors.ENDC}")
    
    paths = {
        "1": "~/storage/downloads",
        "2": "~/storage/documents",
        "3": "~/storage/pictures",
        "4": "~/storage/music",
        "5": "~/storage/movies",
        "6": "~/storage/external-1"
    }
    
    if choice in paths:
        run_command(f"cd {paths[choice]} && pwd && ls -la", f"Accessing {paths[choice]}")
    elif choice == "7":
        path = input("Enter full path: ")
        run_command(f"cd {path} && pwd && ls -la", f"Accessing {path}")
    else:
        print(f"{Colors.FAIL}[!] Invalid choice{Colors.ENDC}")

def clear_cache():
    """Clear cache and temp files"""
    run_command("pkg clean", "Cleaning package cache")
    run_command("apt autoremove -y", "Removing unnecessary packages")

def install_termux_api():
    """Install Termux API"""
    run_command("pkg install termux-api -y", "Installing Termux API")

def install_fun_tools():
    """Install fun tools"""
    tools = [
        "cmatrix", "sl", "fortune", "cowsay",
        "toilet", "boxes", "lolcat"
    ]
    
    print(f"{Colors.GREEN}[*] Installing fun tools...{Colors.ENDC}")
    for tool in tools:
        run_command(f"pkg install {tool} -y", f"Installing {tool}")

def device_info():
    """Display device information"""
    run_command("termux-info", "Displaying Termux info")
    run_command("getprop ro.product.model", "Device model")
    run_command("getprop ro.build.version.release", "Android version")
    run_command("df -h", "Storage information")

def install_web_servers():
    """Install web servers"""
    tools = [
        "nginx", "apache2", "php-fpm",
        "python-flask", "nodejs"
    ]
    
    print(f"{Colors.GREEN}[*] Installing web servers...{Colors.ENDC}")
    for tool in tools:
        run_command(f"pkg install {tool} -y", f"Installing {tool}")

def show_help():
    """Show help information"""
    help_text = f"""
{Colors.GREEN}{Colors.BOLD}TNEH TERMUX SETUP TOOL - HELP{Colors.ENDC}

{Colors.CYAN}Basic Commands:{Colors.ENDC}
• pkg update/upgrade - Update packages
• pkg install [package] - Install package
• pkg list-all - List all packages
• pkg remove [package] - Remove package

{Colors.CYAN}File Operations:{Colors.ENDC}
• ls - List files
• cd [dir] - Change directory
• cp - Copy files
• mv - Move/rename files
• rm - Remove files
• mkdir - Create directory

{Colors.CYAN}Network Commands:{Colors.ENDC}
• ifconfig - Network configuration
• ping - Test connectivity
• wget - Download files
• curl - Transfer data
• nmap - Network scanner

{Colors.CYAN}Useful Tips:{Colors.ENDC}
• Use 'tab' for auto-completion
• Press ↑ for command history
• Use Ctrl+C to stop processes
• Use Ctrl+L to clear screen

{Colors.GREEN}Group: t.me/+QkMGTxBpqftkNDU1{Colors.ENDC}
{Colors.YELLOW}Admin: t.me/tneh_owner (Noman){Colors.ENDC}
"""
    print(help_text)

def main():
    """Main function"""
    clear_screen()
    
    if not check_termux():
        print(f"{Colors.FAIL}[!] Exiting...{Colors.ENDC}")
        sys.exit(1)
    
    while True:
        clear_screen()
        print_banner()
        print_menu()
        
        try:
            choice = input(f"{Colors.GREEN}[ TNEH@Termux ]$ {Colors.ENDC}")
            
            if choice == "01" or choice == "1":
                update_packages()
            elif choice == "02" or choice == "2":
                install_basic_tools()
            elif choice == "03" or choice == "3":
                install_python()
            elif choice == "04" or choice == "4":
                setup_storage()
            elif choice == "05" or choice == "5":
                install_network_tools()
            elif choice == "06" or choice == "6":
                install_customization()
            elif choice == "07" or choice == "7":
                file_manager()
            elif choice == "08" or choice == "8":
                install_security()
            elif choice == "09" or choice == "9":
                install_programming()
            elif choice == "10":
                system_info()
            elif choice == "11":
                fix_repository()
            elif choice == "12":
                edit_bashrc()
            elif choice == "13":
                access_storage()
            elif choice == "14":
                clear_cache()
            elif choice == "15":
                install_termux_api()
            elif choice == "16":
                install_fun_tools()
            elif choice == "17":
                device_info()
            elif choice == "18":
                install_web_servers()
            elif choice == "19":
                show_help()
            elif choice == "00" or choice == "0":
                print(f"{Colors.GREEN}[✓] Thanks for using TNEH Termux Tool!{Colors.ENDC}")
                print(f"{Colors.CYAN}Join our group: t.me/+QkMGTxBpqftkNDU1{Colors.ENDC}")
                break
            else:
                print(f"{Colors.FAIL}[!] Invalid option! Please try again.{Colors.ENDC}")
            
            if choice != "00" and choice != "0":
                input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.ENDC}")
                
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}[!] Interrupted by user{Colors.ENDC}")
            break
        except Exception as e:
            print(f"{Colors.FAIL}[!] Error: {str(e)}{Colors.ENDC}")
            input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.ENDC}")

if __name__ == "__main__":
    main()
