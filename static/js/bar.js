let ep = document.getElementById('ep');
let ef = document.getElementById('ef');
let btnClose = document.getElementById('btnClose');

let ops = [ep,ef];

function filter(id) {
    if (id == "allop") {
      for (let i = 0; i < ops.length; i++) {
        let opc = ops[i];
        if (opc.classList.contains('nShow')) {
          opc.classList.remove('nShow');
        }
        btnClose.click();
      }
    } else if (id == "op1") {
      for (let i = 0; i < ops.length; i++) {
        if(ops[i].classList.contains('nShow')) {
          ops[i].classList.remove('nShow');
        }
        if(ops[i] != ep) {
          ops[i].classList.toggle('nShow');
          btnClose.click();
        }
      }
    } else if (id == "op2") {
      for (let i = 0; i < ops.length; i++) {
        if(ops[i].classList.contains('nShow')) {
          ops[i].classList.remove('nShow');
        }
        if(ops[i] != ef) {
          ops[i].classList.toggle('nShow');
          btnClose.click();
        }
      }
    } 
}

document.addEventListener('DOMContentLoaded', function() {
    const busqueda = document.getElementById('busqueda'); // Asegúrate de que este ID coincide con el de tu input
    const notas = document.querySelectorAll('.cositas #menu_bar .card-body .card-title h3');
    const titulos = document.querySelectorAll('.cositas h2');
    const resul = document.getElementById('general');
  
    // Escucha el evento de entrada en el campo de búsqueda
    busqueda.addEventListener('keyup', function(e) {
      const filtro = e.target.value.toLowerCase(); // Convierte el texto a minúsculas para la comparación
      const value = this.value;
  
      titulos.forEach( function (titulo) {
        if (value.trim() === '') {
          resul.classList.add('nShow');
          titulo.style.display = '';
        } else {
          resul.classList.remove('nShow');
          titulo.style.display = 'none';
        }
      }) 
  
      // Filtra los elementos basados en el texto ingresado
      notas.forEach(function(nota) {
        const padre = nota.closest('#cards_bar')
        if (nota.textContent.toLowerCase().includes(filtro)) {
          padre.style.display = '';
        } else {
          padre.style.display = 'none';
        }
  
      });
    });
});