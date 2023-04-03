const menu1 = document.getElementById('menu1_Americano');
const menu2 = document.getElementById('menu2_CafeLatte');
const menu3 = document.getElementById('menu3_greenTea');
const menuSelect = document.getElementById('menu-select');

menu1.addEventListener('click', () => {
	menuSelect.value = 'menu1_Americano';
});

menu2.addEventListener('click', () => {
	menuSelect.value = 'menu2_CafeLatte';
});

menu3.addEventListener('click', () => {
	menuSelect.value = 'menu3_greenTea';
});
