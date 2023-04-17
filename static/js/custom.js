var ldswitch = document.querySelector('#mode');

function setModePreference(mode) {
    document.cookie = "lightmode=" + mode + "; path=/";
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }

setModePreference(getCookie('lightmode') != null ? getCookie('lightmode') : 'light' );

window.onload = () => {
    let curLightMode = getCookie('lightmode');
    if (curLightMode == 'light') {
        document.querySelector('body').setAttribute('data-theme', 'light');
        ldswitch.checked = true;
    } else {
        document.querySelector('body').setAttribute('data-theme', 'dark');
        ldswitch.checked = false;
    }
};

ldswitch.addEventListener('click', function() {
    let curLightMode = getCookie('lightmode');
    if (curLightMode == 'light') {
        document.querySelector('body').setAttribute('data-theme', 'dark');
        setModePreference('dark');
    } else {
        document.querySelector('body').setAttribute('data-theme', 'light');
        setModePreference('light');
    }
});

