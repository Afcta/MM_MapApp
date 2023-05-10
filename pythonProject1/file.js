function highlightVideoContainer(fileName, elementId) {
  fetch(fileName)
    .then(response => response.text())
    .then(data => {
      const parser = new DOMParser();
      const htmlDoc = parser.parseFromString(data, 'text/html');
      const videoContainer = htmlDoc.getElementById(elementId);
      videoContainer.style.backgroundColor = "grey";
      setTimeout(function() {
        videoContainer.style.backgroundColor = "white";
      }, 1000);
    })
    .catch(error => console.error(error));
}
