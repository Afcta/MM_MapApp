let container = document.querySelector(".container");
let btn = document.getElementById("spin");
let angle = 0;

btn.onclick = function () {
  let randomAngle = Math.ceil(Math.random() * 3600) + 3600; // Generate a random angle between 3600 and 7200 degrees
  container.style.transform = "rotate(" + randomAngle + "deg)";

  setTimeout(function () {
    angle += randomAngle % 360; // Calculate the new angle by adding the randomAngle modulo 360
    if (angle < 60) {
      window.location.href = "map.html";
    } else if (angle < 120) {
      window.location.href = "worldwar.html";
    } else if (angle < 180) {
      window.location.href = "menu.html";
    } else if (angle < 240) {
      window.location.href = "https://player.stornaway.io/watch/3e9a9f0e";
    } else if (angle < 300) {
      window.location.href = "allVideos.html";
    } else {
      window.location.href = "foodRecipe1.html";
    }
  }, 4000);
};

