# EVM Wallet Generator

A simple Python script to generate an Ethereum (EVM) wallet using a 12-word mnemonic phrase. It prints the address, private key, and mnemonic to the terminal and automatically saves the wallet data to a JSON file.

## Features

- Generates an EVM-compatible wallet following BIP-44 standard
- 12-word mnemonic phrase (BIP-39)
- Derivation path: m/44'/60'/0'/0/0
- Outputs address, private key, and mnemonic to terminal
- Automatically saves data to a JSON file named wallet_<last-8-chars-of-address>.json

## Setup and Usage Guide (Linux, macOS, Windows)

```bash
# 1. Clone the repository
git clone https://github.com/denzuqo/evm-wallet-generator.git
cd evm-wallet-generator

# 2. Create a virtual environment
python3 -m venv venv  # Use 'python' instead of 'python3' if necessary

# 3. Activate the virtual environment
# For Linux/macOS:
source venv/bin/activate

# For Windows (Command Prompt):
venv\Scripts\activate

# For Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# 4. Install required dependencies
pip install web3 eth-account

# 5. Run the wallet generator script
python wallet_gen.py
```

## Output

The script will display the following information in the terminal:
- 12-word mnemonic phrase
- Ethereum wallet address
- Private key
- Derivation path
- It also saves the wallet information into a JSON file

Example output:
```
Mnemonic      : milk banner buyer ...
Derivation PB : m/44'/60'/0'/0/0
Address       : 0x1234567890abcdef1234567890abcdef12345678
Private Key   : 0xabcdef...
Wallet saved to wallet_ef123456.json
```

The JSON file such as wallet_ef123456.json will be saved in the current working directory.

## Disclaimer

This script is intended for educational and development purposes only. Do not use it to store real assets or funds permanently.

## License

MIT License. Free to use, modify, and distribute.
