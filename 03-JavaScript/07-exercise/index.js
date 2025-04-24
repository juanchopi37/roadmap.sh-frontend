//LocalStorage
//Nombre: Valor 

const str = "Hola Mundo";

const num = 10;
const bool = true;

const data = {
    nombre: "Juan",
    edad: 20,
    sexo: "Masculino",
}

const data2 = {
    nombre: "Juan",
    edad: 20,
    sexo: "Masculino",

}

const list = [data, data2]


// const json = JSON.stringify(data)

localStorage.setItem("str", str)
localStorage.setItem("bool", bool)
localStorage.setItem("num", num)

//Devuelve como resultado objeto 

localStorage.setItem("data", JSON.stringify(data))
localStorage.setItem("list", JSON.stringify(list))

// Obtener información del localStorage

const str2 = localStorage.getItem("str")

console.log(str2) // devuelve Hola Mundo

const bool2 = localStorage.getItem("bool")
console.log(bool2) // devuelve true

const num2 = localStorage.getItem("num")

console.log(num2)

const data3 = localStorage.getItem("data")

console.log(data3)

const data4 = JSON.parse(data3)
console.log(data4.nombre)

// Obtener información del localStorage

const list2 = localStorage.getItem("list")
const list3 = JSON.parse(list2)
console.log(list3[0].nombre)