let modo = "";

let tableroActual = [];
let turnoActual = "X";

function iniciar(m) {
  modo = m;

  fetch("/iniciar", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ modo: m })
  })
    .then(res => res.json())
    .then(data => {
      document.getElementById("modo").style.display = "none";
      document.getElementById("juego").style.display = "block";
      document.getElementById("estado").textContent = "Turno de X";
      document.getElementById("estado").dataset.finalizado = "";
    });
}

function dibujarTablero(tablero) {
  const cont = document.getElementById("tablero");
  cont.innerHTML = "";

  const finalizado = document.getElementById("estado").dataset.finalizado === "true";

  tablero.forEach((fila, i) => {
    fila.forEach((celda, j) => {
      const div = document.createElement("div");
      div.className = "celda";
      div.textContent = celda;
      if (celda === "" && !finalizado) {
        div.addEventListener("click", () => jugar(i, j));
      }
      cont.appendChild(div);
    });
  });
}

function jugar(i, j) {
  if (document.getElementById("estado").dataset.finalizado === "true") return;
  if (tableroActual[i][j] !== "") return;

  tableroActual[i][j] = turnoActual;
  dibujarTablero(tableroActual);
  document.getElementById("estado").textContent = "Pensando...";

  fetch("/movimiento", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ fila: i, columna: j })
  })
    .then(res => res.json())
    .then(data => {
      setTimeout(() => {
        tableroActual = data.tablero;
        dibujarTablero(tableroActual);

        if (data.ganador) {
          document.getElementById("estado").textContent = `Ganó: ${data.ganador}`;
          document.getElementById("estado").dataset.finalizado = "true";
        } else if (data.empate) {
          document.getElementById("estado").textContent = "Empate";
          document.getElementById("estado").dataset.finalizado = "true";
        } else {
          turnoActual = data.turno;
          document.getElementById("estado").textContent = `Turno de ${data.turno}`;
        }
      }, modo === "humano" ? 0 : 600);
      dibujarTablero(data.tablero);

      if (data.ganador) {
        document.getElementById("estado").textContent = `Ganó: ${data.ganador}`;
        document.getElementById("estado").dataset.finalizado = "true";
      } else if (data.empate) {
        document.getElementById("estado").textContent = "Empate";
        document.getElementById("estado").dataset.finalizado = "true";
      } else {
        document.getElementById("estado").textContent = `Turno de ${data.turno}`;
      }
    });
}

function reiniciar() {
  iniciar(modo);
}
