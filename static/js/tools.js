document.addEventListener('DOMContentLoaded', function() {
    var alertElement = document.getElementById('mens');
    if (alertElement) {
      setTimeout(function() {
        alertElement.style.display = 'none';
      }, 3000);
    }
  });