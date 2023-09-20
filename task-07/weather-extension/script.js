var input = document.querySelector('.input_text');
var main = document.querySelector('#name');
var temp = document.querySelector('.temp');
var desc = document.querySelector('.desc');
var feels_like = document.querySelector('.feel');
var button= document.querySelector('.submit');


button.addEventListener('click', function(name){
fetch('https://api.openweathermap.org/data/2.5/weather?q='+input.value+'&appid=12a7f735af05274b88f00f20ad750309')
.then(response => response.json())
.then(data => {
  var tempValue = data['main']['temp'] - 273.15;
  tempValue = tempValue.toFixed(2);
  var nameValue = data['name'];
  var descValue = data['weather'][0]['description'];
  var feels_like_value = data['main']['feels_like'] - 273.15;
  feels_like_value = feels_like_value.toFixed(2);

  main.innerHTML = nameValue;
  desc.innerHTML = "Right now "+nameValue+" has :"+descValue+".";
  feels_like.innerHTML = "Feels like :"+feels_like_value+ " °C";
  temp.innerHTML = "Temperature : "+tempValue + " °C";
  input.value ="";

})

.catch(err => alert("Please enter the correct city name!"));
})