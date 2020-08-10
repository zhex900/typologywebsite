const path = require('path');

module.exports = {
    entry: './site/index.js',
    output: {
        filename: 'main.js',
        path: path.resolve(__dirname, 'site'),
    },
    devServer: {
        contentBase: path.join(__dirname, 'site'),
        compress: true,
        port: 9000,
    },
};
