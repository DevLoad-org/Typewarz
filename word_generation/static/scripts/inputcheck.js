//will hold input keystrokes
let x = "";
let checker = false;
let timer = 0;

//will hold correct and total keystrokes respectively
let correct = 0;
let total = 0;

//TO CONVERT CHAR INTO SPANS
document.addEventListener('DOMContentLoaded', function() {
    const displayText = document.getElementById('displayText').innerText;
    const displayTextElement = document.getElementById("displayText");
    document.getElementById('displayText').innerHTML = "";
    displayText.split('').forEach(character => {
        const cSpan = document.createElement('span');
        cSpan.innerText = character;
        displayTextElement.appendChild(cSpan);
    })
})

// TO TRACK THE INPUT AND CHECK FOR CORRECTNESS
document.addEventListener("keydown", function(event) {
    if (checker === false)
    {
        startTimer();
        checker = true;
    }
    const displayTextElement = document.getElementById("displayText");
    const displaySpans = displayTextElement.querySelectorAll('span');
    if (x.length === displaySpans.length)
    {
        let accuracy = (correct/total);
        sessionStorage.setItem("accuracy",accuracy);
        sessionStorage.setItem("timer",timer);
        window.location.replace("results");

    }
    let flag = false;
    if (event.which >= 65 && event.which <= 90 || event.which <= 122 && event.which >= 97 || event.which === 32)
    {
        x += `${event.key}`;
        flag = true;
    }   
    else if (event.which === 8)
    {
        x = x.slice(0,-1);
        flag = true;
    }
    if(flag === true)
    {
        total = total + 1;
        const displayTextElement = document.getElementById("displayText");
        const displaySpans = displayTextElement.querySelectorAll('span');
        displaySpans.forEach((characterSpan, index) => {
            const character = x[index]
            if (character == null)
            {
                characterSpan.classList.remove('correct'); 
                characterSpan.classList.remove('incorrect');
            }
            else if (character=== characterSpan.innerText)
            {
                characterSpan.classList.add('correct'); 
                characterSpan.classList.remove('incorrect');
                if (index == x.length-1)
                {
                    correct += 1;
                }
            }
            else
            {
                characterSpan.classList.add('incorrect'); 
                characterSpan.classList.remove('correct');
            }
    })

    }
});

//TIMER
var hr = 0;
var min = 0;
var sec = 0;
var stoptime = true;

function startTimer() {
  if (stoptime == true) {
        stoptime = false;
        timerCycle();
    }
}
function stopTimer() {
  if (stoptime == false) {
    stoptime = true;
  }
}

function timerCycle() {
    if (stoptime == false) {
    sec = parseInt(sec);
    min = parseInt(min);
    hr = parseInt(hr);

    sec = sec + 1;

    if (sec == 60) {
      min = min + 1;
      sec = 0;
    }
    if (min == 60) {
      hr = hr + 1;
      min = 0;
      sec = 0;
    }

    if (sec < 10 || sec == 0) {
      sec = '0' + sec;
    }
    if (min < 10 || min == 0) {
      min = '0' + min;
    }
    if (hr < 10 || hr == 0) {
      hr = '0' + hr;
    }

    timer= (hr * 3600) + (60 *  min) + sec;
    document.getElementById("timerDisplay").innerText = hr + ':' +  min + ':' + sec;

    setTimeout("timerCycle()", 1000);
  }
}
