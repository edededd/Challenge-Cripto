const axios = require('axios');

async function getSwaps(tokenA, tokenB) {
  try {
    const query = `
    {
        swaps(
          orderBy: timestamp
          orderDirection: desc
        ) {
          id
          timestamp
          amount0In
          amount0Out
          amount1In
          amount1Out
          pair {
            token0 {
              symbol
            }
            token1 {
              symbol
            }
          }
        }
      }
    `;

    const response = await axios.post('https://api.thegraph.com/subgraphs/name/sushiswap/exchange', { query });
    const swaps = response.data.data.swaps;

    console.log('Swaps:', swaps);
  } catch (error) {
    console.error('Error:', error);
  }
}


const tokenASymbol = '0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599';
const tokenBSymbol = '0x3472A5A71965499acd81997a54BBA8D852C6E53d';

getSwaps(tokenASymbol, tokenBSymbol);