const axios = require('axios');
const cheerio = require('cheerio');

// Make the request
const domain = "https://www.jules.com";
const url = domain + "/fr-fr/l/pull/?sz=144";

axios.get(url)
    .then(response => {
        // console.log(response);
        getData(response.data);
    })
    .catch(error => {
        console.log(error);
    })

// Using cheerio.js to parse HMTL
let getData = html => {
    data = [];
    const $ = cheerio.load(html);
    $('div.product').each((i, element) => {
        data.push({
            'name': $(element).find('h2 a').text(),
            'url_onmouseover': ($(element).find('img').attr('onmouseover')) ? $(element).find('img').attr('onmouseover').split("'")[1] : null,
            'url_onmouseout': ($(element).find('img').attr('onmouseout')) ? $(element).find('img').attr('onmouseout').split("'")[1] : null,
            'url_img': ($(element).find('img').attr('data-src')) ? $(element).find('img').attr('data-src') : null,
            'price_striked': ($(element).find('div.price p.strike-through.list span')) ? $(element).find('div.price p.strike-through.list span').attr('content') : null,
            'price': ($(element).find('p.sales span.value')) ? $(element).find('p.sales span.value').attr('content') : null,
            'percent_reduc': ($(element).find('span.percent')) ? $(element).find('span.percent').text().trim() : null

        })
    });
    // console.log(data.length);
    console.log(data);
}