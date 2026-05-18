// game/static/game/js/main.js

document.addEventListener("DOMContentLoaded", () => {
// 1. OBTENER LOS DATOS DE DJANGO
    const metadataElement = document.getElementById("game-metadata");
    if (!metadataElement) return;

    const targetWord = metadataElement.getAttribute("data-title");
    const wordLength = parseInt(metadataElement.getAttribute("data-length"));

    console.log("Palabra secreta purificada a adivinar:", targetWord); // Monitoreo en consola hacker

    // 2. CONFIGURACIÓN DEL ESTADO DEL JUEGO
    const maxAttempts = 6;              // Número de intentos estilo Wordle
    let currentAttempt = 0;             // Intento actual del jugador

    // Referencias a los elementos del HTML
    const board = document.getElementById("wordle-board");
    const guessInput = document.getElementById("user-guess");
    const sendBtn = document.getElementById("send-btn");

    // Ajustamos el input para que no deje escribir más letras que las necesarias
    guessInput.maxLength = wordLength;

    // 3. GENERAR LA CUADRÍCULA DINÁMICAMENTE
    // Creamos las filas y celdas vacías basándonos en el largo de la palabra de hoy
    function initBoard() {
        board.innerHTML = ""; // Limpiamos por si acaso
        
        // Configuramos el contenedor CSS Grid dinámicamente para el número de letras
        board.style.display = "grid";
        board.style.gridTemplateRows = `repeat(${maxAttempts}, 1fr)`;
        board.style.gap = "5px";
        board.style.maxWidth = `${wordLength * 50}px`; // Centrado proporcional
        board.style.margin = "20px auto";

        for (let i = 0; i < maxAttempts; i++) {
            const row = document.createElement("div");
            row.className = "grid-row";
            row.style.display = "grid";
            row.style.gridTemplateColumns = `repeat(${wordLength}, 1fr)`;
            row.style.gap = "5px";

            for (let j = 0; j < wordLength; j++) {
                const cell = document.createElement("div");
                cell.className = "letter-box";
                cell.id = `cell-${i}-${j}`;
                
                // Estilos base para las cajitas de las letras
                cell.style.width = "40px";
                cell.style.height = "40px";
                cell.style.border = "1px solid #333";
                cell.style.display = "flex";
                cell.style.justifyContent = "center";
                cell.style.alignItems = "center";
                cell.style.fontFamily = "monospace";
                cell.style.fontWeight = "bold";
                cell.style.color = "#fff";
                cell.style.backgroundColor = "rgba(0,0,0,0.5)";
                cell.style.textTransform = "uppercase";
                
                row.appendChild(cell);
            }
            board.appendChild(row);
        }
    }

    // 4. LÓGICA DE VALIDACIÓN (PROCESAR INTENTO)
    function processGuess() {
        const guess = guessInput.value.trim().toUpperCase();

        // Validaciones básicas de entrada
        if (guess.length !== wordLength) {
            alert(`La respuesta debe tener exactamente ${wordLength} letras.`);
            return;
        }

        // Pintamos las letras del intento actual en la cuadrícula y validamos colores
        for (let i = 0; i < wordLength; i++) {
            const cell = document.getElementById(`cell-${currentAttempt}-${i}`);
            const letter = guess[i];
            cell.textContent = letter;

            // Lógica de colores de Wordle
            if (targetWord[i] === letter) {
                // Letra correcta en la posición correcta (Verde Tecnológico)
                cell.style.backgroundColor = "#2e7d32"; 
                cell.style.borderColor = "#2e7d32";
            } else if (targetWord.includes(letter)) {
                // Letra existe en la palabra pero en otra posición (Amarillo/Dorado sutil)
                cell.style.backgroundColor = "#f57f17";
                cell.style.borderColor = "#f57f17";
            } else {
                // La letra no existe (Gris oscuro de consola)
                cell.style.backgroundColor = "#671212";
                cell.style.borderColor = "#671212";
            }
        }

        // Comprobamos si ganó
        if (guess === targetWord) {
            alert("!MISIÓN CUMPLIDA! Has adivinado el objeto astronómico.");
            endGame();
            return;
        }

        // Siguiente intento
        currentAttempt++;
        guessInput.value = ""; // Limpiamos el cuadro de texto

        // Comprobamos si se quedó sin intentos
        if (currentAttempt >= maxAttempts) {
            alert(`MISIÓN FALLIDA. La palabra correcta era: ${targetWord}`);
            endGame();
        }
    }

    function endGame() {
        guessInput.disabled = true;
        sendBtn.disabled = true;
    }

    // 5. EVENTOS de interacción
    sendBtn.addEventListener("click", processGuess);

    // Permitir enviar la respuesta también al presionar la tecla "Enter"
    guessInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter") {
            processGuess();
        }
    });

    // Arrancamos la cuadrícula al cargar la página
    initBoard();
});