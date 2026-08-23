// Fade-in sections on scroll
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if(entry.isIntersecting){
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.2 });

document.querySelectorAll('.hero-content, .about, .products').forEach(section => {
  observer.observe(section);
});

// Shrink header on scroll
window.addEventListener('scroll', () => {
  const header = document.querySelector('.header');
  header.classList.toggle('shrink', window.scrollY > 50);
});

// Scroll down arrow
document.querySelector('.scroll-down').addEventListener('click', () => {
  document.querySelector('.about').scrollIntoView({ behavior: 'smooth' });
});

// Autoplay video fix for iOS
const video = document.getElementById('heroVideo');

function tryPlayVideo() {
  video.muted = true;
  video.playsInline = true;

  const playPromise = video.play();
  if (playPromise !== undefined) {
    playPromise.catch(() => {
      const retry = () => {
        video.play();
        document.removeEventListener('click', retry);
        document.removeEventListener('touchstart', retry);
      };
      document.addEventListener('click', retry);
      document.addEventListener('touchstart', retry);
    });
  }
}

window.addEventListener('load', tryPlayVideo);
