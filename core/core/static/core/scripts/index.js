let dropdown = document.querySelector('#providers_dropdown');
dropdown.addEventListener('click', function(event) {
  event.stopPropagation();
  dropdown.classList.toggle('is-active');
});

let dropdown_visualizators = document.querySelector('#dropdown-visualizators');
dropdown_visualizators.addEventListener('click', function(event) {
  event.stopPropagation();
  dropdown_visualizators.classList.toggle('is-active');
});

