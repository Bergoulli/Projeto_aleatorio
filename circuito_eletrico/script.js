// Lógica para manipular a interface do usuário e interação do usuário

// Obtendo o canvas e o contexto
const canvas = document.getElementById('circuitCanvas');
const ctx = canvas.getContext('2d');

// Definindo as dimensões do canvas
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Lista de componentes no circuito
let components = [];

// Adicionar um componente ao circuito
function addComponent(component) {
    components.push(component);
}

// Remover um componente do circuito
function removeComponent(component) {
    components = components.filter(comp => comp !== component);
    drawCircuit();
}

// Desenhar o circuito
function drawCircuit() {
    // Limpar o canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Desenhar todos os componentes
    components.forEach(component => {
        component.draw();
    });
}

// Redesenhar o circuito quando a janela for redimensionada
window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    drawCircuit();
});

// Adicionar um resistor ao circuito
const resistor = new Resistor(100, 200, 100, 20);
addComponent(resistor);

// Adicionar uma fonte de tensão (bateria) ao circuito
const battery = new Battery(300, 200, 50, 20);
addComponent(battery);

// Adicionar uma lâmpada ao circuito
const lamp = new Lamp(500, 200, 50, 20);
addComponent(lamp);

// Adicionar um capacitor ao circuito
const capacitor = new Capacitor(700, 200, 20, 20);
addComponent(capacitor);

// Adicionar um interruptor ao circuito
const switchComponent = new Switch(900, 200, 30, 20);
addComponent(switchComponent);

// Desenhar o circuito
drawCircuit();

// Evento de clique para remover componentes
canvas.addEventListener('click', (event) => {
    const clickX = event.clientX - canvas.offsetLeft;
    const clickY = event.clientY - canvas.offsetTop;

    // Verificar se algum componente foi clicado
    components.forEach(component => {
        if (component.isClicked(clickX, clickY)) {
            removeComponent(component);
        }
    });
});
