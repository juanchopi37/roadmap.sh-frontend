
// Obtenemos los inputs del archivo HTML

const alertPlaceholder = document.getElementById('boton-signin');
const nombre = document.getElementById("primerNombre");
const apellido = document.getElementById("apellido");
const email = document.getElementById("inputEmail4");
const contrasena = document.getElementById("inputPassword4");
const direccion = document.getElementById("inputAddress");
const ciudad = document.getElementById("inputCity");
const region = document.getElementById("inputState");
const codigoZip = document.getElementById("inputZip");
const prueba = document.getElementById("prueba");

// Función para mostrar un error al no poner todos los datos 

const appendAlert = (message, type) => {
    const wrapper = document.createElement('div');
    wrapper.innerHTML = [
        `<div class="alert alert-${type} alert-dismissible" role="alert">`,
        `   <div>${message}</div>`,
        '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
        '</div>'
    ].join('');
    alertPlaceholder.append(wrapper);
};



const onSubmit = (e) => {
    e.preventDefault();
    
    const form = e.target;
    const inputs = form.querySelectorAll('input');
    let allFilled = true;

    inputs.forEach(input => {
        if (input.value.trim() === '') {
            allFilled = false;
        }
    });

    if (!allFilled) {
        appendAlert('Por favor ingrese todos los datos', 'danger');
    } else {
        appendAlert('Todos los campos están llenos', 'success');
        registroUser();
    }
};

const alertTrigger = document.getElementById('formulario');
if (alertTrigger) {
    alertTrigger.addEventListener('submit', onSubmit);
}

const registroUser = () => {
    const data = {
        nombre: nombre.value,
        apellido: apellido.value,
        email: email.value,
        contrasena: contrasena.value,
        direccion: direccion.value,
        ciudad: ciudad.value,
        region: region.value,
        codigoZip: codigoZip.value
    };
    console.log(data);
    const dataString = JSON.stringify(data);
};

if (dataString = ""){
    
}
