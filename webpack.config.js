const path = require('path');

module.exports = {
  entry: './js/index.jsx',
  output: {
    path: path.join(__dirname, '/static/'),
    filename: 'bundle.js',
  },
  module: {
    rules: [
    {
      test: /\.jsx?$/,
      use: {
        loader: 'babel-loader',
        options: {
          presets: ['@babel/preset-env', '@babel/react']
        }
      }
    }
  ]
  },
  resolve: {
    extensions: ['.js', '.jsx'],
  },
};
