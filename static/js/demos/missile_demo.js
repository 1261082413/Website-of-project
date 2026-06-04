const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

let score = 0;
let lives = 5;
let missiles = [];
let explosions = [];
let gameOver = false;

const groundY = 475;

const cities = [
    { x: 130, y: groundY, alive: true },
    { x: 280, y: groundY, alive: true },
    { x: 430, y: groundY, alive: true },
    { x: 580, y: groundY, alive: true },
    { x: 730, y: groundY, alive: true },
    { x: 860, y: groundY, alive: true },
];

function createMissile() {
    if (gameOver) return;

    missiles.push({
        x: Math.random() * canvas.width,
        y: 0,
        targetX: Math.random() * canvas.width,
        targetY: groundY,
        speed: 1.3 + Math.random() * 1.2
    });
}

function drawBackground() {
    ctx.fillStyle = "#eef6ff";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = "#dbeafe";
    ctx.fillRect(0, groundY, canvas.width, canvas.height - groundY);

    ctx.fillStyle = "#93c5fd";
    for (let i = 0; i < 14; i++) {
        ctx.fillRect(i * 80, groundY + 35, 45, 10);
    }
}

function drawCities() {
    cities.forEach(city => {
        ctx.fillStyle = city.alive ? "#2563eb" : "#94a3b8";

        ctx.fillRect(city.x - 28, city.y - 28, 56, 28);
        ctx.fillRect(city.x - 18, city.y - 50, 36, 22);
        ctx.fillRect(city.x - 6, city.y - 65, 12, 15);
    });
}

function drawMissiles() {
    missiles.forEach(missile => {
        ctx.strokeStyle = "#ef4444";
        ctx.lineWidth = 2;

        ctx.beginPath();
        ctx.moveTo(missile.x, missile.y);
        ctx.lineTo(missile.targetX, missile.targetY);
        ctx.stroke();

        ctx.fillStyle = "#dc2626";
        ctx.beginPath();
        ctx.arc(missile.x, missile.y, 5, 0, Math.PI * 2);
        ctx.fill();
    });
}

function drawExplosions() {
    explosions.forEach(explosion => {
        ctx.strokeStyle = "#f59e0b";
        ctx.lineWidth = 4;

        ctx.beginPath();
        ctx.arc(explosion.x, explosion.y, explosion.radius, 0, Math.PI * 2);
        ctx.stroke();
    });
}

function drawHUD() {
    ctx.fillStyle = "#111827";
    ctx.font = "bold 22px Arial";
    ctx.fillText("Score: " + score, 24, 34);
    ctx.fillText("Lives: " + lives, 24, 66);

    if (gameOver) {
        ctx.fillStyle = "rgba(15, 23, 42, 0.82)";
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.fillStyle = "#ffffff";
        ctx.font = "bold 52px Arial";
        ctx.fillText("Game Over", 330, 250);

        ctx.font = "22px Arial";
        ctx.fillText("Press Restart Demo to play again", 315, 292);
    }
}

function updateMissiles() {
    missiles.forEach(missile => {
        const dx = missile.targetX - missile.x;
        const dy = missile.targetY - missile.y;
        const distance = Math.sqrt(dx * dx + dy * dy);

        missile.x += (dx / distance) * missile.speed;
        missile.y += (dy / distance) * missile.speed;
    });

    missiles = missiles.filter(missile => {
        if (missile.y >= missile.targetY - 5) {
            lives--;

            const aliveCity = cities.find(city => city.alive);
            if (aliveCity) {
                aliveCity.alive = false;
            }

            if (lives <= 0 || cities.every(city => !city.alive)) {
                gameOver = true;
            }

            return false;
        }

        return true;
    });
}

function updateExplosions() {
    explosions.forEach(explosion => {
        explosion.radius += 1.8;
        explosion.life--;
    });

    explosions = explosions.filter(explosion => explosion.life > 0);
}

canvas.addEventListener("click", function(event) {
    if (gameOver) return;

    const rect = canvas.getBoundingClientRect();
    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;

    const clickX = (event.clientX - rect.left) * scaleX;
    const clickY = (event.clientY - rect.top) * scaleY;

    explosions.push({
        x: clickX,
        y: clickY,
        radius: 10,
        life: 26
    });

    missiles = missiles.filter(missile => {
        const dx = missile.x - clickX;
        const dy = missile.y - clickY;
        const distance = Math.sqrt(dx * dx + dy * dy);

        if (distance < 52) {
            score += 10;
            return false;
        }

        return true;
    });
});

function restartGame() {
    score = 0;
    lives = 5;
    missiles = [];
    explosions = [];
    gameOver = false;

    cities.forEach(city => {
        city.alive = true;
    });
}

function gameLoop() {
    drawBackground();

    if (!gameOver) {
        updateMissiles();
        updateExplosions();
    }

    drawCities();
    drawMissiles();
    drawExplosions();
    drawHUD();

    requestAnimationFrame(gameLoop);
}

setInterval(createMissile, 1100);
gameLoop();