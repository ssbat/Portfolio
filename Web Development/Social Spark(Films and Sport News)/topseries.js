const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Host': 'netflix-weekly-top-10.p.rapidapi.com',
		'X-RapidAPI-Key': '42b4074ef1msheb8667320a3cd2ap16623ejsn26af3d964fe8'
	}
};

fetch('https://netflix-weekly-top-10.p.rapidapi.com/api/tv', options)
  .then(response => response.json())
  .then(data => {
    const liste = Object.values(data);

    liste.map((item) => {
      const m = Object.values(item)
      const n = m[1];
      const top = m[0];
      const names = getStringBetween(n,":")
      const name = getStringBetween(names,".")
      const url = "http://www.omdbapi.com/?t="+name+"&apikey=5cc25e0b";
      getposter(url,name,top,n);
    })
   })
  .catch(err => console.error(err));

function getposter(theUrl,name,top,n) {
	fetch(theUrl)
	.then(res => res.json())
	.then((data) => {
    let p = data["Poster"],
        y = data["Year"],
        g = data["Genre"],
        d = data["Writer"],
        desc = data["Plot"]
    const movie = `<li><img src=${p} alt="${name}"><h2>${n}</h2><p><br>Top:${top}</p><p>Year: ${y}</p>
      <p>Genre: ${g}</p><p>Writers: ${d}</p></li>`;
    document.querySelector('.movies10').innerHTML += movie;
    })
}

function getStringBetween(str,x) {
    const index = findLastIndex(str,x)
    var res = str.substring(0,index);
    return res;
}


function findLastIndex(str,x){
    var index = str.length;
    for (i = 0; i < str.length; i++)
        if (str.charAt(i) == x)
            index = i;
    return index;
}