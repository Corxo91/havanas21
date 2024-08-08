document.getElementById('formulario').addEventListener('submit', function(event) {  
    event.preventDefault();

    let recipe = document.getElementById('recipe');
    let descrip = document.getElementById('descrip');
    let steps = document.getElementById('steps');
    let price = document.getElementById('price');
    let price_alter = document.getElementById('price_alter');
    let time_out = document.getElementById('time_out');
    let count = parseInt(document.getElementById('iteraciones').value);

    // Verifica y llena placeholders para los primeros campos
    [recipe, descrip, steps, price, price_alter, time_out].forEach(function(field) {
        if (!field.value) {
            field.value = field.placeholder || '';
        }
    });

    // Itera sobre los inputs dinámicos y verifica placeholders
    for (let i = 1; i <= count; i++) {
        let inputId = 'ing' + i;
        let amountId = 'cant' + i;
        let input = document.getElementById(inputId);
        let amount = document.getElementById(amountId)
        if (input && !input.value) {
            input.value = input.placeholder || '';
        }
        if (amount && !amount.value) {
            amount.value = amount.placeholder || '';
        }
    }

    this.submit();
});


document.getElementById('formularioo').addEventListener('submit', function(e) {
    e.preventDefault();
    let cuenta = parseInt(document.getElementById('itera').value);
    // Itera sobre los inputs dinámicos y verifica placeholders
    for (let i = 1; i <= cuenta; i++) {
        let valorID = 'imageID' + i
        let valor = document.getElementById(valorID)
        if (valor.value === "") {
            valor.value = "null"
        }
    }
    this.submit();
});


document.getElementById('formulariou').addEventListener('submit', function(e) {
    e.preventDefault();
    let cuenta = parseInt(document.getElementById('iteraC').value);
    console.log(cuenta);
    // Itera sobre los inputs dinámicos y verifica placeholders
    for (let i = 1; i <= cuenta; i++) {
        let valorID = 'imageIDC' + i
        let valor = document.getElementById(valorID)
        if (valor.value === "") {
            valor.value = "null"
        }
    }
    this.submit();
});

document.getElementById('most').addEventListener('click', function() {
    document.getElementById('photoW').click();
});
document.getElementById('mostC').addEventListener('click', function() {
    document.getElementById('photoC').click();
});
document.getElementById('camarera').addEventListener('click', function () { 
    document.getElementById('photo_pirncipal').click();
})

let cerrar = document.querySelectorAll('.cerrar')

cerrar.forEach(function (e) {
    let svg = e.querySelector('.cruz')
    let input = e.querySelector('.imagenID')
    let id = e.querySelector('.id').getAttribute('data-id')
    e.addEventListener('click', function () {
        if (e.classList.contains('modi')) {
            e.style.backgroundColor = "white"
            svg.style.color = "#901a34"
            input.value = ""
            e.classList.remove('modi')
        } else {
            e.style.backgroundColor = "#901a34"
            svg.style.color = "white"
            input.value = id
            e.classList.add('modi')
        }
    })
})

document.addEventListener('DOMContentLoaded', function() {
    var textarea = document.getElementById('descrip');
    var charCountSpan = document.getElementById('charCount');

    // Función para actualizar el contador de caracteres
    function updateCharCount() {
        var length = textarea.value.length;
        charCountSpan.textContent = `${length}/195`;
    }

    // Actualiza el contador de caracteres inicialmente si el textarea ya tiene contenido
    if (textarea.value.length > 0) {
        updateCharCount();
    }

    // Controlador de eventos para el evento input
    textarea.addEventListener('input', updateCharCount);

    // Controlador de eventos para el evento keydown
    textarea.addEventListener('keydown', function(event) {
        var length = this.value.length;

        // Evita que se añadan más caracteres si ya se alcanzó el límite
        if (length >= 195 && event.key !== "Backspace") {
            event.preventDefault(); // Impide la adición de caracteres adicionales
        }
    });
});



