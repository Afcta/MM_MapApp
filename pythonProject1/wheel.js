let container = document.querySelector(".container");
let btn = document.getElementById("spin");
let number = Math.ceil(Math.random() * 10000);

let flash = document.querySelector(".container div");


btn.onclick = function() {
  container.style.transform = "rotate(" + number + "deg)";
  number += Math.ceil(Math.random() * 10000);

  setTimeout(function() {
    let angle = number % 360;
    if (angle < 60) {
      window.location.href = "map.html";
    } else if (angle < 120) {
    window.location.href = "map.html";
    } else if (angle < 180) {
    window.location.href = "map.html";
    } else if (angle < 240) {
    window.location.href = "map.html";
    } else if (angle < 300) {
    window.location.href = "map.html";
    } else {
    window.location.href = "map.html";
    }
  }, 4000);
};

