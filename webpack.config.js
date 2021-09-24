const path = require('path');

const BaseConfig = {
    module: {
        rules: [
            {
                test: /\.tsx?$/,
                use: 'ts-loader',
                exclude: /node-modules/
            }
        ]
    }
};

const WebsiteConfig = Object.assign({}, BaseConfig, {
    entry: './website/assets/ts/index.ts',
    output: {
        path: path.resolve(__dirname, 'website/static/website/js'),
        filename: 'index.js'
    }
});

module.exports = [
    WebsiteConfig
];