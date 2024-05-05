<!-- pages.svelte -->
<script>
    let city = '';
    let weatherData = {};

    async function getWeather() {
        const response = await fetch(`http://localhost:5000/api/weather?city=${city}`);
        weatherData = await response.json();
        console.log(weatherData);
        console.log(city);
    }
</script>

<main>

<div class="container">
    <input type="text" bind:value={city} placeholder="Enter city">
    <button on:click={getWeather}>Get Weather</button>

    {#if Object.keys(weatherData).length > 0 }
        <div class="weather-info">
            <h2>Weather Information</h2>
            <h2> {weatherData.name}</h2>
            <p> Temperature: <b>  {weatherData.main.temp} °C</b></p>
            <p>Feels Like: <b>  {weatherData.main.feels_like} °C</b></p>
            <p>Min Temp: <b>  {weatherData.main.temp_min} °C</b></p>
            <p>Max Temp: <b>  {weatherData.main.temp_max}  °C</b></p>
            <p>Description: <b>  {weatherData.weather[0].description} </b></p>
            <p> Wind Speed: <b>  {weatherData.wind.speed} Km/hr </b></p>
            <p>Humidity: <b>  {weatherData.main.humidity} % </b></p>
            <p>Air Pressure: <b>  {weatherData.main.pressure} Pa </b></p>
        </div>
    {/if}
</div>
</main>


<style>


main{
    font-family: Arial, sans-serif;
    background-image: url('../images/weatherimg.jpeg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    height: 100vh; 
    width: 100%;
    margin:0px; 
    padding: 0px;
    overflow: hidden;

}
.container {

    max-width: 400px;
    margin: 30px auto;
    text-align: center;
    padding: 20px;
    background-color: rgba(255, 255, 255, 0.5); 
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.3); 

}

h2{
    font-size: 24px;
}

input[type="text"] {
    width: 50%;
    padding: 10px;
    margin: 10px 0;
    border: 1px solid #ccc;
    border-radius: 5px;
    outline: none;
}

button {
    background-color: #007BFF;
    color: #fff;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

.weather-info {
    margin-top: 20px;
}

.weather-info p {
    margin-bottom: 10px; 
}

</style>