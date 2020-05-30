/**
 * This function takes the url and the contact form and return
 * a promise from the service that send the mail
 * @param {string} url 
 * @param {object} contactForm
 */
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

    let response = await fetch(url, {
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
        /**
         * function firing when submitting the contact form, and from that
         * calling the api.
         */
        contactForm.addEventListener('submit', (event) => {

            event.preventDefault();
            let sendUrl = "https://api.emailjs.com/api/v1.0/email/send";
            callApi(sendUrl, contactForm).then(function (response) {
                if (response.status == 200) {
                    $("#contactToast .toast-body").text('mail successfully sent');
                    $('#contactToast').toast('show');
                    $('input').val('');
                    $('textarea').val('');
                } else {
                    throw new err
                }
            }).catch(function (err) {
                $('#contactToast .toast-header').addClass("bg-danger");
                $("#contactToast .toast-body").text('error sending the mail');
                $('#contactToast').toast('show');

            });
        });

    }
})