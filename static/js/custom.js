var ldswitch = document.querySelector('#mode');
var loadingSpinner = document.getElementById('loader')

function setModePreference(mode) {
    document.cookie = "lightmode=" + mode + "; path=/";
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

setModePreference(getCookie('lightmode') != null ? getCookie('lightmode') : 'dark');


window.onload = () => {
    setTimeout(() => {
        loadingSpinner.classList.add('d-none')
    }, 230)
    let curLightMode = getCookie('lightmode');
    if (curLightMode == 'light') {
        document.querySelector('body').setAttribute('data-theme', 'light');
        ldswitch.checked = true;
    } else {
        document.querySelector('body').setAttribute('data-theme', 'dark');
        ldswitch.checked = false;
    }


};

ldswitch.addEventListener('click', function () {
    let curLightMode = getCookie('lightmode');
    if (curLightMode == 'light') {
        document.querySelector('body').setAttribute('data-theme', 'dark');
        setModePreference('dark');
    } else {
        document.querySelector('body').setAttribute('data-theme', 'light');
        setModePreference('light');
    }
});

