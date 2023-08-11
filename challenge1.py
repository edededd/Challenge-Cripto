from web3 import Web3
import requests
import os
from dotenv import load_dotenv

load_dotenv()

infura_key = os.environ.get('API_KEY')

# Conectar a la red Ethereum a través de Infura (requiere tu propio Infura Project ID)
infura_url = f"https://mainnet.infura.io/v3/{infura_key}"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Dirección del contrato para el que deseas obtener eventos
contract_address = Web3.to_checksum_address("0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f")
# Obtener el bloque más reciente
latest_block = web3.eth.block_number

# Calcular el bloque desde hace una semana (aproximadamente 60480 bloques en una semana)
one_week_ago_block = latest_block - 20000

# Crear un objeto de filtro de eventos para el contrato
event_filter = web3.eth.filter({
    "fromBlock": one_week_ago_block,
    "toBlock": latest_block,
    "address": contract_address,
    "topic": "0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d822"
})

# Obtener todos los eventos del contrato en el rango de bloques especificado
contract_events = event_filter.get_all_entries()

high_slippage_threshold = 5  # Umbral de slippage alto en porcentaje

# Procesar eventos de "Swap" y calcular slippage
i=0
for event in contract_events:
    print(event)
    i=i+1
print(i)

