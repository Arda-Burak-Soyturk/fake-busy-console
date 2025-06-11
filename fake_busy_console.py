import random
import time
import sys
import os
from datetime import datetime

# ANSI color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    # Add some unusual colors
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    # Add some bright colors
    BRIGHT_RED = '\033[91;1m'
    BRIGHT_GREEN = '\033[92;1m'
    BRIGHT_YELLOW = '\033[93;1m'
    BRIGHT_BLUE = '\033[94;1m'
    BRIGHT_MAGENTA = '\033[95;1m'
    BRIGHT_CYAN = '\033[96;1m'

class ProgressBar:
    def __init__(self, width=50):
        self.width = width
        self.progress = 0
        self.start_time = None
        self.styles = [
            {'left': '[', 'right': ']', 'fill': '=', 'tip': '>', 'empty': '-'},
            {'left': '[', 'right': ']', 'fill': '#', 'tip': '', 'empty': ' '},
            {'left': '|', 'right': '|', 'fill': '█', 'tip': '', 'empty': '░'},
            {'left': '⟦', 'right': '⟧', 'fill': '━', 'tip': '╺', 'empty': ' '},
            {'left': '【', 'right': '】', 'fill': '■', 'tip': '', 'empty': '□'},
            {'left': '⟨', 'right': '⟩', 'fill': '●', 'tip': '', 'empty': '○'},
        ]
        self.current_style = random.choice(self.styles)

    def get_time_remaining(self):
        if not self.start_time:
            return "Calculating..."
        
        elapsed = time.time() - self.start_time
        if self.progress == 0:
            return "Calculating..."
        
        # Estimate total time based on current progress
        total_estimated = elapsed / (self.progress / 100)
        remaining = total_estimated - elapsed
        
        if remaining < 60:
            return f"{remaining:.1f}s"
        elif remaining < 3600:
            return f"{remaining/60:.1f}m"
        else:
            return f"{remaining/3600:.1f}h"

    def update(self, progress):
        if self.progress == 0:
            self.start_time = time.time()
            
        self.progress = min(100, max(0, progress))
        filled = int(self.width * self.progress / 100)
        
        # Create the progress bar
        bar = (self.current_style['fill'] * (filled - 1) + 
               self.current_style['tip'] + 
               self.current_style['empty'] * (self.width - filled))
        
        # Format the output with time remaining
        time_remaining = self.get_time_remaining()
        
        # Add some color based on progress
        if self.progress < 30:
            color = Colors.RED
        elif self.progress < 70:
            color = Colors.YELLOW
        else:
            color = Colors.GREEN
            
        # Format the complete progress bar
        output = (f"\r{color}{self.current_style['left']}{bar}{self.current_style['right']} "
                 f"{self.progress:5.1f}% "
                 f"ETA: {time_remaining}{Colors.ENDC}")
        
        sys.stdout.write(output)
        sys.stdout.flush()

class Spinner:
    def __init__(self):
        self.frames = ['|', '/', '-', '\\']
        self.index = 0

    def spin(self, delay=0.05, cycles=20):
        for _ in range(cycles):
            sys.stdout.write(self.frames[self.index % len(self.frames)])
            sys.stdout.flush()
            time.sleep(delay)
            sys.stdout.write('\b')
            self.index += 1

class TaskManager:
    def __init__(self):
        self.static_tasks = [
            "Compiling kernel module...",
            "Running system diagnostics...",
            "Flushing DNS cache...",
            "Executing batch operation...",
            "Writing buffer to /dev/null...",
            "Verifying system integrity...",
            "Optimizing database indexes...",
            "Running garbage collection...",
            "Checking for system updates...",
            "Analyzing network traffic...",
        ]
        self.error_messages = [
            "Connection timeout",
            "Permission denied",
            "Resource temporarily unavailable",
            "Invalid checksum",
            "Buffer overflow detected",
            "Memory allocation failed",
            "Network unreachable",
            "Service unavailable",
        ]
        self.packages = [
            "linux-headers", "python3", "nginx", "postgresql", "docker", "nodejs",
            "apache2", "mysql-server", "php", "ruby", "golang", "rustc",
            "gcc", "clang", "vim", "emacs", "git", "curl", "wget", "openssh",
            "systemd", "grub", "kernel", "glibc", "gcc-libs", "binutils",
            "openssl", "libssl", "zlib", "bzip2", "xz", "lz4", "zstd"
        ]
        self.repositories = [
            "main", "universe", "multiverse", "restricted", "backports",
            "security", "updates", "proposed", "partner", "canonical"
        ]
        self.commands = [
            "winget", "npm", "pip", "docker", "kubectl", "terraform", "ansible",
            "vagrant", "composer", "yarn", "gradle", "maven", "dotnet", "go",
            "rustc", "gcc", "clang", "make", "cmake", "ninja"
        ]
        self.error_categories = [
            "ObjectNotFound", "CommandNotFoundException", "InvalidOperationException",
            "UnauthorizedAccessException", "InvalidDataException", "TimeoutException",
            "NotSupportedException", "InvalidCastException", "FormatException",
            "ArgumentNullException", "DirectoryNotFoundException", "FileNotFoundException",
            "IOException", "SecurityException", "AccessViolationException"
        ]
        self.symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
        self.hex_chars = "0123456789ABCDEF"

    def generate_garbled_text(self):
        # Generate a long line of random characters
        length = random.randint(50, 120)
        result = []
        
        # Mix of different character types
        for _ in range(length):
            char_type = random.random()
            if char_type < 0.3:  # 30% chance for hex values
                result.append(f"0x{random.choice(self.hex_chars)}{random.choice(self.hex_chars)}")
            elif char_type < 0.5:  # 20% chance for symbols
                result.append(random.choice(self.symbols))
            elif char_type < 0.7:  # 20% chance for numbers
                result.append(str(random.randint(0, 9)))
            else:  # 30% chance for letters
                result.append(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        
        return "".join(result)

    def generate_powershell_error(self):
        command = random.choice(self.commands)
        error_category = random.choice(self.error_categories)
        line_num = random.randint(1, 100)
        char_pos = random.randint(1, 50)
        
        error_msg = f"""{command} : The term '{command}' is not recognized as the name of a cmdlet, function, script file, or operable program.
Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:{line_num} char:{char_pos}
+ {command}
+ {'~' * len(command)}
    + CategoryInfo          : {error_category}: ({command}:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\\Users\\Administrator>"""
        return error_msg

    def generate_apt_update(self):
        repo = random.choice(self.repositories)
        return f"Hit:1 http://archive.ubuntu.com/ubuntu {repo} InRelease"

    def generate_apt_upgrade(self):
        package = random.choice(self.packages)
        version = f"{random.randint(1, 5)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
        return f"Upgrading {package} ({version}-{random.randint(1, 50)}ubuntu{random.randint(1, 5)})"

    def generate_dpkg(self):
        package = random.choice(self.packages)
        return f"Unpacking {package} ({random.randint(1, 5)}.{random.randint(0, 9)}.{random.randint(0, 9)})"

    def generate_systemd(self):
        services = [
            "apache2", "nginx", "mysql", "postgresql", "docker", "ssh",
            "cron", "rsyslog", "systemd-logind", "network-manager"
        ]
        service = random.choice(services)
        actions = ["Starting", "Stopping", "Restarting", "Reloading"]
        action = random.choice(actions)
        return f"{action} {service} service..."

    def get_error(self):
        # 30% chance to generate a PowerShell-style error
        if random.random() < 0.3:
            return self.generate_powershell_error()
        return random.choice(self.error_messages)

    def generate_dynamic_task(self):
        # 15% chance to generate garbled text
        if random.random() < 0.15:
            return self.generate_garbled_text()

        # Add Linux-style operations with 40% probability
        if random.random() < 0.4:
            operations = [
                self.generate_apt_update,
                self.generate_apt_upgrade,
                self.generate_dpkg,
                self.generate_systemd
            ]
            return random.choice(operations)()

        # Original dynamic tasks
        dynamic_templates = [
            # Network operations
            lambda: f"Pinging 192.168.{random.randint(0, 255)}.{random.randint(0, 255)}...",
            lambda: f"Scanning ports on 10.0.{random.randint(0, 255)}.{random.randint(0, 255)}...",
            lambda: f"Establishing secure tunnel to proxy node {random.randint(1, 99)}...",
            lambda: f"Analyzing TCP/IP stack on interface eth{random.randint(0, 3)}...",
            lambda: f"Routing table optimization for subnet 172.{random.randint(16, 31)}.{random.randint(0, 255)}.0/24...",
            
            # Memory and system operations
            lambda: f"Loading memory address 0x{random.randint(10000, 99999):X}...",
            lambda: f"Flushing L{random.randint(1, 3)} cache for processor {random.randint(0, 15)}...",
            lambda: f"Allocating {random.randint(1, 1024)}MB of virtual memory...",
            lambda: f"Defragmenting memory block 0x{random.randint(100000, 999999):X}...",
            lambda: f"Validating memory integrity at 0x{random.randint(1000000, 9999999):X}...",
            
            # File system operations
            lambda: f"Analyzing sector {random.randint(1000, 9000)} on /dev/sd{random.choice('abcdef')}...",
            lambda: f"Optimizing file system journal on partition {random.randint(1, 8)}...",
            lambda: f"Checking file system consistency on mount point /mnt/disk{random.randint(1, 5)}...",
            lambda: f"Writing buffer to /dev/null (size: {random.randint(1, 1000)}MB)...",
            lambda: f"Calculating checksums for block {random.randint(1000, 9999)}...",
            
            # Security operations
            lambda: f"Encrypting payload segment {random.choice('ABCDEF')} with AES-256...",
            lambda: f"Validating certificate chain for domain {random.choice(['example.com', 'test.org', 'demo.net'])}...",
            lambda: f"Generating {random.randint(2048, 4096)}-bit RSA key pair...",
            lambda: f"Verifying digital signature for package {random.randint(1000, 9999)}...",
            lambda: f"Running security audit on user {random.choice(['root', 'admin', 'system'])}...",
            
            # Database operations
            lambda: f"Optimizing database indexes for table 'users_{random.randint(1, 100)}'...",
            lambda: f"Executing SQL query on database 'db_{random.randint(1, 50)}'...",
            lambda: f"Rebuilding database cache for collection {random.choice(['users', 'logs', 'metrics'])}...",
            lambda: f"Running database maintenance on schema v{random.randint(1, 5)}.{random.randint(0, 9)}...",
            lambda: f"Analyzing query performance for index idx_{random.randint(1000, 9999)}...",
            
            # System maintenance
            lambda: f"Running garbage collection cycle {random.randint(1, 1000)}...",
            lambda: f"Compressing data block {random.randint(1, 1000)} with zlib...",
            lambda: f"Processing batch job {random.randint(1000, 9999)} (priority: {random.randint(1, 10)})...",
            lambda: f"Updating system configuration for module mod_{random.randint(1, 100)}...",
            lambda: f"Verifying system integrity checksum [{hex(random.randint(100000, 999999))}]...",
            
            # Complex operations
            lambda: f"Initializing quantum computing simulation (qubits: {random.randint(2, 8)})...",
            lambda: f"Running neural network training iteration {random.randint(1, 1000)}...",
            lambda: f"Processing blockchain transaction 0x{random.randint(1000000, 9999999):X}...",
            lambda: f"Analyzing machine learning model accuracy (epoch {random.randint(1, 100)})...",
            lambda: f"Optimizing hyperparameters for algorithm {random.choice(['SVM', 'RandomForest', 'XGBoost'])}...",
            
            # Debug operations
            lambda: f"Attaching debugger to process PID {random.randint(1000, 9999)}...",
            lambda: f"Analyzing core dump from thread {random.randint(1, 100)}...",
            lambda: f"Profiling function execution time for method {random.choice(['main', 'process', 'handle'])}...",
            lambda: f"Checking memory leaks in module {random.choice(['kernel', 'network', 'storage'])}...",
            lambda: f"Validating stack trace for exception 0x{random.randint(100000, 999999):X}...",
        ]
        return random.choice(dynamic_templates)()

    def get_task(self):
        if random.random() < 0.6:
            return self.generate_dynamic_task()
        else:
            return random.choice(self.static_tasks)

    def add_task(self, task_str: str):
        self.static_tasks.append(task_str)

class SystemStatus:
    def __init__(self):
        self.cpu_usage = 0
        self.memory_usage = 0
        self.uptime = 0
        self.cpu_temp = 0
        self.process_count = 0
        self.network_usage = 0
        self.disk_io = 0

    def update(self):
        self.cpu_usage = random.uniform(20, 95)
        self.memory_usage = random.uniform(30, 85)
        self.uptime += 1
        self.cpu_temp = random.uniform(45, 85)
        self.process_count = random.randint(100, 500)
        self.network_usage = random.uniform(1, 100)
        self.disk_io = random.uniform(1, 100)

    def display(self):
        uptime_str = f"{self.uptime // 3600:02d}:{(self.uptime % 3600) // 60:02d}:{self.uptime % 60:02d}"
        return (
            f"{Colors.BOLD}╔{'═' * 118}╗{Colors.ENDC}\n"
            f"{Colors.BOLD}║{Colors.ENDC} "
            f"{Colors.YELLOW}CPU: {self.cpu_usage:5.1f}%{Colors.ENDC} | "
            f"{Colors.YELLOW}TEMP: {self.cpu_temp:4.1f}°C{Colors.ENDC} | "
            f"{Colors.YELLOW}RAM: {self.memory_usage:5.1f}%{Colors.ENDC} | "
            f"{Colors.YELLOW}PROC: {self.process_count:4d}{Colors.ENDC} | "
            f"{Colors.YELLOW}NET: {self.network_usage:5.1f}MB/s{Colors.ENDC} | "
            f"{Colors.YELLOW}DISK: {self.disk_io:5.1f}MB/s{Colors.ENDC} | "
            f"{Colors.YELLOW}UPTIME: {uptime_str}{Colors.ENDC}"
            f"{Colors.BOLD} ║{Colors.ENDC}\n"
            f"{Colors.BOLD}╚{'═' * 118}╝{Colors.ENDC}\n"
        )

class SystemLogger:
    def __init__(self):
        self.log_levels = {
            'INFO': Colors.GREEN,
            'WARNING': Colors.YELLOW,
            'ERROR': Colors.RED,
            'DEBUG': Colors.BLUE,
            'CRITICAL': Colors.BRIGHT_RED
        }
        self.kernel_prefixes = [
            'kernel', 'systemd', 'NetworkManager', 'dhcpd', 'sshd',
            'apache2', 'nginx', 'mysql', 'postgresql', 'docker'
        ]
        self.process_names = [
            'chrome', 'firefox', 'explorer', 'svchost', 'system',
            'python', 'node', 'java', 'php', 'nginx', 'apache2',
            'mysqld', 'postgres', 'redis', 'mongod', 'docker'
        ]
        self.log_messages = {
            'INFO': [
                "User session started",
                "Service started successfully",
                "Configuration loaded",
                "Cache cleared",
                "Backup completed",
                "Update check completed",
                "Connection established",
                "Authentication successful",
                "File transfer completed",
                "Database connection established"
            ],
            'WARNING': [
                "High memory usage detected",
                "Disk space running low",
                "Connection timeout",
                "Retry attempt failed",
                "Service restart required",
                "Configuration file not found",
                "Invalid credentials attempt",
                "Resource limit reached",
                "Performance degradation detected",
                "Unusual activity detected"
            ],
            'ERROR': [
                "Failed to start service",
                "Connection refused",
                "Permission denied",
                "File not found",
                "Database connection failed",
                "Memory allocation failed",
                "Invalid configuration",
                "Authentication failed",
                "Resource unavailable",
                "Operation timed out"
            ],
            'DEBUG': [
                "Processing request",
                "Validating input",
                "Checking permissions",
                "Initializing component",
                "Loading configuration",
                "Establishing connection",
                "Compiling template",
                "Executing query",
                "Parsing response",
                "Updating cache"
            ],
            'CRITICAL': [
                "System crash detected",
                "Kernel panic",
                "Fatal error in core service",
                "Database corruption detected",
                "Security breach attempt",
                "Hardware failure",
                "Critical service down",
                "System resource exhaustion",
                "Data integrity check failed",
                "Emergency shutdown required"
            ]
        }
        self.kernel_messages = [
            "CPU temperature above threshold",
            "Memory allocation failed",
            "I/O error on device",
            "Network interface down",
            "Filesystem error detected",
            "Hardware watchdog triggered",
            "PCIe error detected",
            "USB device disconnected",
            "ACPI error",
            "DMA buffer overflow"
        ]

    def generate_kernel_message(self):
        prefix = random.choice(self.kernel_prefixes)
        message = random.choice(self.kernel_messages)
        return f"{prefix}: {message}"

    def generate_process_message(self):
        process = random.choice(self.process_names)
        pid = random.randint(1000, 9999)
        action = random.choice(['started', 'stopped', 'crashed', 'restarted'])
        return f"Process {process}[{pid}] {action}"

    def generate_log(self):
        # 30% chance for kernel message
        if random.random() < 0.3:
            return self.generate_kernel_message()
        
        # 20% chance for process message
        if random.random() < 0.2:
            return self.generate_process_message()
        
        # Regular log message
        level = random.choice(list(self.log_levels.keys()))
        message = random.choice(self.log_messages[level])
        color = self.log_levels[level]
        
        # Add some random context
        if random.random() < 0.3:
            context = f" (pid={random.randint(1000, 9999)})"
        else:
            context = ""
            
        return f"{color}[{level}] {message}{context}{Colors.ENDC}"

class NetworkTrafficSimulator:
    def __init__(self):
        self.protocols = ['TCP', 'UDP', 'ICMP', 'HTTP', 'HTTPS', 'FTP', 'SSH', 'DNS']
        self.ports = {
            'HTTP': 80,
            'HTTPS': 443,
            'FTP': 21,
            'SSH': 22,
            'DNS': 53,
            'SMTP': 25,
            'POP3': 110,
            'IMAP': 143,
            'MySQL': 3306,
            'PostgreSQL': 5432,
            'MongoDB': 27017,
            'Redis': 6379
        }
        self.status_codes = ['ESTABLISHED', 'TIME_WAIT', 'CLOSE_WAIT', 'LISTEN', 'SYN_SENT']
        self.connection_types = ['incoming', 'outgoing']
        
    def generate_ip(self):
        return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    
    def generate_port(self):
        return random.randint(1024, 65535)
    
    def generate_packet_count(self):
        return random.randint(1, 9999)
    
    def generate_connection_log(self):
        protocol = random.choice(self.protocols)
        src_ip = self.generate_ip()
        dst_ip = self.generate_ip()
        src_port = self.generate_port()
        dst_port = self.ports.get(protocol, self.generate_port())
        status = random.choice(self.status_codes)
        packets = self.generate_packet_count()
        conn_type = random.choice(self.connection_types)
        
        return f"{protocol} {src_ip}:{src_port} -> {dst_ip}:{dst_port} {status} {packets} packets {conn_type}"
    
    def generate_port_scan(self):
        target_ip = self.generate_ip()
        ports = sorted(random.sample(range(1, 1024), 3))
        return f"Port scan detected on {target_ip} - Scanned ports: {', '.join(map(str, ports))}"
    
    def generate_connection_attempt(self):
        protocol = random.choice(self.protocols)
        src_ip = self.generate_ip()
        dst_ip = self.generate_ip()
        dst_port = self.ports.get(protocol, self.generate_port())
        result = random.choice(['success', 'failed', 'timeout', 'refused'])
        
        return f"Connection attempt: {protocol} {src_ip} -> {dst_ip}:{dst_port} - {result}"
    
    def generate_network_log(self):
        log_types = [
            self.generate_connection_log,
            self.generate_port_scan,
            self.generate_connection_attempt
        ]
        weights = [0.5, 0.2, 0.3]  # 50% connection logs, 20% port scans, 30% connection attempts
        return random.choices(log_types, weights=weights)[0]()

class FileOperationsSimulator:
    def __init__(self):
        self.file_extensions = [
            '.txt', '.log', '.json', '.xml', '.csv', '.dat', '.bin',
            '.exe', '.dll', '.so', '.dylib', '.py', '.js', '.html',
            '.css', '.jpg', '.png', '.pdf', '.zip', '.tar', '.gz'
        ]
        self.directories = [
            '/var/log', '/etc', '/usr/bin', '/home/user',
            '/opt', '/tmp', '/var/www', '/var/lib',
            'C:\\Windows\\System32', 'C:\\Program Files',
            'C:\\Users\\Administrator\\Documents',
            'C:\\Users\\Administrator\\Downloads'
        ]
        self.file_names = [
            'system', 'config', 'backup', 'data', 'temp',
            'cache', 'log', 'error', 'debug', 'info',
            'report', 'analysis', 'database', 'settings',
            'document', 'image', 'archive', 'package'
        ]
        self.permissions = ['r', 'w', 'x']
        self.transfer_speeds = ['KB/s', 'MB/s', 'GB/s']
        
    def generate_file_name(self):
        name = random.choice(self.file_names)
        ext = random.choice(self.file_extensions)
        return f"{name}{ext}"
    
    def generate_file_size(self):
        size = random.randint(1, 9999)
        unit = random.choice(['B', 'KB', 'MB', 'GB'])
        return f"{size}{unit}"
    
    def generate_transfer_speed(self):
        speed = random.uniform(1, 999)
        unit = random.choice(self.transfer_speeds)
        return f"{speed:.1f}{unit}"
    
    def generate_file_transfer(self):
        src_file = self.generate_file_name()
        dst_file = self.generate_file_name()
        size = self.generate_file_size()
        speed = self.generate_transfer_speed()
        progress = random.randint(0, 100)
        
        return f"Transferring {src_file} -> {dst_file} ({size}) [{progress}%] {speed}"
    
    def generate_directory_listing(self):
        dir_path = random.choice(self.directories)
        num_files = random.randint(3, 8)
        files = []
        
        for _ in range(num_files):
            size = self.generate_file_size()
            name = self.generate_file_name()
            date = f"{random.randint(1, 31):02d}-{random.randint(1, 12):02d}-{random.randint(2020, 2024)}"
            time = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}"
            files.append(f"{size} {date} {time} {name}")
        
        return f"Directory of {dir_path}\n" + "\n".join(files)
    
    def generate_permission_change(self):
        file_name = self.generate_file_name()
        old_perms = ''.join(random.sample(self.permissions, random.randint(1, 3)))
        new_perms = ''.join(random.sample(self.permissions, random.randint(1, 3)))
        user = random.choice(['user', 'group', 'others'])
        
        return f"Changing permissions: {file_name} {old_perms} -> {new_perms} for {user}"
    
    def generate_file_operation(self):
        operation_types = [
            self.generate_file_transfer,
            self.generate_directory_listing,
            self.generate_permission_change
        ]
        weights = [0.4, 0.3, 0.3]  # 40% transfers, 30% listings, 30% permission changes
        return random.choices(operation_types, weights=weights)[0]()

class ProcessInfoSimulator:
    def __init__(self):
        self.process_names = [
            'chrome', 'firefox', 'explorer', 'svchost', 'system',
            'python', 'node', 'java', 'php', 'nginx', 'apache2',
            'mysqld', 'postgres', 'redis', 'mongod', 'docker',
            'systemd', 'sshd', 'cron', 'rsyslog', 'network',
            'kernel', 'init', 'bash', 'zsh', 'powershell'
        ]
        self.process_states = ['running', 'sleeping', 'stopped', 'zombie', 'uninterruptible']
        self.process_types = ['system', 'user', 'daemon', 'kernel']
        
    def generate_pid(self):
        return random.randint(1, 65535)
    
    def generate_cpu_usage(self):
        return random.uniform(0.1, 99.9)
    
    def generate_memory_usage(self):
        return random.uniform(0.1, 4096.0)  # MB
    
    def generate_process_tree(self, depth=0, max_depth=3):
        if depth >= max_depth:
            return []
            
        num_children = random.randint(0, 3) if depth < max_depth - 1 else 0
        processes = []
        
        # Parent process
        parent_pid = self.generate_pid()
        parent_name = random.choice(self.process_names)
        parent_cpu = self.generate_cpu_usage()
        parent_mem = self.generate_memory_usage()
        parent_state = random.choice(self.process_states)
        
        indent = "  " * depth
        processes.append(f"{indent}├─ {parent_name}[{parent_pid}] {parent_state} CPU: {parent_cpu:.1f}% MEM: {parent_mem:.1f}MB")
        
        # Child processes
        for i in range(num_children):
            child_processes = self.generate_process_tree(depth + 1, max_depth)
            processes.extend(child_processes)
            
        return processes
    
    def generate_process_list(self):
        num_processes = random.randint(5, 10)
        processes = []
        
        for _ in range(num_processes):
            pid = self.generate_pid()
            name = random.choice(self.process_names)
            cpu = self.generate_cpu_usage()
            mem = self.generate_memory_usage()
            state = random.choice(self.process_states)
            process_type = random.choice(self.process_types)
            
            processes.append(f"{pid:6d} {name:15s} {state:10s} {cpu:6.1f}% {mem:8.1f}MB {process_type}")
        
        return processes
    
    def generate_memory_allocation(self):
        total_memory = 16384.0  # 16GB
        used_memory = random.uniform(total_memory * 0.3, total_memory * 0.9)
        free_memory = total_memory - used_memory
        cached = random.uniform(0, free_memory * 0.5)
        buffers = random.uniform(0, free_memory * 0.3)
        swap_used = random.uniform(0, total_memory * 0.2)
        
        return (
            f"Memory Usage:\n"
            f"Total:     {total_memory:8.1f}MB\n"
            f"Used:      {used_memory:8.1f}MB\n"
            f"Free:      {free_memory:8.1f}MB\n"
            f"Cached:    {cached:8.1f}MB\n"
            f"Buffers:   {buffers:8.1f}MB\n"
            f"Swap Used: {swap_used:8.1f}MB"
        )
    
    def generate_process_info(self):
        info_types = [
            self.generate_process_tree,
            self.generate_process_list,
            self.generate_memory_allocation
        ]
        weights = [0.3, 0.4, 0.3]  # 30% trees, 40% lists, 30% memory
        generator = random.choices(info_types, weights=weights)[0]
        
        if generator == self.generate_process_tree:
            return "Process Tree:\n" + "\n".join(generator())
        elif generator == self.generate_process_list:
            return "Process List:\nPID     NAME            STATE      CPU%   MEM      TYPE\n" + "\n".join(generator())
        else:
            return generator()

class InteractiveSimulator:
    def __init__(self):
        self.prompts = [
            'PS C:\\Users\\Administrator>',
            'root@server:~#',
            'user@desktop:$',
            'C:\\>',
            'mysql>',
            'python>',
            '>>>',
            'In [1]:',
            'docker>',
            'git>'
        ]
        self.commands = [
            'ls', 'dir', 'cd', 'pwd', 'git status', 'git pull',
            'docker ps', 'docker-compose up', 'npm install',
            'pip install', 'python script.py', 'mysql -u root',
            'systemctl status', 'journalctl', 'top', 'htop',
            'vim', 'nano', 'cat', 'grep', 'find', 'chmod',
            'chown', 'tar', 'zip', 'unzip', 'curl', 'wget',
            'ping', 'ssh', 'scp', 'rsync', 'mount', 'umount'
        ]
        self.cursor_positions = ['|', '█', '▌', '▐']
        self.command_history = []
        self.current_prompt = random.choice(self.prompts)
        
    def generate_command(self):
        command = random.choice(self.commands)
        self.command_history.append(command)
        if len(self.command_history) > 10:
            self.command_history.pop(0)
        return command
    
    def generate_prompt(self):
        self.current_prompt = random.choice(self.prompts)
        cursor = random.choice(self.cursor_positions)
        return f"{self.current_prompt} {cursor}"
    
    def generate_command_history(self):
        if not self.command_history:
            return "No commands in history"
        
        history = []
        for i, cmd in enumerate(self.command_history, 1):
            history.append(f"{i:3d}  {cmd}")
        return "Command History:\n" + "\n".join(history)
    
    def generate_cursor_movement(self):
        movements = [
            '\033[D',  # Left
            '\033[C',  # Right
            '\033[A',  # Up
            '\033[B',  # Down
            '\033[H',  # Home
            '\033[F'   # End
        ]
        return random.choice(movements)
    
    def generate_interaction(self):
        interaction_types = [
            self.generate_prompt,
            self.generate_command,
            self.generate_command_history
        ]
        weights = [0.4, 0.4, 0.2]  # 40% prompts, 40% commands, 20% history
        generator = random.choices(interaction_types, weights=weights)[0]
        
        if generator == self.generate_command_history:
            return generator()
        else:
            result = generator()
            # Add cursor movement after command or prompt
            if random.random() < 0.3:
                result += self.generate_cursor_movement()
            return result

class FakeCMD:
    def __init__(self, duration: int = None):
        self.duration = duration
        self.spinner = Spinner()
        self.tasks = TaskManager()
        self.progress = ProgressBar()
        self.status = SystemStatus()
        self.logger = SystemLogger()
        self.network = NetworkTrafficSimulator()
        self.files = FileOperationsSimulator()
        self.processes = ProcessInfoSimulator()
        self.interactive = InteractiveSimulator()
        self.start_time = None
        self.error_chance = 0.15  # 15% chance of error
        self.unusual_colors = [
            Colors.BRIGHT_MAGENTA,
            Colors.BRIGHT_CYAN,
            Colors.BRIGHT_YELLOW,
            Colors.BRIGHT_GREEN,
            Colors.BRIGHT_BLUE,
            Colors.BRIGHT_RED
        ]

    def setup_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            os.system('mode con: cols=120 lines=40')
        except:
            pass  # Non-Windows platforms

    def log(self, message, show_progress=False):
        # Check if the message is garbled text
        if any(c in message for c in self.tasks.symbols) and len(message) > 50:
            # Use unusual color for garbled text, no timestamp
            color = random.choice(self.unusual_colors)
            sys.stdout.write(f"{color}{message}{Colors.ENDC}\n")
            sys.stdout.flush()
            return

        # Normal logging with timestamp
        timestamp = datetime.now().strftime("%H:%M:%S")
        sys.stdout.write(f"{Colors.BLUE}[{timestamp}] {Colors.ENDC}{Colors.BOLD}[*] {message} {Colors.ENDC}")
        sys.stdout.flush()
        
        if show_progress:
            # Create a new progress bar for each progress display
            self.progress = ProgressBar()
            for i in range(101):
                self.progress.update(i)
                # Vary the speed of progress
                time.sleep(random.uniform(0.01, 0.05))
            sys.stdout.write("\n")
        else:
            self.spinner.spin(delay=0.04, cycles=random.randint(10, 30))
            sys.stdout.write(f"{Colors.GREEN}done.{Colors.ENDC}\n")
        
        sys.stdout.flush()

    def show_error(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        sys.stdout.write(f"{Colors.BLUE}[{timestamp}] {Colors.ENDC}{Colors.RED}[!] Error: {message}{Colors.ENDC}\n")
        sys.stdout.flush()

    def run(self):
        self.setup_terminal()
        self.start_time = time.time()
        try:
            while True:
                # Random chance to update and display system status (10% chance)
                if random.random() < 0.02:
                    self.status.update()
                    sys.stdout.write(self.status.display())
                    sys.stdout.flush()
                
                # 40% chance to show a system log
                if random.random() < 0.4:
                    log_message = self.logger.generate_log()
                    timestamp = datetime.now().strftime("%H:%M:%S")
                    sys.stdout.write(f"{Colors.BLUE}[{timestamp}] {Colors.ENDC}{log_message}\n")
                    sys.stdout.flush()
                    time.sleep(random.uniform(0.1, 0.3))
                    continue
                
                # 30% chance to show network traffic
                if random.random() < 0.3:
                    network_log = self.network.generate_network_log()
                    timestamp = datetime.now().strftime("%H:%M:%S")
                    sys.stdout.write(f"{Colors.BLUE}[{timestamp}] {Colors.ENDC}{network_log}\n")
                    sys.stdout.flush()
                    time.sleep(random.uniform(0.1, 0.2))
                    continue
                
                # 25% chance to show file operations
                if random.random() < 0.25:
                    file_log = self.files.generate_file_operation()
                    sys.stdout.write(f"{file_log}\n")
                    sys.stdout.flush()
                    time.sleep(random.uniform(0.1, 0.2))
                    continue
                
                # 20% chance to show process information
                if random.random() < 0.2:
                    process_info = self.processes.generate_process_info()
                    sys.stdout.write(f"{process_info}\n")
                    sys.stdout.flush()
                    time.sleep(random.uniform(0.2, 0.4))
                    continue
                
                # 15% chance to show interactive elements
                if random.random() < 0.15:
                    interaction = self.interactive.generate_interaction()
                    sys.stdout.write(f"{interaction}\n")
                    sys.stdout.flush()
                    time.sleep(random.uniform(0.1, 0.2))
                    continue
                
                # Get and execute task
                task = self.tasks.get_task()
                show_progress = random.random() < 0.3  # 30% chance to show progress bar
                self.log(task, show_progress)
                
                # Random chance to show error
                if random.random() < self.error_chance:
                    error = self.tasks.get_error()
                    self.show_error(error)
                    time.sleep(random.uniform(0.5, 1.5))
                
                time.sleep(random.uniform(0.2, 1.0))

                if self.duration and (time.time() - self.start_time >= self.duration):
                    print(f"{Colors.GREEN}[+] Task duration complete. Exiting.{Colors.ENDC}")
                    break
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}[!] Interrupted by user.{Colors.ENDC}")

# Main Entry Point
if __name__ == "__main__":
    fake_cmd = FakeCMD(duration=None)  # Set duration=60 for 60 seconds
    fake_cmd.run()
