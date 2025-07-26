import json
from eth_account import Account

# Aktifkan fitur HD Wallet
Account.enable_unaudited_hdwallet_features()

# Generate mnemonic 12 kata dan buat wallet
mnemonic = Account.create_with_mnemonic(num_words=12)[1]
hd_path = "m/44'/60'/0'/0/0"
acct = Account.from_mnemonic(mnemonic, account_path=hd_path)

# Ambil informasi wallet
wallet_info = {
    "mnemonic": mnemonic,
    "hd_path": hd_path,
    "address": acct.address,
    "private_key": acct.key.hex(),
    "network": "Ethereum Mainnet"
}

# Tampilkan ke terminal
print("=== Wallet EVM ===")
for key, value in wallet_info.items():
    print(f"{key}: {value}")

# Simpan ke file JSON
suffix = acct.address[-8:]
filename = f"wallet_{suffix}.json"
with open(filename, 'w') as f:
    json.dump(wallet_info, f, indent=4)

print(f"\nWallet saved to {filename}")