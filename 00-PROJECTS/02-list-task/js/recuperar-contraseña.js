const recuperarPassword = document.getElementById("btnRecuperar");
const containerRecovery = document.getElementById("containerRecovery");

// Evento para mostrar el formulario de recuperación de contraseña
recuperarPassword.addEventListener("click", () => {
    containerRecovery.innerHTML = `
    <div class="d-flex flex-column justify-content-between align-items-center gap-1">
        <h6 class="text-center mt-3">Recuperar contraseña</h6>
        <input type="text" class="form-control mx-3" placeholder="Correo electrónico registrado" id="emailRecovery">
        <button class="btn btn-secondary mt-3" id="buscarPassword">Buscar</button>
        <div class="containerPassword"></div>
    </div>
    `;

    // 🔹 Se selecciona el botón creado dinámicamente y se le asigna el evento
    document.getElementById("buscarPassword").addEventListener("click", buscarPassword);
});

// Función para encontrar la contraseña
function buscarPassword() {
    const emailRecovery = document.getElementById("emailRecovery").value.trim();
    const listaUsuarios = JSON.parse(localStorage.getItem("listaUsuarios")) || [];

    // Buscar usuario por correo
    const usuarioEncontrado = listaUsuarios.find(user => user.email === emailRecovery);

    // Seleccionar el contenedor creado dinámicamente
    const containerPassword = document.querySelector(".containerPassword");

    if (usuarioEncontrado) {
        containerPassword.innerHTML = `
        <div class="d-flex flex-column mt-2">
            <h6 class="text-center mt-3">Contraseña recuperada</h6>
            <p class="text-center mb-1" id="copiarPassword">${usuarioEncontrado.password}</p>
            <button class="btn btn-outline-secondary mt-1" type="button" id="botonCopiar">Copiar</button>
        </div>
        `;

        // Agregar evento para copiar la contraseña
        document.getElementById("botonCopiar").addEventListener("click", copiarPassword);
    } else {
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Correo no encontrado",
        });
    }
}

// Función para copiar la contraseña al portapapeles
function copiarPassword() {
    const passwordTexto = document.getElementById("copiarPassword").innerText;
    navigator.clipboard.writeText(passwordTexto).then(() => {
        Swal.fire({
            icon: "success",
            title: "¡Éxito!",
            text: "Contraseña copiada al portapapeles",
        });
    });
    setTimeout(() => {
        document.getElementById("containerRecovery").innerHTML = ""
    }, 1000)
}
