const express = require('express');
const fetch = require('node-fetch');
const csvtojson = require('csvtojson');

const app = express();
const csvUrl = "https://raw.githubusercontent.com/cem1000/DublinBikeAvailability/main/dublinbikes.csv";

app.get('/api/bikes', async (req, res) => {
  try {
    const response = await fetch(csvUrl);
    const csvData = await response.text();
    const jsonData = await csvtojson().fromString(csvData);
    res.json(jsonData);
  } catch (error) {
    console.error(error);
    res.status(500).send('Error retrieving the data');
  }
});

const port = process.env.PORT || 3000;
module.exports = app;
});
