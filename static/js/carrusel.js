const html = document.documentElement;

const carrusel = document.getElementById("carrusel")
const screen_height = window.innerHeight;
const screen_width = window.innerWidth;

const dinamic_link = document.getElementById("dinamic-link");

const links = {
    1:"https://google.com",
    2:"https://github.com",
    3:"https://microsoft.com",
    4:"https://apple.com",
    5:"https://redmagic.com"
}

html.style.setProperty("--screen_width", `${screen_width}px`);
html.style.setProperty("--screen_height", `${screen_height}px`);

let index = 1;

function chanche_img() {
    if (index >= 5) {
        index = 0;
    }

    let move = -index * screen_width;
    carrusel.style.translate = move + "px";

    for (let i = 1; i < 6; i++) {
        const link1 = document.getElementById(`cl${i}`);
        link1.style.background = "rgba(128, 128, 128, 0.151)";
    }

    const link = document.getElementById(`cl${index+1}`);
    link.style.background = "var(--elements_color_3)";

    const link_button = document.getElementById("dinamic-link");
    link_button.href = links[index+1];

    index++
}

function front_img() {
    chanche_img();
    clearInterval(intervalo);
    intervalo = setInterval(chanche_img, 5000);
}

function back_img() {
    if (index === 1) {
        index = 4;
    }
    else {
        index -= 2;
    }
    chanche_img();
    clearInterval(intervalo);
    intervalo = setInterval(chanche_img, 5000);
}

let intervalo = setInterval(chanche_img, 5000)