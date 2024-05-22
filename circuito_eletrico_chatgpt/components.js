// Definições de classes para diferentes componentes elétricos

// Classe para representar um resistor
class Resistor {
    constructor(x, y, length, width) {
        this.x = x;
        this.y = y;
        this.length = length;
        this.width = width;
    }

    // Desenhar o resistor
    draw() {
        ctx.beginPath();
        ctx.moveTo(this.x, this.y - this.width / 2);
        ctx.lineTo(this.x + this.length / 3, this.y - this.width / 2);
        ctx.lineTo(this.x + 2 * this.length / 3, this.y + this.width / 2);
        ctx.lineTo(this.x + this.length, this.y + this.width / 2);
        ctx.strokeStyle = 'black';
        ctx.lineWidth = 3;
        ctx.stroke();
        ctx.closePath();
    }

    // Verificar se o resistor foi clicado
    isClicked(clickX, clickY) {
        return (
            clickX > this.x && clickX < this.x + this.length &&
            clickY > this.y - this.width / 2 && clickY < this.y + this.width / 2
        );
    }
}

// Classe para representar uma fonte de tensão (bateria)
class Battery {
    constructor(x, y, width, height) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
    }

    // Desenhar a fonte de tensão (bateria)
    draw() {
        ctx.beginPath();
        ctx.rect(this.x, this.y - this.height / 2, this.width, this.height);
        ctx.fillStyle = 'blue';
        ctx.fill();
        ctx.closePath();
    }

    // Verificar se a bateria foi clicada
    isClicked(clickX, clickY) {
        return (
            clickX > this.x && clickX < this.x + this.width &&
            clickY > this.y - this.height / 2 && clickY < this.y + this.height / 2
        );
    }
}

// Classe para representar uma lâmpada
class Lamp {
    constructor(x, y, radius) {
        this.x = x;
        this.y = y;
        this.radius = radius;
    }

    // Desenhar a lâmpada
    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        ctx.fillStyle = 'yellow';
        ctx.fill();
        ctx.closePath();
    }

    // Verificar se a lâmpada foi clicada
    isClicked(clickX, clickY) {
        const dx = clickX - this.x;
        const dy = clickY - this.y;
        const distance = Math.sqrt(dx * dx + dy * dy);
        return distance <= this.radius;
    }
}

// Classe para representar um capacitor
class Capacitor {
    constructor(x, y, width, height) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
    }

    // Desenhar o capacitor
    draw() {
        ctx.beginPath();
        ctx.rect(this.x - this.width / 2, this.y - this.height / 2, this.width, this.height);
        ctx.fillStyle = 'gray';
        ctx.fill();
        ctx.closePath();
    }

    // Verificar se o capacitor foi clicado
    isClicked(clickX, clickY) {
        return (
            clickX > this.x - this.width / 2 && clickX < this.x + this.width / 2 &&
            clickY > this.y - this.height / 2 && clickY < this.y + this.height / 2
        );
    }
}

// Classe para representar um interruptor
class Switch {
    constructor(x, y, width, height) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.state = false; // Estado inicial: desligado
    }

    // Mudar o estado do interruptor
    toggle() {
        this.state = !this.state;
    }

    // Desenhar o interruptor
    draw() {
        ctx.beginPath();
        ctx.rect(this.x - this.width / 2, this.y - this.height / 2, this.width, this.height);
        ctx.fillStyle = this.state ? 'green' : 'red'; // Verde para ligado, vermelho para desligado
        ctx.fill();
        ctx.closePath();
    }

    // Verificar se o interruptor foi clicado
    isClicked(clickX, clickY) {
        return (
            clickX > this.x - this.width / 2 && clickX < this.x + this.width / 2 &&
            clickY > this.y - this.height / 2 && clickY < this.y + this.height / 2
        );
    }
}
