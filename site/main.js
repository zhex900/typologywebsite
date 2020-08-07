function buildQuiz(){
    const output = [];
    questions.forEach(
        (currentQuestion, questionNumber) => {
            const answers = [];
            for (letter in currentQuestion.answers){
                
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
        }
    );
    quizContainer.innerHTML = output.join('');
}

function get_colrow_chance(list, a, b, c) {
    let output = 0;  
    if (list[0] == a && list[1] == b) {
        output += 1;
        console.log("output at if 1: " + output);
    }
    if (list[1] == b && list[2] == c) {
        output += 1;
        console.log("output at if 2: " + output);
    }
    if (list[0] == a && list[2] == c) {
        output += 1;
        console.log("output at if 3: " + output);
    }
    console.log("output at end of function: " + output);
    return output;
}

function showResults(){
    const answerContainers = quizContainer.querySelectorAll('.answers');

    let dich_answer_list = [];
    let unsure_answer_list = [];

    questions.forEach( (currentQuestion, questionNumber)  => {
        const answerContainer = answerContainers[questionNumber];
        const selector = `input[name=question${questionNumber}]:checked`;
        const userAnswer = (answerContainer.querySelector(selector) || {}).value;

        // the first three are the columns, the last three are the rows
        var dich_q_numbers = [0,1,2,4,5,6];
        if (questionNumber in dich_q_numbers) {
            console.log("if question in list is working")
            if (userAnswer == 'a') {
                dich_answer_list.push(0);
            } else if (userAnswer == 'b') {
                dich_answer_list.push(1);
            } else {
                dich_answer_list.push(2);
            }
        } else {
            if (userAnswer == 'a') {
                unsure_answer_list.push(0);
            } else if (userAnswer == "b") {
                unsure_answer_list.push(1);
            } else if (userAnswer == "c") {
                unsure_answer_list.push(2);
            } else {
                unsure_answer_list.push(3);
            }
        }
        console.log(dich_answer_list);
    });
    let tally_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

    const cols = [[0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15]];
    const rows = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]];
    
    let list_col_dichs = dich_answer_list.slice(0, 3);
    let list_row_dichs = dich_answer_list.slice(3, 6);
    
    //todo: make the list of lists of dichotomies the same by inverting the 1s and zeros on list-row-dichs
    //and swapping around the last two lists on list_col_dichs so that they both are [[1, 0, 1], [1, 1, 0], [0, 1, 1], [0, 0, 0]]
    if (!(2 in list_col_dichs)) {    //THESE ARE NOT WORKING FIX ASAP   
        if (!(list_col_dichs in [[1, 0, 1], [1, 1, 0], [0, 0, 0], [0, 1, 1]]) && unsure_answer_list[0] !== 3) {
            list_row_dichs[unsure_answer_list[0]] = Math.abs(list_row_dichs[unsure_answer_list[0]] - 1);
        }
    }
    if (!(2 in list_row_dichs)) {
        if (!(list_row_dichs in [[0, 1, 0], [1, 1, 0], [1, 0, 0], [1, 1, 1]]) && unsure_answer_list[1] !== 3) {
            list_row_dichs[unsure_answer_list[1]] = Math.abs(list_row_dichs[unsure_answer_list[1]] - 1);
    
        }
    }
    
    console.log("list_col_dichs: " + list_col_dichs);
    console.log("list_row_dichs: " + list_row_dichs);

    let col_chances = [0, 0, 0, 0];
    let row_chances = [0, 0, 0, 0];
    //calculate the chance for a given row to be selected
    col_chances[0] = get_colrow_chance(list_col_dichs, 1, 0, 1);
    col_chances[1] = get_colrow_chance(list_col_dichs, 1, 1, 0);
    col_chances[2] = get_colrow_chance(list_col_dichs, 0, 0, 0);
    col_chances[3] = get_colrow_chance(list_col_dichs, 0, 1, 1);
    //calculate the chance for a given column to be selected
    //THIS IS NOT WORKING PROPERLY - FIX ASAP
    row_chances[0] = get_colrow_chance(list_row_dichs, 0, 1, 0);
    row_chances[1] = get_colrow_chance(list_row_dichs, 0, 0, 1);
    row_chances[2] = get_colrow_chance(list_row_dichs, 1, 0, 0);
    row_chances[3] = get_colrow_chance(list_row_dichs, 1, 1, 1);

    console.log("col_chances: " + col_chances);
    console.log("row_chances: " + row_chances);
    
    for (var i = 0; i < 4; i++) {
        cols[i].forEach(j => tally_list[j] += col_chances[i]);
        rows[i].forEach(j => tally_list[j] += row_chances[i]);
    }
    
    resultsContainer.innerHTML = `<table>
        <tr>
            <th>Results:</th>
            <th>Finisher</th>
            <th>Background</th>
            <th>In-charge</th>
            <th>Starter</th>
        </tr>
        <tr>
            <th>Intellectual</th>
            <td>INTJ: ${tally_list[0]}</td>
            <td>INTP: ${tally_list[1]}</td>
            <td>ENTJ: ${tally_list[2]}</td>
            <td>ENTP: ${tally_list[3]}</td>
        </tr>
        <tr>
            <th>Idealist</th>
            <td>INFJ: ${tally_list[4]}</td>
            <td>INFP: ${tally_list[5]}</td>
            <td>ENFJ: ${tally_list[6]}</td>
            <td>ENFP: ${tally_list[7]}</td>
        </tr>
        <tr>
            <th>Guardian</th>
            <td>ISTJ: ${tally_list[8]}</td>
            <td>ISFJ: ${tally_list[9]}</td>
            <td>ESTJ: ${tally_list[10]}</td>
            <td>ESFJ: ${tally_list[11]}</td>
        </tr>
        <tr>
            <th>Artisan</th>
            <td>ISTP: ${tally_list[12]}</td>
            <td>ISFP: ${tally_list[13]}</td>
            <td>ESTP: ${tally_list[14]}</td>
            <td>ESFP: ${tally_list[15]}</td>
        </tr>
    </table>`;
}

const quizContainer = document.getElementById('quiz')
const resultsContainer = document.getElementById('results')
const submitButton = document.getElementById('submit')
const questions = [
    {
        question: "Initiating or Responding?",
        answers: {
            a: "initiating",
            b: "responding"
        }
    },
    {
        question: "Direct or Informative?",
        answers: {
            a: "direct",
            b: "informative"
        }
    },
    {
        question: "Control or Movement?",
        answers: {
            a: "control",
            b: "movement"
        }
    },
    {
        question: "Out of these first three questions, which one were you the least confident answering?",
        answers: {
            a: "initiating/responding",
            b: "direct/informative",
            c: "control/movement",
        }
    },
    {
        question: "Abstract or Concrete?", //something is very wrong with these last three questions
        answers: {
            a: "abstract",
            b: "concrete"
        }
    },
    {
        question: "Affiliative or Pragmatic?",
        answers: {
            a: "affiliative",
            b: "pragmatic"
        }
    },
    {
        question: "Systematic or Interest?",
        answers: {
            a: "systematic",
            b: "interest"
        }
    },
    {
        question: "Out of the last three questions, which one were you the least confident answering?",
        answers: {
            a: "abstract/concrete",
            b: "direct/informative",
            c: "control/movement"
        }
    }
];

buildQuiz();
quizContainer.addEventListener('click', showResults);