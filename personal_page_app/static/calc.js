// Get the input field and result div by their ID
const inputField = document.getElementById('calc-input');
const resultDiv = document.querySelector('.user-result');

// Add an event listener to the input field that triggers whenever the input value changes
inputField.addEventListener('input', () => {
    try {
        var result = inputField.value;
        if (result.includes('x') == true) {
            result = result.replaceAll('x', '*');
        } else {
            
        }
        resultDiv.textContent = eval(result);
    } catch(err) { 

    } 
});