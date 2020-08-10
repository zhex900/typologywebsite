export function get_colrow_chance(list, a, b, c) {
    let output = 0;
    if (list[0] == a && list[1] == b) {
        output += 1;
    }
    if (list[1] == b && list[2] == c) {
        output += 1;
    }
    if (list[0] == a && list[2] == c) {
        output += 1;
    }
    return output;
}

export function findInArray(value, array) {
    let output = false;
    for (var i = 0; i < array.length; i++){
        const item = array[i]
        if (item === value) {
            output = true;
            break;
        }
    }
    return output;
}