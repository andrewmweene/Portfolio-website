const menuToggle = document.querySelector('.menu-toggle');
const menu = document.querySelector('.nav-menu');

if (menuToggle && menu) {
    menuToggle.addEventListener('click', () => {
        const open = menuToggle.getAttribute('aria-expanded') === 'true';
        menuToggle.setAttribute('aria-expanded', String(!open));
        menu.classList.toggle('is-open', !open);
    });

    menu.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => {
        menuToggle.setAttribute('aria-expanded', 'false');
        menu.classList.remove('is-open');
    }));
}