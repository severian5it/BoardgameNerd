async function callApi(url, contactForm) {
    
    let sendType = "POST";

    let data = {
        service_id: "gmail",
        template_id: "cocktail",
        user_id: "user_6QWtZ07QnotlGgzAFHDng",
        template_params: {
            "from_name": contactForm.contactName.value,
            "from_email": contactForm.contactEmail.value,
            "subject": contactForm.contactSubject.value,
            "message": contactForm.contactMessage.value,
        }
    };
    const postData = JSON.stringify(data);

    let response = await  fetch(url, {
            method: sendType,
            headers: {
            'Content-Type': 'application/json',
            },
            body: postData
        });
    return await response;
}

$(document).ready(function () {

    if (document.querySelector('#contact-form')) {

        const contactForm = document.querySelector('#contact-form');

        contactForm.addEventListener('submit', (event) => {

            event.preventDefault();
            let sendUrl = "https://api.emailjs.com/api/v1.0/email/send";
            callApi(sendUrl, contactForm).then(function (response) {
                console.log(response)
            }).catch(function (err) {
                console.log('Oops... ' + err);

            });


        });

    }
})