document.addEventListener('DOMContentLoaded', () => {
    const loader = document.querySelector('#preloader');
  
    window.addEventListener('load', () => {
      loader.classList.add('fondy-out');
  
      // supprime le préchargeur du DOM après la transition
      setTimeout(() => {
        loader.style.display = 'none';
      }, 500); // durée de la transition en millisecondes
    });
  });
  