import React from 'react';
import ReactDOM from 'react-dom';
import Speech from './speech';

// This method is only called once
ReactDOM.render(
  // Insert the component into the DOM
  <Speech url="/speech/" />,
  document.getElementById('reactEntry'),
);
