document.addEventListener("DOMContentLoaded", function(){
    let accuracy = sessionStorage.getItem("accuracy");
    let timer = sessionStorage.getItem("timer");
    let hours = 0
    let minutes = 0
    let seconds = 0
    const WPM = Math.round((((100*accuracy)/timer)* 60));
    hours = timer % 3600;
    hours = timer - hours;
    timer = timer - hours;
    hours = hours / 3600;
    hours = String(hours).padStart(2, '0')
    minutes = timer % 60;
    minutes = timer - minutes;
    timer = timer - minutes;
    minutes = minutes / 60;
    minutes = String(minutes).padStart(2, '0')
    seconds = String(timer).padStart(2, '0')
    accuracy = accuracy * 100;
    accuracy = accuracy.toFixed(2);
    document.getElementById("WPM").innerText=WPM;
    document.getElementById("accuracy").innerText = accuracy + "%";
    document.getElementById("timeTaken").innerText = hours + ':' +  minutes + ':' + seconds;
    document.getElementById("WPMsub").value = WPM;
    document.getElementById("timesub").value = hours + ':' +  minutes + ':' + seconds
    document.getElementById("accuracysub").value = accuracy;
})