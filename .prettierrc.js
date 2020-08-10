module.exports = {
    trailingComma: 'es6',
    tabWidth: 4,
    singleQuote: true,
    printWidth: 100,
    bracketSpacing: false,
    overrides: [
        {
            files: '*.json',
            options: {
                tabWidth: 2,
            },
        },
    ],
};
