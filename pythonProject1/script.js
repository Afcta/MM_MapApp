const videoContainers = document.querySelectorAll('.video-container');

function showVideos(category) {
  videoContainers.forEach(container => {
    const videoCategory = container.getAttribute('data-category');
    if (videoCategory === category || category === 'all') {
      container.style.display = 'flex';
    } else {
      container.style.display = 'none';
    }
  });
}

const buttons = document.querySelectorAll('.category-button');
buttons.forEach(button => {
  button.addEventListener('click', () => {
    const category = button.getAttribute('data-category');
    showVideos(category);
  });
});