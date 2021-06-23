// webpack.config.js
const webpack = require('webpack');
const path = require('path');
const glob = require('glob');

const fileNames = glob.sync('./portfolio/js/**.js').reduce(function (obj, el) { obj[path.parse(el).name] = el; return obj }, {});

module.exports = {
    mode: 'production',
    entry: fileNames,
    output: {
        path: path.join(__dirname, '/portfolio/static/js/'),
        filename: 'bundle.js',
    },
    module: {
        rules: [
            {
                // Test for js or jsx files
                test: /\.jsx?$/,
                // Exclude external modules from loader tests
                exclude: /node_modules/,
                loader: 'babel-loader',
                options: {
                    presets: ['@babel/preset-env', '@babel/preset-react'],
                },
            },
        ],
    },
    resolve: {
        extensions: ['.js'],
    },
};