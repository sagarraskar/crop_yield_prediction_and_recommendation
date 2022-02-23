import React from 'react';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';

import Home from './components/Home';
import Predict from './components/Predict';
import Recommend from './components/Recommend';


import {AppBar, Toolbar, Typography} from '@mui/material';


function App() {
  return (
    <Router>
      <div className="App">
        <AppBar position="sticky">
          <Toolbar>
            <Typography variant="h6" color="inherit">
              Crop Yield Predictor And Recommender
            </Typography>
          </Toolbar>
        </AppBar>
        <Routes>
          <Route exact path='/' element={<Home />} />
          <Route path='/predict' element={<Predict />} />
          <Route path='/recommend' element={<Recommend />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
