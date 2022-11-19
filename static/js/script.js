/* jshint esversion: 11 */

// this function removes the alert after 5 seconds
setTimeout(function () {
    let messages = document.getElementById("alert-message");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 7000);

// cookies consent

const cookieStorage = {
    getItem: (item) => {
        const cookies = document.cookie
        .split(';')
        .map(cookie => cookie.split('='))
        .reduce((acc, [key, value]) => ({ ...acc, [key.trim()]: value }),{});
    return cookies[item];
    },
    setItem: (item, value) => {
        const now = new Date();
        let expiryDate = new Date(now);
        expiryDate.setDate(now.getDate() + 365);
        document.cookie = `${item}=${value}; expires=${expiryDate}; SameSite=Lax; secure`;
    },
};

const storageType = cookieStorage;
const consentPropertyName = 'byinoati_consent';

const shouldShowPopup = () => !storageType.getItem(consentPropertyName);
const saveToStorage = () => storageType.setItem(consentPropertyName, true);

window.onload = () => {

    const acceptFn = event => {
        saveToStorage(storageType);
        consentPopup.style.visibility = 'hidden';
    }

    const consentPopup = document.getElementById('consent-popup');
    const acceptBtn = document.getElementById('accept-cookies-btn');
    acceptBtn.addEventListener('click', acceptFn);

    if (shouldShowPopup(storageType)) {
        setTimeout(() => {
            consentPopup.style.visibility = 'visible';
        }, 500);
    }
};