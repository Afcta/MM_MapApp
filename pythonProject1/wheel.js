let container = document.querySelector(".container");
let btn = document.getElementById("spin");
let number = Math.ceil(Math.random() * 10000);

let flash = document.querySelector(".container div");


btn.onclick = function() {
  container.style.transform = "rotate(" + number + "deg)";
  number += Math.ceil(Math.random() * 10000);

  setTimeout(function() {
    let angle = number % 360;
    if (angle < 90) {
      window.location.href = "worldwar.html";
    } else if (angle < 180) {
    window.location.href = "https://player.stornaway.io/watch/3e9a9f0e";
    } else if (angle < 270) {
    window.location.href = "map.html";
    } else {
    window.location.href = "allVideos.html";
    }
  }, 4000);
};

