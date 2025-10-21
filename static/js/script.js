document.getElementById('mode-toggle').addEventListener('click', () => {
    document.body.classList.toggle('dark');
});
function openBuyModal(productId) {
    document.getElementById('product_id').value = productId;
    document.getElementById('buyModal').style.display = 'block';
}

function closeBuyModal() {
    document.getElementById('buyModal').style.display = 'none';
}
const modeToggle = document.getElementById('mode-toggle');
const body = document.body;

modeToggle.addEventListener('click', () => {
    body.classList.toggle('dark');
    localStorage.setItem('darkMode', body.classList.contains('dark'));
});

// LocalStorage’dan dark mode holatini tekshirish



// sahifa yangilanganda ham holatni saqlash
if (localStorage.getItem('darkMode') === 'true') {
    body.classList.add('dark');
}
document.addEventListener("DOMContentLoaded", function () {
    const faqItems = document.querySelectorAll(".faq-item");

    faqItems.forEach(item => {
        const question = item.querySelector(".faq-question");
        question.addEventListener("click", () => {
            item.classList.toggle("active");

            // boshqa ochilganlarni yopish
            faqItems.forEach(other => {
                if (other !== item) other.classList.remove("active");
            });
        });
    });
});