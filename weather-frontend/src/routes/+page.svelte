<!-- pages.svelte -->
<script>
    let city = "";
  let weatherData = {};
  let citySuggestions = [];
  let showSuggestions = false;

    async function getWeather() {
        const response = await fetch(`http://localhost:5000/api/weather?city=${city}`);
        weatherData = await response.json();
        console.log(weatherData);
        console.log(city);
    }

    
  async function getCitySuggestions(keyword) {
    const response = await fetch(
      `http://localhost:5000/api/cities?keyword=${keyword}`
    );
    citySuggestions = await response.json();
    console.log(citySuggestions);
  }

  function handleInput(event) {
    const keyword = event.target.value.trim();
    if (keyword !== "") {
      getCitySuggestions(keyword);
      showSuggestions = true;
    } else {
      citySuggestions = [];
      showSuggestions = false;
    }
  }

   /*  Function to handle selection of a city suggestion */
   function handleSuggestionClick(cityName) {
    city = cityName;
    showSuggestions = false;
    getWeather();
  }

</script>

<main>

  <div class="container">
    <div class="input-container">
      <input type="text" bind:value={city} placeholder="Enter city" on:input={handleInput} />
      <button on:click={getWeather}>Get Weather</button>
      <!-- Suggestions dropdown -->
    {#if showSuggestions && citySuggestions.length > 0}
    <ul class="suggestions">
      {#each citySuggestions as suggestion}
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
        <li on:click={() => handleSuggestionClick(suggestion)}>{suggestion}</li>
      {/each}
    </ul>
  {/if}
    </div>

    
  {#if Object.keys(weatherData).length > 0}
  <div class="weather-info">
    <div class="temperature-info">
      <p class="temperature">{weatherData.main.temp}°</p>
      <p class="feels-like">Feels Like: {weatherData.main.feels_like}°C</p>
      <p class="city-info">{weatherData.name}</p>
    </div>
    <div class="weather-details">
      <div class="left-details">
        <p>Min Temp: {weatherData.main.temp_min}°C</p>
        <p>Max Temp: {weatherData.main.temp_max}°C</p>
        <p>Air Pressure: {weatherData.main.pressure} P</p>
      </div>
      <div class="right-details">
        <p>Humidity: {weatherData.main.humidity}%</p>
        <p>Wind Speed: {weatherData.wind.speed} Km/hr</p>
      </div>
    </div>
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
    position: relative;


}

p{
    font-size: 24px;
    text-align: center;
}

input[type="text"] {
    font-size: 18px;
    width: 50%;
    padding: 10px;
    margin: 10px 0;
    border: 1px solid #ccc;
    border-radius: 5px;
    outline: none;
    position: relative;
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

.city-info {
    font-size: 1.1rem;
  }

  .temperature-info {
    flex: 1;
    text-align: center;
  }

  .temperature {
    font-size: 3rem;
    margin-bottom: 10px;
  }

  .feels-like {
    font-size: 1rem;
  }

  .weather-details {
    flex: 1;
    display: grid;
    grid-template-rows: repeat(2, 1fr);
    gap: 10px;
    text-align: left;
  }

  .suggestions {
  position: absolute;
  width: auto; /* Set width to auto to fit content */
  width: 50%; /* Set max-width to 100% to prevent overflow */
  max-height: 200px;
  overflow-y: auto;
  border: 1px solid #ccc;
  border-top: none;
  background-color: #fff;
  z-index: 1;
  margin-top: 10px; /* Adjust margin top to create space between input and dropdown */
  padding-left: 0;
  list-style-type: none;
  position: absolute;
  text-align: left;
  left: 50px; /* Align dropdown with left edge of input */
  top:55px;
  border-radius: 5px;
}
  .suggestions li {
    padding: 5px 10px;
    cursor: pointer;
  }

  .suggestions li:hover {
    background-color: #f0f0f0;
  }
</style>