const sushi = require('@sushiswap/sushi-data'); // common js

async function getPairDailyData(pairAddress) {
  try {
    const e = await sushi.exchange.pair({pair_address:"0xa30911e072a0c88d55b5d0a0984b66b0d04569d0"})
    console.log(e)
    const g = await sushi.exchange.pair24h({pair_address:"0xa30911e072a0c88d55b5d0a0984b66b0d04569d0"})
    //console.log(g)
    const f = await sushi.masterchef.pools()
    //console.log(f)
    const x= await sushi.blocks.latestBlock()
    //console.log(x)
    const y = await sushi.exchange.ethPrice()
    //console.log(y)

    const z =await sushi.blocks.getBlock({block: 17886863, timestamp:1691699219})
    console.log(z)
        // Obtiene datos históricos diarios para el par de tokens especificado
    const pairDailyData = await sushi.charts.pairDaily({ pair_address: pairAddress });
    
    // Imprime los datos históricos
    //console.log(`Datos históricos diarios para el par de tokens en dirección: ${pairAddress}`);
    console.log(pairDailyData[pairDailyData.length-1]);


  } catch (error) {
    console.error('Ocurrió un error:', error);
  }
}

// Dirección del contrato del par de tokens que deseas analizar
const pairAddress = '0x2170ed0880ac9a755fd29b2688956bd959f933f8'; // Ejemplo: ETH/DAI pair

// Llama a la función para obtener los datos históricos diarios del par de tokens
getPairDailyData(pairAddress);
