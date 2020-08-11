export const getColrowChance = (list, a, b, c) => {
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
};
// replace with native find
export const findInArray = (value, array) => {
    let output = false;
    for (var i = 0; i < array.length; i++) {
        const item = array[i];
        if (item === value) {
            output = true;
            break;
        }
    }
    return output;
};
export const getTypeFromArray = (array) => {
    const types = ["INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP", "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP"];
    let largest_index = 0;
    let largest_value = 0;
    let only_one_largest = true
    for (var i = 0; i < array.length; i++) {
        if (largest_value === array[i]) {
            only_one_largest = false;
        } else if (array[i] > largest_value) {
            only_one_largest = true;
            largest_value = array[i];
            largest_index = i;
        }
    }
    if (only_one_largest === false) {
        return "";
    } else {
        return "You are (probably) an " + types[largest_index];
    }
};