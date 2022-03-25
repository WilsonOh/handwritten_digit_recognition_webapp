let is_drawing = false;

const c = document.getElementById("myCanvas");
const ctx = c.getContext("2d");
const NUM_SQ = 28;
const SQ_SIZE = c.clientHeight / NUM_SQ;

let grid = [];

drawGrid();
init_grid();

c.addEventListener("mousedown", (_) => {
  is_drawing = true;
});

c.addEventListener("mouseup", (_) => {
  is_drawing = false;
});

c.addEventListener("mousemove", (e) => {
  let x = Math.floor(e.offsetX / SQ_SIZE);
  let y = Math.floor(e.offsetY / SQ_SIZE);
  if (is_drawing) {
    grid[x][y] = true;
    if (x < NUM_SQ - 1 && y < NUM_SQ - 1) {
      grid[x + 1][y] = true;
      grid[x + 1][y + 1] = true;
      grid[x][y + 1] = true;
    }
  }
});

c.addEventListener("mousemove", (_) => {
  for (let i = 0; i < NUM_SQ; i++) {
    for (let j = 0; j < NUM_SQ; j++) {
      if (grid[i][j] && is_drawing) {
        ctx.fillRect(i * SQ_SIZE, j * SQ_SIZE, SQ_SIZE, SQ_SIZE);
      }
    }
  }
});

const reset_button = document.getElementById("reset_button");
const submit_button = document.getElementById("submit_button");

submit_button.onclick = () => {
  const xhr = new XMLHttpRequest();
  xhr.onload = () => {
    const result_text = document.getElementById("result_text");
    result_text.innerHTML = `The digit is:<br>${xhr.responseText}</br>`;
  };
  xhr.open("POST", "/submit");
  xhr.setRequestHeader("Accept", "application/json");
  xhr.setRequestHeader("Content-type", "application/json");
  xhr.send(JSON.stringify(printGrid()));
  clearGrid();
};

reset_button.onclick = () => {
  clearGrid();
};

function clearGrid() {
  ctx.clearRect(0, 0, c.clientWidth, c.clientHeight);
  drawGrid();
  init_grid();
}

function drawGrid() {
  for (let i = SQ_SIZE; i < c.clientWidth; i += SQ_SIZE) {
    ctx.moveTo(i, 0);
    ctx.lineTo(i, c.clientHeight);
    ctx.stroke();
  }

  for (let i = SQ_SIZE; i < c.clientHeight; i += SQ_SIZE) {
    ctx.moveTo(0, i);
    ctx.lineTo(c.clientWidth, i);
    ctx.stroke();
  }
}

function init_grid() {
  for (let i = 0; i < NUM_SQ; i++) {
    grid[i] = [];
    for (let j = 0; j < NUM_SQ; j++) {
      grid[i][j] = false;
    }
  }
}

function printGrid() {
  const copy = [];
  for (let i = 0; i < NUM_SQ; i++) {
    copy[i] = [];
    for (let j = 0; j < NUM_SQ; j++) {
      if (grid[j][i]) {
        copy[i][j] = 1;
      } else {
        copy[i][j] = 0;
      }
    }
  }
  return copy;
}
