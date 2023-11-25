const wtf_phone_field = document.getElementById('phone');
wtf_phone_field.style.cssText = 'display: none;';
wtf_phone_field.parentElement.insertAdjacentHTML('beforeend', '<div><input required type="tel" id="_phone"></div>');
const fancy_phone_field = document.getElementById('_phone');
const fancy_phone_iti = window.intlTelInput(fancy_phone_field, {
    separateDialCode: true,
    utilsScript: "https://cdn.jsdelivr.net/npm/intl-tel-input@18.2.1/build/js/utils.js",
    initialCountry: "auto",
    geoIpLookup: function (callback) {
        fetch("https://ipapi.co/json")
            .then(function (res) {
                return res.json();
            })
            .then(function (data) {
                callback(data.country_code);
            })
            .catch(function () {
                callback("jo");
            });
    }
});
fancy_phone_iti.setNumber(wtf_phone_field.value);
fancy_phone_field.addEventListener('blur', function () {
    wtf_phone_field.value = fancy_phone_iti.getNumber();
});
const error = fancy_phone_iti.getValidationError();
