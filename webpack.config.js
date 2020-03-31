const path = require('path');

module.exports = {
  entry: './js/index.jsx',
  output: {
    path: path.join(__dirname, '/static/'),
    filename: 'bundle.js',
  },
  resolve: {
    extensions: ['.js', '.jsx'],
  },
};
