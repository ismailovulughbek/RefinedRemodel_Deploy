document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector(".homePageForm");
    const responseMsg = document.querySelector(".showMessage2");
    let lang = localStorage.getItem("selectedLanguage") || "en";


    console.log(lang);
    

    form.addEventListener("submit", function (e) {
        e.preventDefault();
    
        const data = {
            name: form.name.value.trim(),
            phone: form.phone.value.trim(),
            email: form.email.value.trim(),
            service: form.service.value.trim(),
            message: form.message.value.trim()
        };
    


        if (!data.name || !data.email || !data.phone || !data.service || !data.message) {
            message = {'en':'Please fill in all fields!', 'es': '¡Por favor, rellena todos los campos!'}
            showMessage(lang, message, 0)
            return;
        }
    

        fetch("/service_message", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        })
        .then(res => res.json())
        .then(data => {
            showMessage(lang, data.message, 1)
            if (data.status === "success") form.reset();
        })
        .catch(err => {
            showMessage(lang, 'Something went wrong. Please try again later!', 0)
            console.error(err);
        });
    });

    function showMessage(lang, message, status) {
        responseMsg.style.opacity = "1";
        responseMsg.style.height = "auto";

        if (status){

            if(lang == 'en'){
                responseMsg.innerHTML = message.en
            }else{
                responseMsg.innerHTML = message.es
            }

            responseMsg.style.backgroundColor = "green";

        }else{

            if(lang == 'en'){
                responseMsg.innerHTML = message.en
            }else{
                responseMsg.innerHTML = message.es
            }

            responseMsg.style.backgroundColor = "red";

        }



        setTimeout(() => {
            responseMsg.style.opacity = "0";
            responseMsg.style.height = "0";
            responseMsg.style.overflow = "hidden"
        }, 3000);
    }
});