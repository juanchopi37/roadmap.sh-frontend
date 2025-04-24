const userJSON = localStorage.getItem("user")

if (!userJSON) {
    location.href = "http://127.0.0.1:5500/index.html"
}

const salir = () => {
    localStorage.removeItem("user")
    location.href = "http://127.0.0.1:5500/index.html"
}

const lista = JSON.parse(localStorage.getItem("listaTareas")) || []

const inputTitulo = document.getElementById("titulo")
const inputDescripcion = document.getElementById("decription")
const tbody = document.getElementById("cuerpo")
const btnRegistro = document.getElementById("btnRegistro")

let editarIndex = null

// Función para registrar

const onRegister = () => {
    const titulo = inputTitulo.value.trim()
    const descripcion = inputDescripcion.value.trim()
    if (!titulo || !descripcion) return

    const user = JSON.parse(userJSON)
    const autor = `${user.firstName} ${user.lastName}`

    const data = { titulo, descripcion, autor }

    if (editarIndex === null) {
        lista.push(data)
    } else {
        lista[editarIndex] = data
        editarIndex = null
        btnRegistro.textContent = "Registro"

        Swal.fire({
            title: "Tarea actualizada",
            text: "La tarea ha sido editada con éxito",
            icon: "success",
            showClass: {
                popup: "animate__animated animate__fadeInUp animate__faster"
            },
            hideClass: {
                popup: "animate__animated animate__fadeOutDown animate__faster"
            }
        });
    }
    
    localStorage.setItem("listaTareas", JSON.stringify(lista))
    inputTitulo.value = ""
    inputDescripcion.value = ""
    cargaData()
}

// Función para cargar los datos de la lista en localStorage

const cargaData = () => {
    tbody.innerHTML = lista.map((data, index) => `
        <tr>
            <td>${data.autor}</td>
            <td>${data.titulo}</td>
            <td>${data.descripcion}</td>
            <td class="d-flex gap-3">
                <button class="btn btn-warning" onclick="editarTarea(${index})">Editar</button>
                <button class="btn btn-danger" onclick="eliminarTarea(${index})">Eliminar</button>
            </td>
        </tr>
    `).join("")
}

// Función para editar las tareas de la lista

const editarTarea = (index) => {
    inputTitulo.value = lista[index].titulo
    inputDescripcion.value = lista[index].descripcion
    editarIndex = index
    btnRegistro.textContent = "Editar"
}

// Eliminar tareas

const eliminarTarea = (index) => {
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
          confirmButton: "btn btn-success",
          cancelButton: "btn btn-danger"
        },
        buttonsStyling: false
      });
      swalWithBootstrapButtons.fire({
        title: "¿Estás seguro?",
        text: "No podrás revertir esta acción",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Sí, eliminar",
        cancelButtonText: "No, cancelar",
        reverseButtons: true
      }).then((result) => {
        if (result.isConfirmed) {
            lista.splice(index, 1)
            localStorage.setItem("listaTareas", JSON.stringify(lista))
            cargaData()
            swalWithBootstrapButtons.fire({
                title: "Eliminado",
                text: "La tarea ha sido eliminada",
                icon: "success"
            })
        } else if (
          /* Read more about handling dismissals below */
          result.dismiss === Swal.DismissReason.cancel
        ){
          swalWithBootstrapButtons.fire({
            title: "Cancelado",
            text: "Tu tarea no ha sido eliminada",
            icon: "error"
          });
        }
      });
}

// Función para eliminar todas las tareas

const limpiarLista = () => {
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
          confirmButton: "btn btn-success",
          cancelButton: "btn btn-danger"
        },
        buttonsStyling: false
      });
      swalWithBootstrapButtons.fire({
        title: "¿Estás seguro de eliminar toda la lista?",
        text: "Esto no se puede revertir",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Eliminar",
        cancelButtonText: "Cancelar",
        reverseButtons: true
      }).then((result) => {
        if (result.isConfirmed) {
          localStorage.removeItem("listaTareas")
          lista.length = 0
          cargaData()
            swalWithBootstrapButtons.fire({
                title: "Eliminado",
                text: "La tarea ha sido eliminada",
                icon: "success"
            })
        } else if (
          /* Read more about handling dismissals below */
          result.dismiss === Swal.DismissReason.cancel
        ){
          swalWithBootstrapButtons.fire({
            title: "Cancelado",
            text: "Tu tarea no ha sido eliminada",
            icon: "error"
          });
        }
      });
}

// Función para buscar tareas en tiempo real 

const buscarTarea = (termino) => {
    const resultado = lista.filter(tarea => 
        tarea.titulo.toLowerCase().includes(termino.toLowerCase()) ||
        tarea.descripcion.toLowerCase().includes(termino.toLowerCase())
    )
    tbody.innerHTML = resultado.map((data, index) => `
        <tr>
            <td>${data.autor}</td>
            <td>${data.titulo}</td>
            <td>${data.descripcion}</td>
            <td class="d-flex gap-3">
                <button class="btn btn-warning" onclick="editarTarea(${index})">Actualizar</button>
                <button class="btn btn-danger" onclick="eliminarTarea(${index})">Eliminar</button>
            </td>
        </tr>
    `).join("")
}

cargaData()
