/* jshint esversion: 11 */

// this function removes the alert after 5 seconds
setTimeout(function () {
    let messages = document.getElementById("alert-message");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 7000);

// cookies consent

const cookieStorage = {
    getItem: (key) => {
        const cookies = document.cookie
        .split(';')
        .map(cookie => cookie.split('='))
    .reduce((acc, [key, value]) => ({ ...acc, [key.trim()]: value }),{});
    return cookies[key];
    },
    setItem: (key, value) => {
        const now = new Date();
        let expiryDate = new Date(now);
        expiryDate.setDate(now.getDate() + 365);
        document.cookie = `${key}=${value}; expires=${expiryDate}; SameSite=Lax; secure`;

    },
};

const storageType = cookieStorage;
const consentPropertyName = 'byinoati_consent';
const shouldShowPopup = () => !storageType.getItem(consentPropertyName);
const saveToStorage = () => storageType.setItem(consentPropertyName, true);

window.onload = () => {
    const consentPopup = document.getElementById('consent-popup');
    const acceptBtn = document.getElementById('accept-cookies-btn');

    const acceptFn = event => {
        saveToStorage(storageType)
        consentPopup.style.visibility = 'hidden';
    }

    acceptBtn.addEventListener('click', acceptFn);

    if (shouldShowPopup(storageType)){
        setTimeout(() => {
            consentPopup.style.visibility = 'visible';
        }, 500);
    }
};