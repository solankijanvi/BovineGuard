let menu = document.querySelector('#menu-btn');
let navbar = document.querySelector('.navbar');

menu.onclick = () => {
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
};

window.onscroll = () => {
    menu.classList.remove('fa-times');
    navbar.classList.remove('active');
};
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('review-form');
    const reviewContainer = document.getElementById('review-container');

    form.addEventListener('submit', (event) => {
        event.preventDefault();

        // Get form data
        const name = document.getElementById('name').value;
        const reviewText = document.getElementById('review-text').value;

        // Create new review element
        const reviewBox = document.createElement('div');
        reviewBox.className = 'box';

        reviewBox.innerHTML = `

            <h3>${name}</h3>
            <p class="text">${reviewText}</p>
        `;

        
        reviewContainer.prepend(reviewBox);

        
        form.reset();
    });
});

