const axios = require('axios');

const apiUrl = 'https://min-api.cryptocompare.com/data/pricehistorical';
const fsym = 'ETH'; 
const tsyms = 'USD';
const ts = 1452680400; 
axios.get(apiUrl, {
  params: {
    fsym: fsym,
    tsyms: tsyms,
    ts: ts
  }
})
.then(response => {
  const data = response.data;
  console.log('Price Data:', data);
})
.catch(error => {
  console.error('Error:', error);
});









