import {getColrowChance, findInArray, getTypeFromArray} from './util.js';
import questions from '../data/questions.json';

console.log(questions);
const quizContainer = document.getElementById('quiz');

function buildQuiz() {
    const output = [];
    questions.forEach((currentQuestion, questionNumber) => {
        const answers = [];
        for (const letter in currentQuestion.answers) {
            //add html button for each option
            answers.push(
                `<label>
                        <input type = "radio" name = "question${questionNumber}" value="${letter}">
                        ${currentQuestion.answers[letter]}                  
                    </label>`
            );
        }
        output.push(
            `<h3><div class="question"> ${currentQuestion.question} </div></h3>
                <div class="answers"> ${answers.join('')} </div>`
        );
    });
    quizContainer.innerHTML = output.join('');
}

function showResults() {
    const answerContainers = quizContainer.querySelectorAll('.answers');

    let list_unsure_answers = [];
    let list_dich_answers = [];

    questions.forEach((currentQuestion, questionNumber) => {
        const answerContainer = answerContainers[questionNumber];
        const selector = `input[name=question${questionNumber}]:checked`;
        const userAnswer = (answerContainer.querySelector(selector) || {}).value;

        // the first three are the columns, the last three are the rows
        var dich_q_numbers = [0, 1, 2, 4, 5, 6];
        if (findInArray(questionNumber, dich_q_numbers)) {
            if (userAnswer == 'a') {
                list_dich_answers.push(0);
            } else if (userAnswer == 'b') {
                list_dich_answers.push(1);
            } else {
                list_dich_answers.push(2);
            }
        } else {
            if (userAnswer == 'a') {
                list_unsure_answers.push(0);
            } else if (userAnswer == 'b') {
                list_unsure_answers.push(1);
            } else if (userAnswer == 'c') {
                list_unsure_answers.push(2);
            } else {
                list_unsure_answers.push(3);
            }
        }
    });
    let tally_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

    let list_col_dichs = list_dich_answers.slice(0, 3);
    let list_row_dichs = list_dich_answers.slice(3, 6);

    const cols = [
        [0, 4, 8, 12],
        [1, 5, 9, 13],
        [2, 6, 10, 14],
        [3, 7, 11, 15],
    ];
    const rows = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, 10, 11],
        [12, 13, 14, 15],
    ];

    /*i could have make the list of lists of dichotomies the same by inverting the 1s and zeros on list-row-dichs
    and swapping around the last two lists on list_col_dichs so that they both are ["101", "110", "011", "000"]
    however, i didn't because i wanted to preserve the 16personalities type-grid layout*/

    if (!findInArray(2, list_col_dichs)) {
        if (
            !findInArray(list_col_dichs.join(''), ['101', '110', '000', '011']) &&
            list_unsure_answers[0] !== 3
        ) {
            list_col_dichs[list_unsure_answers[0]] = Math.abs(
                list_col_dichs[list_unsure_answers[0]] - 1
            );
        }
    }
    if (!findInArray(2, list_row_dichs)) {
        if (
            !findInArray(list_row_dichs.join(''), ['010', '110', '100', '111']) &&
            list_unsure_answers[1] !== 3
        ) {
            list_row_dichs[list_unsure_answers[1]] = Math.abs(
                list_row_dichs[list_unsure_answers[1]] - 1
            );
        }
    }

    let col_chances = [0, 0, 0, 0];
    let row_chances = [0, 0, 0, 0];
    //calculate the chance for a given row to be selected
    col_chances[0] = getColrowChance(list_col_dichs, 1, 0, 1);
    col_chances[1] = getColrowChance(list_col_dichs, 1, 1, 0);
    col_chances[2] = getColrowChance(list_col_dichs, 0, 0, 0);
    col_chances[3] = getColrowChance(list_col_dichs, 0, 1, 1);
    //calculate the chance for a given column to be selected
    row_chances[0] = getColrowChance(list_row_dichs, 0, 1, 0);
    row_chances[1] = getColrowChance(list_row_dichs, 0, 0, 1);
    row_chances[2] = getColrowChance(list_row_dichs, 1, 0, 0);
    row_chances[3] = getColrowChance(list_row_dichs, 1, 1, 1);
    
    for (var i = 0; i < 4; i++) {
        cols[i].forEach((j) => (tally_list[j] += col_chances[i]));
        rows[i].forEach((j) => (tally_list[j] += row_chances[i]));
    }

    // these are the dichotomies that will be displayed in the table.
    const final_dichs = [];
    for (let i = 0; i < 3; i++) {
        if (list_col_dichs[i] === 2) {
            final_dichs.push('<span style="color:red">0</span>', '<span style="color:red">0</span>');
        } else if (list_col_dichs[i] === 0) {
            final_dichs.push(`<span style="color:limegreen">1</span>`, `<span style="color:red">0</span>`);
        } else {
            final_dichs.push(`<span style="color:red">0</span>`, `<span style="color:limegreen">1</span>`);
        }
    }
    for (let i = 0; i < 3; i++) {
        if (list_row_dichs[i] === 2) {
            final_dichs.push('<span style="color:red">0</span>', '<span style="color:red">0</span>');
        } else if (list_row_dichs[i] === 0) {
            final_dichs.push(`<span style="color:limegreen">1</span>`, `<span style="color:red">0</span>`);
        } else {
            final_dichs.push(`<span style="color:red">0</span>`, `<span style="color:limegreen">1</span>`);
        }
    }
    const result = getTypeFromArray(tally_list)
    /*
    0: initiating 1:responding
    2: direct 3: informative
    4: control 5: movement
    6: abstract 7: concrete
    8: affiliative 9: pragmatic
    10: systematic 11: interest
    */
    resultsContainer.innerHTML = `<h2>Results:</h2>
    <p>(this is just a demonstration of how it works, and wouldn't be shown in the final version)</p>
    <table>
        <tr>
            <th>
                Interaction styles >
                Temperaments V
            </th>
            <th>
                Finisher
                Responding:${final_dichs[1]}
                Directive:${final_dichs[2]}
                Progression:${final_dichs[5]}
            </th>
            <th>
                Background
                Responding:${final_dichs[1]}
                Informative:${final_dichs[3]}
                Outcome:${final_dichs[4]}
            </th>
            <th>
                In-charge
                Initiating:${final_dichs[0]}
                Direct:${final_dichs[2]}
                Outcome:${final_dichs[4]}
            </th>
            <th>
                Starter
                Initiating:${final_dichs[0]}
                Informative:${final_dichs[3]}
                Progression:${final_dichs[5]}
            </th>
        </tr>
        <tr>
            <th>
                Intellectual
                Abstract:${final_dichs[6]}
                Pragmatic:${final_dichs[9]}
                Systematic:${final_dichs[10]}
            </th>
            <td>INTJ:${tally_list[0]}</td>
            <td>INTP:${tally_list[1]}</td>
            <td>ENTJ:${tally_list[2]}</td>
            <td>ENTP:${tally_list[3]}</td>
        </tr>
        <tr>
            <th>
                Idealist
                Abstract:${final_dichs[6]}
                Affiliative:${final_dichs[8]}
                Interest:${final_dichs[11]}
            </th>
            <td>INFJ:${tally_list[4]}</td>
            <td>INFP:${tally_list[5]}</td>
            <td>ENFJ:${tally_list[6]}</td>
            <td>ENFP:${tally_list[7]}</td>
        </tr>
        <tr>
            <th>
                Guardian
                Concrete:${final_dichs[7]}
                Affiliative:${final_dichs[8]}
                Systematic:${final_dichs[10]}
            </th>
            <td>ISTJ:${tally_list[8]}</td>
            <td>ISFJ:${tally_list[9]}</td>
            <td>ESTJ:${tally_list[10]}</td>
            <td>ESFJ:${tally_list[11]}</td>
        </tr>
        <tr>
            <th>
                Artisan
                Concrete:${final_dichs[7]}
                Pragmatic:${final_dichs[9]}
                Interest:${final_dichs[11]}
            </th>
            <td>ISTP:${tally_list[12]}</td>
            <td>ISFP:${tally_list[13]}</td>
            <td>ESTP:${tally_list[14]}</td>
            <td>ESFP:${tally_list[15]}</td>
        </tr>
    </table>
    <h1>${result}</h1>`;
}


const resultsContainer = document.getElementById('results');
const submitButton = document.getElementById('submit');

buildQuiz();
quizContainer.addEventListener('click', showResults);