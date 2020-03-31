import React from 'react';
import ReactDOM from 'react-dom';
import Speech from './speech';

// This method is only called once
ReactDOM.render(
  // Insert the likes component into the DOM
  <Feed url="/api/v1/p/" />,
  document.getElementById('reactEntry'),
);
