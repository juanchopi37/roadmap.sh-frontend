// sirve para obtener la referencia de un elemento html
// document.getElementById("ID")

const user = localStorage.getItem("user")

if (user!==null) {
    location.href = "http://127.0.0.1:5500/lista.html"
}

const form = document.getElementById("formulario")
const inputEmail =  document.getElementById("email")
const inputPassword = document.getElementById("password")


//funcion callback para el Evento submit
const onSubmit =(ev)=>{
    ev.preventDefault()

    let email = inputEmail.value
    let password = inputPassword.value

    if(email===""){
        inputEmail.placeholder="Debe ingresar el correo"
        return
    }
    if(password===""){
        inputPassword.placeholder="Debe ingresar la contraseña"
        return
    }

    const listUser = JSON.parse(localStorage.getItem("listaUsuarios")||"[]")

   
    const user = listUser.find(item => item.email=== email)

    if (!user) {
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Usuario no registrado",
          });
        return
    }

    if (password===user.password) {
        const useJSON = JSON.stringify(user)
        localStorage.setItem("user",useJSON)
        location.href="http://127.0.0.1:5500/lista.html"
    } else{
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "La contraseña es incorrecta",
          });
    }
}

// agregar evento al elemento html
form.addEventListener("submit",onSubmit )