// src/components/WeatherComponent.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './WeatherComponent.css'; // Import CSS for styling

const WeatherComponent = () => {
  const [weatherData, setWeatherData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchWeatherData = async () => {
      try {
        const response = await axios.get('http://localhost:5000/weather');
        setWeatherData(response.data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching weather data:', error);
        setLoading(false);
      }
    };

    fetchWeatherData();
  }, []);

  return (
    <div className="weather-container">
      <h1>Weather Information</h1>
      {loading ? (
        <p>Loading...</p>
      ) : (
        weatherData && (
          <div className="weather-details">
            <p><strong>Location:</strong> {weatherData.location.name}, {weatherData.location.country}</p>
            <p><strong>Temperature:</strong> {weatherData.temperature} °C</p>
            <p><strong>Cloudiness:</strong> {weatherData.cloud} %</p>
            <p><strong>Humidity:</strong> {weatherData.humidity} %</p>
            <p><strong>Pressure:</strong> {weatherData.pressure} hPa</p>
            <p><strong>Wind:</strong> {weatherData.wind.speed} m/s, {weatherData.wind.deg}°</p>
          </div>
        )
      )}
    </div>
  );
};

export default WeatherComponent;

// // src/components/WeatherComponent.js
// import React, { useState, useEffect } from 'react';
// import axios from 'axios';

// const WeatherComponent = () => {
//   const [weatherData, setWeatherData] = useState(null);
//   const [loading, setLoading] = useState(true);

//   useEffect(() => {
//     const fetchWeatherData = async () => {
//       try {
//         const response = await axios.get('http://localhost:5000/weather');
//         setWeatherData(response.data);
//         setLoading(false);
//       } catch (error) {
//         console.error('Error fetching weather data:', error);
//         setLoading(false);
//       }
//     };

//     fetchWeatherData();
//   }, []);

//   return (
//     <div className="weather-container">
//       <h1>Weather Information</h1>
//       {loading ? (
//         <p>Loading...</p>
//       ) : (
//         weatherData && (
//           <div className="weather-details">
//             <p><strong>Location:</strong> {weatherData.location.name}, {weatherData.location.country}</p>
//             <p><strong>Temperature:</strong> {weatherData.temperature} °C</p>
//             <p><strong>Cloudiness:</strong> {weatherData.cloud} %</p>
//             <p><strong>Humidity:</strong> {weatherData.humidity} %</p>
//             <p><strong>Pressure:</strong> {weatherData.pressure} hPa</p>
//             <p><strong>Wind:</strong> {weatherData.wind.speed} m/s, {weatherData.wind.deg}°</p>
//           </div>
//         )
//       )}
//     </div>
//   );
// };

// export default WeatherComponent;
