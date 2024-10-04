let currentIndex = 0;
const items = document.querySelectorAll('.slider-item');
const totalItems = items.length;

document.getElementById('next').addEventListener('click', () => {
    moveToNextSlide();
});

document.getElementById('prev').addEventListener('click', () => {
    moveToPrevSlide();
});

function updateSlider() {
    items.forEach((item, index) => {
        item.style.display = index === currentIndex ? 'block' : 'none';
    });
}

function moveToNextSlide() {
    currentIndex = (currentIndex + 1) % totalItems;
    updateSlider();
}

function moveToPrevSlide() {
    currentIndex = (currentIndex - 1 + totalItems) % totalItems;
    updateSlider();
}

updateSlider();
