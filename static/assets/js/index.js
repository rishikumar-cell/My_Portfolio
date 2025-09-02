const toggleBtn = document.getElementById('toggleBtn');
  const sidebar = document.getElementById('sidebar');
  const toggleIcon = toggleBtn.querySelector('i');

  toggleBtn.addEventListener('click', () => {
    sidebar.classList.toggle('active');

    // Change icon between bars and cross
    if (sidebar.classList.contains('active')) {
      toggleIcon.classList.remove('bi-list');
      toggleIcon.classList.add('bi-x');
    } else {
      toggleIcon.classList.remove('bi-x');
      toggleIcon.classList.add('bi-list');
    }
  });





   const roles = ["Freelancer", "Developer", "Designer", "Blogger"];
  const typedText = document.getElementById("typed-text");
  let roleIndex = 0;
  let charIndex = 0;
  let typingSpeed = 100; // ms per character
  let erasingSpeed = 50; // ms per character
  let delayBetweenRoles = 1500; // ms before next word

  function typeRole() {
    if (charIndex < roles[roleIndex].length) {
      typedText.textContent += roles[roleIndex].charAt(charIndex);
      charIndex++;
      setTimeout(typeRole, typingSpeed);
    } else {
      setTimeout(eraseRole, delayBetweenRoles);
    }
  }

  function eraseRole() {
    if (charIndex > 0) {
      typedText.textContent = roles[roleIndex].substring(0, charIndex - 1);
      charIndex--;
      setTimeout(eraseRole, erasingSpeed);
    } else {
      roleIndex = (roleIndex + 1) % roles.length;
      setTimeout(typeRole, typingSpeed);
    }
  }

  // Start the typing effect
  document.addEventListener("DOMContentLoaded", () => {
    if (roles.length) setTimeout(typeRole, 500);
  });

const themeToggle = document.getElementById('theme-toggle');
const themeIcon = document.getElementById('theme-icon');

themeToggle.addEventListener('click', () => {
  document.body.classList.toggle('dark-theme');

  // Switch icon
  if(document.body.classList.contains('dark-theme')){
    themeIcon.classList.remove('fa-moon');
    themeIcon.classList.add('fa-sun');
  } else {
    themeIcon.classList.remove('fa-sun');
    themeIcon.classList.add('fa-moon');
  }
});





  window.addEventListener('DOMContentLoaded', () => {
    const toastMessages = document.querySelectorAll('.toast-message');
    toastMessages.forEach(msg => {
        setTimeout(() => {
            msg.style.display = 'none';
        }, 4000); // 4 seconds
    });
  });

