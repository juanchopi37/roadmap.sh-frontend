// sirve para obtener la referencia de un elemento html
// document.getElementById("ID")

const form = document.getElementById("formulario")

const inputEmail =  document.getElementById("email")
const inputPassword = document.getElementById("password")
const messageErrorEmail = document.getElementById("mensaje-error-email")

const messageErrorPassword = document.getElementById("mensaje-error-password")


//funcion callback para el vento submit
const onSubmit =(ev)=>{
    ev.preventDefault()

    let email = inputEmail.value
    let password = inputPassword.value

    if(email===""){
        messageErrorEmail.innerHTML= "<p>Debe ingresar el email</p>"
        return
    }else{
        messageErrorEmail.innerHTML=""
    }

    if(password===""){
        messageErrorPassword.innerHTML= "<p>Debe ingresar el password</p>"
        return
    }else{
        messageErrorPassword.innerHTML=""
    }
   
    if (email==="test@test.co" && password==="1234") {
        alert("El usuario es valido")
        inputEmail.value=""
        inputPassword.value=""
    } else{
        alert("El usuario no es valido")
    }
}

// agregar evento al elemento html
form.addEventListener("submit",onSubmit )