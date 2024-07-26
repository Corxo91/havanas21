const hoverButton = document.getElementById('b1');
const hoverButton2 = document.getElementById('b2');
const component = document.getElementById('index');

function handleHover() {
    component.classList.add('gradientR')
}
function handleHoverL() {
    component.classList.add('gradientL')
}

function handleMouseOut() {
    component.classList.remove('gradientR')
}
function handleMouseOutL() {
    component.classList.remove('gradientL')
}

hoverButton.addEventListener('mouseover', handleHover);
hoverButton2.addEventListener('mouseover', handleHoverL);
hoverButton.addEventListener('mouseout', handleMouseOut);
hoverButton2.addEventListener('mouseout', handleMouseOutL);

document.addEventListener('DOMContentLoaded', function() {
    var alertElement = document.getElementById('sms');
    if (alertElement) {
      setTimeout(function() {
        alertElement.style.display = 'none';
      }, 3000);
    }
<<<<<<< HEAD
  });
=======
  });
>>>>>>> 800db762a542d7ba1511d3ceaf6b32a37e3cc2ec
