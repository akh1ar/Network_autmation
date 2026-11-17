# Cisco Python Network Automation

Hands-on Python network automation examples for Cisco IOS/IOS XE labs, using **Netmiko (SSH)** and **ncclient (NETCONF)**. The project demonstrates VLAN provisioning, discovery of NETCONF capabilities, retrieval of YANG-modeled interface data, and basic IPv4 address classification. An Alpine Linux setup script is included for preparing a lightweight automation host.

> **Lab project:** These examples were developed from learning scripts. They are not a production-ready orchestration platform. Run configuration changes only on devices you own or have permission to manage.

## Features

- **VLAN automation:** Create VLANs 80 through 89 with names `MY_VLAN_80`–`MY_VLAN_89` on a Cisco IOS switch.
- **NETCONF discovery:** Connect to an IOS XE device and print supported server capabilities.
- **NETCONF interface retrieval:** Query IETF interface configuration/state using an XML subtree filter and format selected fields.
- **IPv4 classification:** Recognize multicast, unicast, limited broadcast, and subnet-directed broadcast addresses.
- **Alpine Linux setup:** Prepare a Python virtual environment and dependencies on an Alpine lab machine.

## Tools and Technologies

Python 3, Cisco IOS/IOS XE, SSH, Netmiko, ncclient, NETCONF/YANG, XML, xmltodict, Alpine Linux, IPv4.

## Repository Structure

```text
Cisco-Python-Network-Automation/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── config_notes.md
├── device_info.py
├── IOSXE_8kv_sandbox.py
├── NETCONF_FILTER.py
├── filter-ietf-interfaces.xml
├── ipv4-primary_modes.py
├── scripts/
│   ├── __init__.py
│   ├── vlan_automation.py
│   └── alpine_setup.sh
└── tests/
    └── test_ipv4_modes.py
```

## Prerequisites

- Python 3.10+ recommended
- Access to a Cisco IOS switch with SSH and privilege to configure VLANs, for the VLAN example
- Access to a NETCONF-enabled Cisco IOS XE device on TCP port 830, for the NETCONF examples
- Correct IP addresses, credentials, and network reachability

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/Cisco-Python-Network-Automation.git
   cd Cisco-Python-Network-Automation
   ```

2. Create a virtual environment and install dependencies:

   **Linux/macOS**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   python -m pip install -r requirements.txt
   ```

   **Windows (PowerShell)**
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
   ```

3. Create a local environment file from the template:

   **Linux/macOS**
   ```bash
   cp .env.example .env
   ```

   **Windows (PowerShell)**
   ```powershell
   Copy-Item .env.example .env
   ```

4. Edit `.env` with your own lab IP addresses and credentials. **Never commit `.env`.**

## Usage

### 1. NETCONF Capabilities

```bash
python IOSXE_8kv_sandbox.py
```

Prints advertised NETCONF server capabilities for the configured IOS XE device.

### 2. NETCONF Interface Query

```bash
python NETCONF_FILTER.py
```

Uses `filter-ietf-interfaces.xml` to query interface configuration and state. Some IOS XE versions no longer expose the legacy `ietf-interfaces` state subtree, so adapt the filter to the device's supported YANG models if needed.

### 3. VLAN Automation (changes device configuration)

```bash
python -m scripts.vlan_automation
```

Creates VLANs 80–89 on the switch configured as `SW1` in `.env`. Review VLAN IDs and names before using it. It does not save startup configuration automatically.

### 4. IPv4 Transmission Types

```bash
python ipv4-primary_modes.py
```

Example output:

```text
Unicast
Broadcast
Multicast
```

For directed broadcast detection, a subnet such as `192.168.1.0/24` is required; `.255` alone does **not** always mean broadcast.

### 5. Alpine Linux Lab Setup

The original manually executed Alpine commands have been adapted to `scripts/alpine_setup.sh`. Review the script and run it on an Alpine lab VM as root:

```bash
sh scripts/alpine_setup.sh
. /root/network-automation-venv/bin/activate
pip install -r requirements.txt
```

## Testing

The IPv4 tests do not require connecting to lab devices:

```bash
python -m unittest discover -s tests -v
```

## Security

The source files originally contained lab passwords. They have been removed from the public-ready files; credentials now come from `.env`. Rotate any active passwords that were embedded in the originals. NETCONF host-key verification is set to `false` in the sample config **only for isolated labs**. See [Security & Configuration Notes](config_notes.md).

## Learning Outcomes

Practice Python automation, SSH-based device configuration, NETCONF/YANG discovery, structured XML retrieval, handling secret configuration separately from code, and network address fundamentals.

## Future Improvements

- Validate reachability before opening connections
- Add structured logging and exception handling
- Support multiple devices from an inventory
- Add per-device backups and configuration diff/review
- Replace legacy IETF interface-state queries where necessary
- Add mock-based network automation tests

## License

No license has been selected. Contact the repository owner for reuse permissions. Add a license file if you wish to permit redistribution or modification.
