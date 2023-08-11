import os
from web3 import Web3
from dotenv import load_dotenv
import requests
load_dotenv()

infura_key = os.environ.get('API_KEY')

infura_url = f"https://mainnet.infura.io/v3/{infura_key}"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Dirección del contrato Uniswap V2 Router 2 en la cadena Ethereum
uniswap_router_2_address = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"

# Obtener el bloque más reciente
latest_block_number = web3.eth.block_number

# Definir el umbral de slippage para identificar high slippage swaps
slippage_threshold = 0.05  # Puedes ajustar este valor según tus necesidades

# Filtrar las transacciones en el contrato Uniswap V2 Router 2
high_slippage_swaps = []

for block_number in range(latest_block_number - 1, latest_block_number + 1):
    block = web3.eth.get_block(block_number)
    transactions = block['transactions']
    
    for tx_hash in transactions:
        
        tx = web3.eth.get_transaction(tx_hash)
        if tx and tx['to'] == uniswap_router_2_address:
            # Calcular slippage para la transacción
            expected_amount = 2  # Calcula el expected_amount (depende del caso)
            actual_amount = tx['value']
            slippage = (actual_amount - expected_amount) / expected_amount
            
            # Verificar si es un high slippage swap
            if slippage > slippage_threshold:
                high_slippage_swaps.append(tx)
                
                
# Imprimir los high slippage swaps identificados
for swap in high_slippage_swaps:
    print("Transacción:", swap['hash'].hex())
    print("Valor:", swap['value'])
    print("Remitente:", swap['from'])
    print("Receptor:", swap['to'])
    print("Slippage:", slippage)
    print()
# Direcciones de los tokens DAI y ETH
#dai_address = "0x6B175474E89094C44Da98b954EedeAC495271d0F"
#eth_address = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"