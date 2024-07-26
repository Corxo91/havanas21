document.addEventListener('DOMContentLoaded', function() {
    var alertElement = document.getElementById('mens');
    if (alertElement) {
      setTimeout(function() {
        alertElement.style.display = 'none';
      }, 3000);
    }
  });
<<<<<<< HEAD


  let ingredientCounter = 3; // Empezamos con 3 campos por defecto

function addIngredientField() {
  ingredientCounter++;

  // Crear un nuevo div para el nuevo campo de ingrediente
  let newIngredientDiv = document.createElement('div');
  newIngredientDiv.classList.add('input-group', 'mb-3', 'inputI');

  // Crear el nuevo campo de ingrediente
  let newIngredientLabel = document.createElement('span');
  newIngredientLabel.classList.add('input-group-text', 'border', 'border-danger-subtle');
  newIngredientLabel.textContent = 'Ingrediente y Cantidad';

  let newIngredientInput1 = document.createElement('input');
  newIngredientInput1.type = 'text';
  newIngredientInput1.classList.add('form-control', 'border', 'border-danger-subtle');
  newIngredientInput1.ariaLabel = 'First name';
  newIngredientInput1.name = `ing${ingredientCounter}`;

  let newIngredientInput2 = document.createElement('input');
  newIngredientInput2.type = 'text';
  newIngredientInput2.classList.add('form-control', 'border', 'border-danger-subtle');
  newIngredientInput2.ariaLabel = 'Last name';
  newIngredientInput2.name = `cant${ingredientCounter}`;

  // Agregar los nuevos elementos al div
  newIngredientDiv.appendChild(newIngredientLabel);
  newIngredientDiv.appendChild(newIngredientInput1);
  newIngredientDiv.appendChild(newIngredientInput2);

  // Agregar el nuevo div al formulario
  let lastIngredientInput = document.querySelector('.ultimo');

  // Insertar el nuevo div antes del último input con clase 'ultimo'
  lastIngredientInput.parentNode.insertBefore(newIngredientDiv, lastIngredientInput);
}

function addIngredientField2() {
  ingredientCounter++;

  // Crear un nuevo div para el nuevo campo de ingrediente
  let newIngredientDiv = document.createElement('div');
  newIngredientDiv.classList.add('input-group', 'mb-3', 'inputI');

  // Crear el nuevo campo de ingrediente
  let newIngredientLabel = document.createElement('span');
  newIngredientLabel.classList.add('input-group-text', 'border', 'border-danger-subtle');
  newIngredientLabel.textContent = 'Ingrediente y Cantidad';

  let newIngredientInput1 = document.createElement('input');
  newIngredientInput1.type = 'text';
  newIngredientInput1.classList.add('form-control', 'border', 'border-danger-subtle');
  newIngredientInput1.ariaLabel = 'First name';
  newIngredientInput1.name = `ing${ingredientCounter}`;

  let newIngredientInput2 = document.createElement('input');
  newIngredientInput2.type = 'text';
  newIngredientInput2.classList.add('form-control', 'border', 'border-danger-subtle');
  newIngredientInput2.ariaLabel = 'Last name';
  newIngredientInput2.name = `cant${ingredientCounter}`;

  // Agregar los nuevos elementos al div
  newIngredientDiv.appendChild(newIngredientLabel);
  newIngredientDiv.appendChild(newIngredientInput1);
  newIngredientDiv.appendChild(newIngredientInput2);

  // Agregar el nuevo div al formulario
  let lastIngredientInput = document.querySelector('.ultimo2');

  // Insertar el nuevo div antes del último input con clase 'ultimo'
  lastIngredientInput.parentNode.insertBefore(newIngredientDiv, lastIngredientInput);
}

function removeIngredientField() {
  if (ingredientCounter > 3) {
    // Seleccionar el último div con la clase 'inputI'
    let lastIngredientDiv = document.querySelectorAll('.inputI')[ingredientCounter - 1];

    // Remover el div del formulario
    lastIngredientDiv.parentNode.removeChild(lastIngredientDiv);

    // Decrementar el contador de ingredientes
    ingredientCounter--;
  }
}

  let cocina = document.getElementById('contenido')
    carta = document.getElementById('contenido_carta');
    cartaBar = document.getElementById('contenido_bar');
    nav = document.getElementById('nav_contenido');

function returnCocina() {
  cocina.style.display = "block";
  nav.style.display = "";
  carta.style.display = "none";
}

function returnCarta() {
  cocina.style.display = "none";
  carta.style.display = "block";
  nav.style.display = "none";
}
function returnBar() {
  cocina.style.display = "block";
  nav.style.display = "";
  cartaBar.style.display = "none";
}

function returnCartaBar() {
  cocina.style.display = "none";
  cartaBar.style.display = "block";
  nav.style.display = "none";
}
=======
>>>>>>> 800db762a542d7ba1511d3ceaf6b32a37e3cc2ec
