
const displayTime = document.querySelector(".display-time");
// Time
function showTime() {
    let time = new Date();
    displayTime.innerText = time.toLocaleTimeString("en-US", { hour12: false });
    setTimeout(showTime, 1000);
}

showTime();