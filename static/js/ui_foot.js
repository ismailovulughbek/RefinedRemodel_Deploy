document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector(".homePageForm");
    const responseMsg = document.querySelector(".showMessage2");


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
            showMessage(message, 0)
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
            showMessage(data.message, 1)
            if (data.status === "success") form.reset();
        })
        .catch(err => {
            showMessage('Something went wrong. Please try again later!', 0)
            console.error(err);
        });
    });

    function showMessage(message, status) {

        let lang = localStorage.getItem("selectedLanguage") || "en";

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