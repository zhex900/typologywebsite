const {findInArray} = require('./util');

test('findInArray should find element in array', () => {
    expect(findInArray(1, [1, 2])).toBe(true);
});
