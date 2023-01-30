const url = 'http://127.0.0.1:8000';
var csrftoken = '';

document.addEventListener("DOMContentLoaded", function(){
  setUpDropDowns();
  csrftoken = getCookie('csrftoken');
});

function setUpDropDowns(){
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

  let graph_dropdown = document.querySelector('#graph_list');

  graph_dropdown.onchange = function() {
    selected_graph_name = graph_dropdown.value;
    const request = new XMLHttpRequest();
    request.onreadystatechange = function () {
      if (request.readyState === 4 && request.status === 200) {
        location.reload();
      }
    };
    request.open('GET', `${url}/choose_graph/${selected_graph_name}`, true);
    request.send();
  }
}

function getCookie(name) {
  var value = "; " + document.cookie;
  var parts = value.split("; " + name + "=");
  if (parts.length == 2) return parts.pop().split(";").shift();
}

let apply_btn = document.querySelector('#apply_filter_and_search');
apply_btn.addEventListener('click', function(event){
  event.stopPropagation();
  const request = new XMLHttpRequest();
  request.open('POST', `${url}/filter`, true);
  request.setRequestHeader('Content-Type', 'application/json');
  request.setRequestHeader("X-CSRFToken", csrftoken);
  request.onreadystatechange = function () {
      if (request.readyState === 4 && request.status === 200) {
        location.reload();
      }
  };

  let searchContent = document.querySelector('#search_input').value;

  let attributeContent = document.querySelector('#attribute').value;
  let operatorContent = document.querySelector('#operator').value;
  let valueContent = document.querySelector('#filter_value').value;

  if(searchContent != '' || valueContent != ''){
    const body = JSON.stringify({search: searchContent, filter: {attribute: attributeContent, operator: operatorContent, value: valueContent}});
    request.send(body);
  }  
});

let remove_search_query_buttons = document.querySelectorAll('.remove_search_query');
let remove_filter_query_buttons = document.querySelectorAll('.remove_filter_query');

for(let btn of remove_search_query_buttons){
  btn.addEventListener('click', function(event){
    event.stopPropagation();
    const request = new XMLHttpRequest();
    request.onreadystatechange = function () {
      if (request.readyState === 4 && request.status === 200) {
        location.reload();
      }
    };
    request.open('GET', `${url}/delete_search_query/${btn.id}`, true);
    request.send();
  })
}

for(let btn of remove_filter_query_buttons){
  btn.addEventListener('click', function(event){
    event.stopPropagation();
    const request = new XMLHttpRequest();
    request.onreadystatechange = function () {
      if (request.readyState === 4 && request.status === 200) {
        location.reload();
      }
    };
    request.open('GET', `${url}/delete_filter_query/${btn.id}`, true);
    request.send();
  })
}

