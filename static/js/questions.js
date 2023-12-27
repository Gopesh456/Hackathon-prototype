// let editor = document.querySelector("#editor");
let codeEditor = ace.edit("editor");

const submitBtn = document.querySelector('.submit-btn')
const question = document.querySelector('p')
const textArea = document.querySelector('#textarea')
const runBtn = document.querySelector('.run-btn')

let editorLib = {
    init() {
        // Configure Ace

        // Theme
        codeEditor.setTheme("ace/theme/nord_dark");

        // Set language
        codeEditor.session.setMode("ace/mode/python");

        // Set Options
        codeEditor.setOptions({
            enableBasicAutocompletion: true,
            enableLiveAutocompletion: true,
        });

        // Set Default Code
        codeEditor.setValue("#Code here");
    }
}

editorLib.init()


// runBtn.addEventListener('click',()=>{
    // const userCode = codeEditor.getValue();
//     console.log(userCode)
//     textArea.textContent = userCode
// })


