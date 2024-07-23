// src/App.js
import React from 'react';
import './App.css';
import WeatherComponent from './components/WeatherComponent';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Weather App</h1>
      </header>
      <main className="App-main">
        <WeatherComponent />
      </main>
    </div>
  );
}

export default App;


// // src/App.js
// import React from 'react';
// import './App.css';
// import WeatherComponent from './components/WeatherComponent';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <WeatherComponent />
//       </header>
//     </div>
//   );
// }

// export default App;
