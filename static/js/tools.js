document.addEventListener('DOMContentLoaded', function() {
    var alertElement = document.getElementById('mens');
    if (alertElement) {
      setTimeout(function() {
        alertElement.style.display = 'none';
      }, 3000);
    }
  });

  //funcionalidad del menu hamburguesa

  let ep = document.getElementById('ep');
  let ef = document.getElementById('ef');
  let ec = document.getElementById('ec');
  let ci = document.getElementById('ci');
  let pf = document.getElementById('pf');
  let guar = document.getElementById('guar');
  let pos = document.getElementById('pos');
  let suge = document.getElementById('suge');
  let btnClose = document.getElementById('btnClose');

  let ops = [ep,ef,ec,ci,pf,guar,pos,suge];
  let opz = [ep,ef];

  function filtrar(id) {
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
    } else if (id == "op3") {
      for (let i = 0; i < ops.length; i++) {
        if(ops[i].classList.contains('nShow')) {
          ops[i].classList.remove('nShow');
        }
        if(ops[i] != ec) {
          ops[i].classList.toggle('nShow');
          btnClose.click();
        }
      }
    } else if (id == "op4") {
      for (let i = 0; i < ops.length; i++) {
        if(ops[i].classList.contains('nShow')) {
          ops[i].classList.remove('nShow');
        }
        if(ops[i] != ci) {
          ops[i].classList.toggle('nShow');
          btnClose.click();
        }
      }
    } else if (id == "op5") {
      for (let i = 0; i < ops.length; i++) {
        if(ops[i].classList.contains('nShow')) {
          ops[i].classList.remove('nShow');
        }
        if(ops[i] != pf) {
          ops[i].classList.toggle('nShow');
          btnClose.click();
        }
      }
    } else if (id == "op6") {
      for (let i = 0; i < ops.length; i++) {
        if(ops[i].classList.contains('nShow')) {
          ops[i].classList.remove('nShow');
        }
        if(ops[i] != guar) {
          ops[i].classList.toggle('nShow');
          btnClose.click();
        }
      }
    } else if (id == "op7") {
      for (let i = 0; i < ops.length; i++) {
        if(ops[i].classList.contains('nShow')) {
          ops[i].classList.remove('nShow');
        }
        if(ops[i] != pos) {
          ops[i].classList.toggle('nShow');
          btnClose.click();
        }
      }
    } else if (id == "op8") {
      for (let i = 0; i < ops.length; i++) {
        if(ops[i].classList.contains('nShow')) {
          ops[i].classList.remove('nShow');
        }
        if(ops[i] != suge) {
          ops[i].classList.toggle('nShow');
          btnClose.click();
        }
      }
    }
  }

  function filter(id) {
    if (id == "allop") {
      for (let i = 0; i < ops.length; i++) {
        let opc = opz[i];
        if (opc.classList.contains('nShow')) {
          opc.classList.remove('nShow');
        }
        btnClose.click();
      }
    } else if (id == "op1") {
      for (let i = 0; i < opz.length; i++) {
        if(opz[i].classList.contains('nShow')) {
          opz[i].classList.remove('nShow');
        }
        if(opz[i] != ep) {
          opz[i].classList.toggle('nShow');
          btnClose.click();
        }
      }
    } else if (id == "op2") {
      for (let i = 0; i < opz.length; i++) {
        if(opz[i].classList.contains('nShow')) {
          opz[i].classList.remove('nShow');
        }
        if(opz[i] != ef) {
          opz[i].classList.toggle('nShow');
          btnClose.click();
        }
      }
    } 
}

document.addEventListener('DOMContentLoaded', function() {
  const busqueda = document.getElementById('busqueda'); // Asegúrate de que este ID coincide con el de tu input
  const notas = document.querySelectorAll('.cositas #note h5');
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
      const padre = nota.closest('#target')
      if (nota.textContent.toLowerCase().includes(filtro)) {
        padre.style.display = '';
      } else {
        padre.style.display = 'none';
      }

    });
  });
});


