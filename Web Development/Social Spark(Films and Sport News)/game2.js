const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Host': 'videogames-news2.p.rapidapi.com',
		'X-RapidAPI-Key': '42b4074ef1msheb8667320a3cd2ap16623ejsn26af3d964fe8'
	}
};

fetch('https://videogames-news2.p.rapidapi.com/videogames_news/recent', options)
	.then(response => response.json())
	.then(response => {
		let i=0
		while (i < 7) {
                const item = response[i];
                const t = item["title"]
                const img = item["image"]
                const l = item["link"]
                const d = item["date"]
                const result = `<li><a href=${l}><img src=${img}></a><a href=${l} style="text-decoration: None;"><pg>${t}</pg></a><pc>${d}</pc></li>`;
                                document.querySelector('.gamingnews1').innerHTML += result;
                i++;
        }
        while (i < 10) {
        	const item = response[i];
                const t = item["title"]
                const img = item["image"]
                const l = item["link"]
                const result = `<li><a href=${l}><img src=${img}></a><a href=${l} style="text-decoration: None;"><pg>${t}</pg></a></li>`;
                                document.querySelector('.gamenews1').innerHTML += result;
                i++;
        }
    })
	



	.catch(err => console.error(err));