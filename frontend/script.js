let modo = "";
let turno = "X"; // usado solo en modo humano vs humano

function iniciar(m) {
  modo = m;

  fetch("/iniciar", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({modo: m})
  }).then(() => {
    document.getElementById("modo").style.display = "none";
    document.getElementById("juego").style.display = "block";
    dibujarTablero([
      ["", "", ""],
      ["", "", ""],
      ["", "", ""]
    ]);
    document.getElementById("estado").textContent = `Turno de X`;
  });
}

function dibujarTablero(tablero) {
  const cont = document.getElementById("tablero");
  cont.innerHTML = "";

  tablero.forEach((fila, i) => {
    fila.forEach((celda, j) => {
      const div = document.createElement("div");
      div.className = "celda";
      div.textContent = celda;
      if (celda === "") {
        div.onclick = () => jugar(i, j);
      }
      cont.appendChild(div);
    });
  });
}

function jugar(i, j) {
  fetch("/movimiento", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({fila: i, columna: j})
  })
  .then(res => res.json())
  .then(data => {
    dibujarTablero(data.tablero);

    if (data.ganador) {
      document.getElementById("estado").textContent = `Ganó: ${data.ganador}`;
    } else if (data.empate) {
      document.getElementById("estado").textContent = "Empate";
    } else {
      document.getElementById("estado").textContent = `Turno de ${data.turno}`;
    }
  });
}
