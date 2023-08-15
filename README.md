# Challenge-Crypto
# Liquidity and AMM Challenge

## Question 1: 

To identify and report high slippage swaps from three different AMMs, we follow a slippage calculation process. Firstly, we require the actual price of a specific token X at a given timestamp. This value is obtained using the CryptoCompare API. However, locating this value can be complex, as there are no readily available functions providing historical data. If such functions exist, they typically offer real-time values, as seen in the SushiSwap API.

Subsequently, we proceed to compute the slippage by applying the formula  (Execution Price - Expected Price) / Expected Price. It's worth noting that this methodology diverges from the typical behavior of AMMs, where the automated trading market calculates anticipated trade values. We consider high slippage if the result is more or equal to 0.9%.

For our calculations, we've selected three prominent AMMs: Uniswap v2, Uniswap v3, and SushiSwap. For each case, we utilize the CryptoCompare API to determine the actual value of coin X at a specific moment.

**For Uniswap V2:** We've selected the FOX and ETH coins. The swap involved 3.3081553221339284 ETH for 312,171.332655604731542489 FOX, as observed on [this page](https://etherscan.io/tx/0x00d7752c3d5e055989dd408225ccf845855936b5ac7d79bd0863f80ba66175d8/). To calculate the actual ratio of these coins at that moment, we executed the code historicalPrice.js. The result was calculated as (94364 - 92186) / 92186 = 2.36% (high slippage).

**For SushiSwap:** We've selected the ALCX and ETH coins. The swap involved 2.284340461227795491 ETH for 309.770068188940186052 ALCX, as seen on [this page](https://etherscan.io/tx/0x728d1ab45b6e7fa6886abe4f66d411b3288b6ce6ed3ae919cb55b735e8c8beb8). To calculate the actual ratio of these coins at that moment, we executed the code historicalPrice.js. The result was calculated as (135.6 - 138.4) / 138.4 = -2.02% (high slippage).

**For Uniswap V3:** We've selected the FTM and ETH coins. The swap involved 16,787.84125611425420293 FTM for 2.177133049503625197 ETH, as observed on [this page](https://etherscan.io/tx/0xc4c1bf4c187847f9ba303e62f28b76c4f5c08ebff54cb3604ca49613160b3405). To calculate the actual ratio of these coins at that moment, we executed the code historicalPrice.js. The result was calculated as (7710.98 - 7638.25) / 7638.25 = 0.95% (high slippage).





## Question 2: Traditional AMM vs. Concentrated Liquidity

**Describe how a traditional AMM (like Uniswap V2) works compared to one with concentrated liquidity.**

A traditional Automated Market Maker (AMM) operates according to the Constant Function Market Maker (CFMM) law between two currencies, X and Y. This mathematical formula maintains a constant product of the value of the function applied into X and Y in the liquidity pool, facilitating trades and valuations across a broad spectrum of price ranges. For example, Uniswap V2, a traditional AMM, employs the constant function market maker with a constant product between the quantity of X and Y. In specific terms, if 'x' and 'y' denote the amounts of assets X and Y within the pool at a given moment, their product, 'x * y,' remains constant as 'k' (where 'k' is a fixed numerical value).

In the context of concentrated liquidity, exemplified by Uniswap V3, the AMM retains its core attributes while introducing a significant distinction: liquidity providers gain the ability to manually select specific price ranges within which their contributed currency will be actively utilized for trading. This innovative feature empowers liquidity providers, offering them the flexibility to optimize their exposure to trading activity, potentially leading to higher returns. By strategically choosing price ranges, providers can align their positions with areas of market interest, capitalizing on opportunities within distinct price bands and enhancing their potential for profitability.



## Limitations
I have tried to obtain this with the assistance of various APIs, but they are quite limited in their usability and somewhat challenging to interpret, such as the GraphQL or Ethereum API. Nonetheless, they can prove useful in uncovering other patterns, like sets of transactions between specific pairs of coins. This has been a constraint I've encountered in recent days while tackling this challenge, but I have gained valuable insights and I believe that in future projects, the required time would be significantly reduced. You can see some examples of how to find these transactions in getSwaps.js and uniswap.js.

## Installation

To run this code, you'll need to have Node.js and npm (Node Package Manager) installed on your machine. If you don't have them installed, you can download and install them from the official Node.js website: [Node.js Downloads](https://nodejs.org/en/download/).

Once you have Node.js and npm installed, follow these steps:

1. Clone this repository: git clone https://github.com/edededd/Challenge-Cripto
2. Navigate to the project directory:
3. Install the required dependencies: 
  - npm install axios
  - npm install web3
4. Execute the code: node historicalPrice.js

## Testing
In historicalPrice.js, you can set the variables for obtain the ratio of price between two coins. In fsym and tsyms you can set the name of the coins, and in ts you can set the timestamp. 


 