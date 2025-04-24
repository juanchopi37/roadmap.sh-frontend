// Arrays o Lista 

const list = [0,1,2,3]

console.log(list)

//Agragar elemento a la lista

list.push(4)
console.log(list)

const list2 = [5,6,7]

//Concatena dos arrays en un nuevo array

const list3 = list.concat(list2)

console.log(list3)

//Elimina el primer elemento de las lista

list.shift()
console.log(list)

//Elimina el ultimo elemento de la lista

list.pop()
console.log(list)

//Recorrer y mostrar toda la lista 

list.forEach((value)=>{
    console.log(value)
})

// Filtrar lista 

const filterList = list.filter((value, index)=> index !== 0)

console.log(filterList)

//

const newList = list3.map((value)=> sum = value + 1)

console.log(newList)

// Extraer los numeros impares 

const list4 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

// const nueva_lista = list4.filter ((index) => index % 2 === 0)
const nueva_lista = []

for (let i = 0; i < list4.length; i++) {
    if (list4[i] % 2 === 0) {
        nueva_lista.push(list4[i])
    }
}

nueva_lista.forEach(function(number, index){
    console.log(index + ":" + number )
})

console.log(nueva_lista)
