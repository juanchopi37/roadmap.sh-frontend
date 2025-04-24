# Conceptos Básicos de HTML

## ¿Que es HTML?

HTML significa Hyper Text Markup Language, el cual nos permite crear una especie de estructura de una página web a través de etiquetas que crean elementos en la página web

## Etiquetas en HTML

Las etiquetas nos permiten estructurar la página web a través de una estructura básica a la cual podemos poner otra gran cantidad de etiquetas que nos permiten poner mas contenido nuestra página web y nutrirla mas.

La etiqueta más importante es la `<html></html>` esta define el comienzo y final de todo el contenido de la página web

Luego sigue el `<head></head>` este nos permite definir la información que aparecerá en el navegador como el nombre de la pagina y la información previa que aparece al buscar la página

Por último, tenemos el `<body></body>` que nos permite poner todo el contenido que aparecerá en la página web cuando el usuario entre

## Estructura etiquetas HTML

Existen 2 tipos de etiquetas las que tienen etiqueta de cierre y las que no la necesitan

Las etiquetas siempre estan entre signos de `<` y `>` a la etiqueta de cierre siempre se le pone un `/`

### Estructura básica

## Tags básicos y más usados

- **`<html>`**
  _Contenedor raíz del documento._
  Es la etiqueta que engloba todo el contenido HTML.
- **`<head>`**
  _Metadatos y recursos._
  Aquí van los enlaces a hojas de estilo, scripts, el título de la página y otra info que no se muestra directamente en pantalla.
- **`<title>`**
  _Título del documento._
  Define el texto que aparece en la pestaña del navegador.
- **`<meta>`**
  _Información sobre el documento._
  Se utiliza para definir la codificación, el viewport, autoría, etc.
- **`<link>`**
  _Vinculación a recursos externos._
  Principalmente se usa para enlazar hojas de estilo CSS.
- **`<script>`**
  _Inserción de código JavaScript._
  Añade interactividad y lógica a tu página.
- **`<body>`**
  _Contenido visible de la página._
  Aquí es donde colocas todo lo que los usuarios verán en el navegador.
- **`<header>`**
  _Encabezado de una sección o página._
  Generalmente incluye logotipos, menús de navegación y títulos.
- **`<nav>`**
  _Sección de navegación._
  Contiene los enlaces que permiten moverse por el sitio.
- **`<main>`**
  _Contenido principal._
  Marca la parte central del documento, eliminando distracciones de barras laterales o menús.
- **`<section>`**
  _División temática del contenido._
  Ideal para agrupar bloques de contenido relacionados.
- **`<article>`**
  _Contenido independiente y auto-contenido._
  Perfecto para entradas de blog, noticias o cualquier pieza que pueda estar por sí sola.
- **`<aside>`**
  _Contenido complementario._
  Usado para barras laterales, citas o información adicional.
- **`<footer>`**
  _Pie de página._
  Aquí van los créditos, información de contacto o enlaces legales.
- **`<h1>` a `<h6>`**
  _Encabezados jerárquicos._
  `<h1>` es el título más importante y `<h6>` el menos relevante; organizan y estructuran el contenido.
- **`<p>`**
  _Párrafo._
  Para insertar bloques de texto.
- **`<a>`**
  _Hipervínculo._
  Conecta a otras páginas o secciones de la misma página.
- **`<img>`**
  _Imagen._
  Inserta imágenes y soporta atributos para definir tamaño, alternativa y más.
- **`<ul>`**
  _Lista desordenada._
  Crea listas con viñetas.
- **`<ol>`**
  _Lista ordenada._
  Crea listas numeradas.
- **`<li>`**
  _Elemento de lista._
  Representa cada ítem dentro de `<ul>` o `<ol>`.
- **`<div>`**
  _Contenedor genérico._
  Agrupa contenido para aplicar estilos o manipularlo con scripts sin darle un significado semántico específico.

## Atributos de etiquetas

En esencia los atributos permiten codificar comportamientos dentro de las etiquetas o donde encontrar lo que necesita ya sea un enlace a una página web una imagen que queremos que aparezca en la página o video o audio, todo depende de la página que estemos haciendo

## Atributos básicos de etiquetas

1. **id**
   - **Para qué sirve:** Asigna un identificador único a un elemento, ideal para aplicar estilos o manipularlo con JavaScript.
   - **Ejemplo:**
     ```html
     <div id="header">Contenido del encabezado</div>
     ```
2. **class**
   - **Para qué sirve:** Agrupa elementos para aplicarles los mismos estilos o comportamientos.
   - **Ejemplo:**
     ```html
     <p class="intro">Bienvenido a mi sitio web</p>
     ```
3. **src**
   - **Para qué sirve:** Especifica la ruta de un recurso, como una imagen o un script.
   - **Ejemplo:**
     ```html
     <img src="logo.png" alt="Logotipo de la empresa" />
     ```
4. **href**
   - **Para qué sirve:** Define la URL de destino de un enlace.
   - **Ejemplo:**
     ```html
     <a href="https://ejemplo.com">Visitar Ejemplo</a>
     ```
5. **alt**
   - **Para qué sirve:** Proporciona una descripción alternativa para imágenes, fundamental para la accesibilidad y para el caso de que la imagen no cargue.
   - **Ejemplo:**
     ```html
     <img src="foto.jpg" alt="Descripción de la foto" />
     ```
6. **title**
   - **Para qué sirve:** Muestra información adicional en forma de tooltip cuando el usuario pasa el cursor sobre el elemento.
   - **Ejemplo:**
     ```html
     <span title="Más información sobre este tema">Info</span>
     ```
7. **style**
   - **Para qué sirve:** Aplica estilos CSS directamente al elemento en línea.
   - **Ejemplo:**
     ```html
     <p style="color: blue; font-weight: bold;">Texto en azul y negrita</p>
     ```
8. **target**
   - **Para qué sirve:** Define dónde se abrirá el enlace. Por ejemplo, `_blank` abre el enlace en una nueva pestaña.
   - **Ejemplo:**
     ```html
     <a href="https://ejemplo.com" target="_blank">Abrir en nueva pestaña</a
     ```
9. **rel**
   - **Para qué sirve:** Establece la relación entre el documento actual y el recurso enlazado, importante para SEO y seguridad (como `nofollow` o `noopener`).
   - **Ejemplo:**
     ```html
     <a href="https://ejemplo.com" rel="nofollow">Enlace sin seguimiento</a>
     ```
10. **data-\***
    - **Para qué sirve:** Permite almacenar información personalizada en un elemento sin afectar su semántica. Útil para scripts y aplicaciones interactivas.
    - **Ejemplo:**
      ```html
      <div data-user-id="123" data-role="admin">Usuario</div>
      ```
11. **type**
    - **Para qué sirve:** Especifica el tipo de un elemento, comúnmente usado en inputs y scripts.
    - **Ejemplo:**
      ```html
      <input type="email" name="correo" />
      ```
12. **value**
    - **Para qué sirve:** Define el valor de un elemento, como en campos de formularios, que puede ser un valor por defecto o el valor actual.
    - **Ejemplo:**
      ```html
      <input type="text" value="Texto por defecto" />
      ```
13. **placeholder**
    - **Para qué sirve:** Muestra un texto sugerente en un campo de entrada hasta que el usuario comienza a escribir, ayudando a entender qué se espera en el campo.
    - **Ejemplo:**
      ```html
      <input type="text" placeholder="Ingresa tu nombre" />
      ```
14. **name**
    - **Para qué sirve:** Asigna un nombre al elemento, esencial para enviar datos en formularios, ya que el servidor utiliza este nombre para identificar cada dato.
    - **Ejemplo:**
      ```html
      <input type="password" name="clave" />
      ```
15. **disabled**
    - **Para qué sirve:** Deshabilita un elemento, evitando la interacción del usuario.
    - **Ejemplo:**
      ```html
      <button disabled>Botón inactivo</button>
      ```
16. **required**
    - **Para qué sirve:** Indica que un campo de formulario es obligatorio, de modo que el formulario no se enviará sin completar este campo.
    - **Ejemplo:**
      ```html
      <input type="text" name="usuario" required />
      ```

## Tipos de selección

Los tipos de selección son formas que nos permiten aplicar un estilo a una [etiqueta de HTML](https://www.notion.so/HTML-1936dc665f62803391d5c5ffc8d0491c?pvs=21) esto lo podemos hacer a traves de:

- id: podemos añadir un id en el archivo html y luego invocarlo en el archivo CSS para aplicar un estilo a la etiqueta con el id que hemos creado
  Sintaxis (html)
  ```html
  <div id="id-de-la-clase">contenido de la clase</div>
  ```
  en CSS sería:
  ```css
  #id-de-la-clase {
    /*Contenido del estilo*/
  }
  ```
- class: podemos añadir clases a las etiquetas para que sean llamadas en CSS
  ```html
  <div class="nombre-de-la-clase">Contenido del tag</div>
  ```
  En CSS el llamado sería:
  ```css
  .nombre-de-la-clase {
    /*Aqui iría el contenido del estilo de la etiqueta
  	*/
  }
  ```
- Tipo de etiqueta: Podemos utilizar un estilo especifico para un tipo de tag, por defecto todas las futuras etiquetas que se hagan tendrán como base el estilo que se haya utilizado en dicha etiqueta
