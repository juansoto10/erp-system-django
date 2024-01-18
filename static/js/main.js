console.log('Hello capibara');

// Wait for the DOM to be ready
document.addEventListener('DOMContentLoaded', function () {
  // Get the button and icons
  const body = document.querySelector('body');
  const toggleButton = document.getElementById('toggle-theme');
  const moonIcon = document.querySelector('ion-icon[name="moon"]');
  const sunnyIcon = document.querySelector('ion-icon[name="sunny"]');
  const isDarkModeActive = JSON.parse(localStorage.getItem('darkMode'));
  const theSideBar = document.querySelector('#the-sidebar');
  const currentLocation = window.location.href;

  isDarkModeActive ? body.classList.add('dark') : body.classList.remove('dark');
  sunnyIcon.style.display = isDarkModeActive ? 'inline' : 'none';
  moonIcon.style.display = isDarkModeActive ? 'none' : 'inline';

  // Add click event listener to the button
  toggleButton.addEventListener('click', function () {
    // Toggle the dark class on the body
    body.classList.toggle('dark');
    localStorage.setItem('darkMode', body.classList.contains('dark'));

    // Toggle the visibility of moon and sunny icons
    moonIcon.style.display = body.classList.contains('dark')
      ? 'none'
      : 'inline';
    sunnyIcon.style.display = body.classList.contains('dark')
      ? 'inline'
      : 'none';
  });

  // console.log(currentLocation);
  // if (currentLocation === 'http://127.0.0.1:8000/')
  //   theSideBar.style.display = 'block';
  // else theSideBar.style.display = 'none';
});
