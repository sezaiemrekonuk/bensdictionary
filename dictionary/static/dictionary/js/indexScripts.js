var copyButtons = document.querySelectorAll("#specialChars");
var lightModeButton = document.getElementById("mode");
const logoImage = document.getElementById("logo-index");

const copyText = e => {
  var buttonText = e.target.getAttribute("data-text");
  document.getElementById("search-input").value += buttonText;
}
for (var i = 0; i < copyButtons.length; i++) {
  copyButtons[i].addEventListener("click", copyText);
}

const getLigthMode = () => {
    return document.cookie.split(';').find(row => row.trim().startsWith('lightmode='));
}

const setImageMode = () => {
    let lightMode = getLigthMode();
    if (lightMode) {
        lightMode = lightMode.split('=')[1];
        if (lightMode == 'light') {
            logoImage.src = "static/img/light-logo.png"
        } else {
            logoImage.src = "static/img/dark-logo.png"
        }
    }
}

setImageMode();

lightModeButton.addEventListener('click', setImageMode);
