const site1 = 'https://api.openweathermap.org/data/2.5/weather?q=';
const site2 ='&appid=169754886df2a0fd1511c01cd2309818'

const list = ["Beirut","Riyadh","Cairo","Baghdad","Amman","Muscat","Damascus","Abu Dhabi",
              "Kuwait","Sanaa","Doha","Ramallah","Nicosia","Manama"]
for (item of list) {
    const api_url = site1 + item + site2;
    async function getapi(url) {
        const response = await fetch(url);
        var data = await response.json();
        
        const n = data["name"]
        const w = data["weather"]
        const ma = w[0]["main"]
        const des = w[0]["description"]
        const des1 = des.charAt(0).toUpperCase() + des.slice(1); 
        const m = data["main"]
        const temperature = m["temp"]
        const result = `<li><img src="countries/${n}.png" alt="${n}"><h2>${n}</h2><p>Description: ${des1}</p>
                        <p>Weather: ${ma}</p><p>Temperature: ${(temperature-273.15).toFixed(2)} °C</p></li>`
        document.querySelector('.weather').innerHTML += result;
    }
    getapi(api_url);
}



