const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Host': 'covid-193.p.rapidapi.com',
		'X-RapidAPI-Key': '42b4074ef1msheb8667320a3cd2ap16623ejsn26af3d964fe8'
	}
};

fetch('https://covid-193.p.rapidapi.com/statistics', options)
	.then(response => response.json())
	.then(response => {
		console.log(response)
		const r = response["response"]
		for (i in r){
			const c = r[i]["country"];
			const p = r[i]["population"];
			const tca = r[i]["cases"]["total"];
			const tre = r[i]["cases"]["recovered"];
			const nca = r[i]["cases"]["new"];
			const aca = r[i]["cases"]["active"];
			const cca = r[i]["cases"]["critical"];
			const tde = r[i]["deaths"]["total"];
			const nde = r[i]["deaths"]["new"];
			const tte = r[i]["tests"]["total"];

			var result = `<li style="text-decoration: none;list-style: none"><tr><th>${c}</th><th style="text-align: center">${p}</th><th style="text-align: center">${tca}</th><th style="text-align: center">${nca}</th><th style="text-align: center">${aca}</th>
			              <th style="text-align: center">${cca}</th><th style="text-align: center">${tde}</th><th style="text-align: center">${nde}</th><th style="text-align: center">${tre}</th><th style="text-align: center">${tte}</th></tr></li>`
	        document.querySelector('tbody').innerHTML += result;
        }
        const dat = r[0]["day"]
        var d = `<li><h1>${dat}</h1></li>`
        document.querySelector('.date').innerHTML = d;
	})
	.catch(err => console.error(err));
