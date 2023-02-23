const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Host': 'cryptocurrency-price.p.rapidapi.com',
		'X-RapidAPI-Key': '42b4074ef1msheb8667320a3cd2ap16623ejsn26af3d964fe8'
	}
};

fetch('https://cryptocurrency-price.p.rapidapi.com/', options)
	.then(response => response.json())
    .then(data => {
    const liste = Object.values(data);
    liste.map((item) => {
      const m = Object.values(item)
      for (let i = 0; i < m.length; i++){
      	const n = m[i]["name"]
      	var newname = n.substring(0,n.lastIndexOf(i+1));
      	var picname = newname
      	if (newname === "USD Coin"){
      		var picname = "USDCoin"
      	}
      	const cur = `<li><img src=Currency/${picname}.png alt="${newname}"><h2>Name: ${newname}</h2><p><br>Rank: ${m[i]["rank"]}</p>
      	             <p>Price: ${m[i]["price"]}</p></li>`;
        document.querySelector('.finance').innerHTML += cur;
      }
  })
})

const list = ["gold","silver","platinum","palladium"]
async function getapi(item) {
        const response = await fetch("https://api.metals.live/v1/spot");
        var data = await response.json();
        console.log(data)
        const m = list.indexOf(item, 0)
        const n = item
        const p = data[m][n]
        const N = n.charAt(0).toUpperCase() + n.slice(1);
        const result = `<li><h2>${N}</h2><p>Price: ${p}$</p></li>`
        document.querySelector('.finance1').innerHTML += result;
    }
for (item of list) {
	console.log(item)
    getapi(item);
}

const list1 = ["iridium","rhodium","ruthenium","lead","aluminum","copper","nickel","tin","zinc","cobalt","bronze","brass"]
async function getapi2(item) {
        const response = await fetch("https://api.metals.live/v1/spot/commodities");
        var data = await response.json();
        console.log(data)
        const m = list1.indexOf(item, 0)
        const n = item
        const p = data[m][n]
        const N = n.charAt(0).toUpperCase() + n.slice(1);
        const result = `<li><h2>${N}</h2><p>Price: ${p}$</p></li>`
        document.querySelector('.finance1').innerHTML += result;
    }
for (item of list1) {
	console.log(item)
    getapi2(item);
}