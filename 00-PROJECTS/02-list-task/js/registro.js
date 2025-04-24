const user = localStorage.getItem("user")

if (user!==null) {
    location.href = "http://127.0.0.1:5500/lista.html"
}


const form = document.getElementById("registro")
const inputFirstName = document.getElementById("firstName")
const inputLastName = document.getElementById("lastName")
const inputEmail = document.getElementById("email")
const inputPhone = document.getElementById("phone")
const inputPassword = document.getElementById("contrasena")
const ppalHTML = document.getElementById("ppal")

let listaUsuarios
const listJSON = localStorage.getItem("listaUsuarios")
if (listJSON !== null) {
    listaUsuarios = JSON.parse(listJSON)
} else {
    listaUsuarios = []
}

//funcion callback para el Evento submit
const onSubmit = (ev) => {
    ev.preventDefault()

    let email = inputEmail.value
    let firstName = inputFirstName.value
    let lastName = inputLastName.value
    let phone = inputPhone.value
    let password = inputPassword.value

    if (firstName === "") {
        inputFirstName.placeholder = "Debe ingresar el nombre"
        return
    }

    if (lastName === "") {
        inputLastName.placeholder = "Debe ingresar el apellido"
        return
    }

    if (phone === "") {
        inputPhone.placeholder = "Debe ingresar el teléfono"
        return
    }

    if (email === "") {
        inputEmail.placeholder = "Debe ingresar el Correo"
        return
    }

    if (password === "") {
        inputPassword.placeholder = "Debe ingresar la contraseña"
        return
    }

    if (listaUsuarios.some(usuario => usuario.email === email)) {
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Este correo ya existe",
          });
        return
    }

    inputEmail.value = ""
    inputFirstName.value = ""
    inputLastName.value = ""
    inputPhone.value = ""
    inputPassword.value = ""

    const newUser = {
        email,
        password,
        firstName,
        lastName,
        phone
    }
    listaUsuarios.push(newUser)
    const listJSON = JSON.stringify(listaUsuarios)
    localStorage.setItem("listaUsuarios", listJSON)

    // ppalHTML.innerHTML += `
    // <div class="alert alert-success" role="alert">
    //     Usuario registrado con exito!
    // </div>
    // `

    Swal.fire({
        title: "Usuario registrado exitosamente",
        icon: "success",
        draggable: true
    });

    setTimeout(() => {
        location.href = "http://127.0.0.1:5500/index.html"
    }, 2000)
}
//funcion callback para el Evento pulsar teclas y verificar si son letras o numeros
const pulsarLet = (e) => {
    if (["ArrowLeft", "ArrowRight"].includes(e.key)) {
        return;
    }
    if (/^[0-9]$/.test(e.key) && e.key !== "Backspace") {
        e.preventDefault();
    }
}

const pulsarNum = (e) => {
    if (["ArrowLeft", "ArrowRight"].includes(e.key)) {
        return;
    }

    if (!/^[0-9]$/.test(e.key) && e.key !== "Backspace") {
        e.preventDefault();
    }
}

form.addEventListener("submit", onSubmit)

inputFirstName.addEventListener("keydown", pulsarLet)
inputLastName.addEventListener("keydown", pulsarLet)
inputPhone.addEventListener("keydown", pulsarNum)


