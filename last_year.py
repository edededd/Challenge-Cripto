import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

infura_key = os.environ.get('API_KEY')

infura_url = f"https://mainnet.infura.io/v3/{infura_key}"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Dirección del contrato Uniswap V2 en la cadena Ethereum
uniswap_contract_address = "0x1f98431c8ad98523631ae4a59f267346ea31f984"
checksum_address = Web3.to_checksum_address(uniswap_contract_address)

end_of_2022 = 1672531199
init_of_2022 = 1641052800
# Obtener el bloque más reciente
latest_block = web3.eth.get_block_number(end_of_2022)
init_block = web3.eth.get_block_number(init_of_2022)

filter_params = {
    "fromBlock": init_block + 1,
    "toBlock": latest_block,
    "address": checksum_address
}
transactions = web3.eth.get_logs(filter_params)

max_value_transaction = None
max_value = 0

for tx in transactions:
    tx_hash = tx["transactionHash"]
    tx_receipt = web3.eth.get_transaction(tx_hash)
    print(tx_receipt["value"])
    if tx_receipt and tx_receipt["value"] > max_value:
        max_value = tx_receipt["value"]
        max_value_transaction = tx_receipt

if max_value_transaction:
    print("Transacción de mayor valor:")
    print("Hash:", max_value_transaction["hash"].hex())
    print("Valor:", max_value_transaction["value"])
    print("Remitente:", max_value_transaction["from"])
    print("Receptor:", max_value_transaction["to"])
else:
    print("No se encontraron transacciones en el último año.")
