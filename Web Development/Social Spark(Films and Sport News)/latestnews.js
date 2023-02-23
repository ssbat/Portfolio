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
		while (i < 3) {
                const item = response[i];
                const t = item["title"]
                const img = item["image"]
                const l = item["link"]
                const d = item["date"]
                const result1 = `<li><div class="latestnews"><div class="latestpics"><a href=${l}><img src=${img}></a></div>
                                 <div class="latesttext"><pg style="text-decoration: none;">${t}</pg></div></div></li>`;
                                document.querySelector('.latestnewsg').innerHTML += result1;
                i++;
        }
    })
	



	.catch(err => console.error(err));