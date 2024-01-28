function myFunction(x) {
  x.classList.toggle("change");
  var x = document.getElementById("myDropdown");
  if (x.className === "dropdown") {
    x.className += " responsive";
  } else {
    x.className = "dropdown";
  }
}
