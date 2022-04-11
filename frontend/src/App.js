import React, { Suspense, Component } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import { withTranslation } from 'react-i18next';

import Home from './components/Home';
import Predict from './components/Predict';
import Recommend from './components/Recommend';


import { AppBar, Toolbar, Typography, Box } from '@mui/material';
import LanguageMenu from './components/LanguageMenu';


function App({ t }) {

  return (
    <Router>
      <div className="App">
        <Suspense fallback={<div>Loading...</div>}>
          <AppBar position="static">
            <Box sx={{ flexGrow: 1 }}>
              <Toolbar>

                <Typography variant="h6" color="inherit" sx={{ flexGrow: 1 }} compoennt="div">
                  <Link to='/' style={{ textDecoration: 'none', color: 'inherit' }}>
                    {t("app.title")}
                  </Link>
                </Typography>


                <LanguageMenu />
              </Toolbar>
            </Box>

          </AppBar>
          <Routes>
            <Route exact path='/' element={<Home />} />
            <Route path='/predict' element={<Predict />} />
            <Route path='/recommend' element={<Recommend />} />
          </Routes>
        </Suspense>
      </div>
    </Router>
  );
}

export default withTranslation()(App);
