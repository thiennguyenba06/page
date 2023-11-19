let workTittle = document.getElementById('work');
let breakTittle = document.getElementById('break');


let workTime = 25;
let breakTime = 5;

let seconds = "00"


// display
window.onload = () => {
    document.getElementById('minutes').innerHTML = workTime;
    document.getElementById('seconds').innerHTML = seconds;
    workTittle.classList.add('active');
}


// start function
function start() {
    // change button
    document.getElementById('start').style.display = "none";
    document.getElementById('reset').style.display = "block";

    // change time
    seconds = 59;
    let workMinutes = workTime - 1;
    let breakMinutes = breakTime - 1;

    breakCount = 0;

    let timerFunction = () => {
        console.log(workMinutes, seconds)
        // change display
        seconds = seconds - 1;
        document.getElementById('minutes').innerHTML = workMinutes;
        document.getElementById('seconds').innerHTML = seconds;

        if (seconds === 0) {
            seconds = 59;
            workMinutes = workMinutes - 1;
            if (workMinutes === -1) {
                if (breakCount % 2 === 0) {
                    workMinutes = breakMinutes;
                    breakCount++

                    // change panel
                    workTittle.classList.remove('active');
                    breakTittle.classList.add('active');
                } else {
                    // continue work
                    workMinutes = workTime;
                    breakCount++

                    // change the painel
                    breakTittle.classList.remove('active');
                    workTittle.classList.add('active');
                }
            }
        }
    }
    // start countdown
    setInterval(timerFunction, 1000); // 1000 = 1s
}

