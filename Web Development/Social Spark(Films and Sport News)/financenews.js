const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Host': 'mboum-finance.p.rapidapi.com',
		'X-RapidAPI-Key': '42b4074ef1msheb8667320a3cd2ap16623ejsn26af3d964fe8'
	}
};

fetch('https://mboum-finance.p.rapidapi.com/ne/news', options)
	.then(response => response.json())
	.then(response => {
		for (item of response){
			const data = Object.values(item)
			const t = data[0]
			const s = data[3]
			const p = data[2]
			const l = data[1]
			const result = `<li><a href="${l}"><p5>${t}<br><br><br></p5></a>
                        <p3>${s}<br>${p}</p3></li>`
            document.querySelector('.finance2').innerHTML += result;
		}
	})
	.catch(err => console.error(err));