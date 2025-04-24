// //Definimos 

// const persona = {
//     "nombre": "Juan",
//     "edad": "18",
//     "altura": "1,75",
//     "sexo": "masculino"
// }


// console.log(persona)

// console.log(persona.edad)

// persona.nacionalidad = "Colombiano"

// console.log(persona.nacionalidad)

const nombre = document.getElementById("nombre")
const apellido = document.getElementById("apellido")
const edad = document.getElementById("edad")
const registro = document.getElementById("registro")


const registroPersonas = ()=> {
    const data = {
        nombre: nombre.value,
        apellido: apellido.value,
        edad: edad.value
    }

    console.log(data)
}

const data = JSON.stringify(data)
registro.innerHTML = JSON
console.log(JSON)