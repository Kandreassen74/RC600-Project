const patches = [
  "01 Intro Drone",
  "02 Verse Clean",
  "03 Chorus Drive",
  "04 Breakdown",
  "05 Solo",
  "06 Ambient Out"
];

const tracks = Array.from({ length: 6 }, (_, i) => `Track ${i + 1}`);
const logElement = document.querySelector("#log");
const patchGrid = document.querySelector("#patch-grid");
const trackGrid = document.querySelector("#track-grid");
const trackTemplate = document.querySelector("#track-template");

let activePatch = null;
let tapTimes = [];

function log(message) {
  const timestamp = new Date().toLocaleTimeString("no-NO", { hour12: false });
  logElement.textContent = `[${timestamp}] ${message}\n${logElement.textContent}`.slice(0, 4000);
}

function sendMidiMock(type, payload) {
  // Bytt ut med WebMIDI-send når RC-600 er koblet til.
  log(`MIDI ${type}: ${JSON.stringify(payload)}`);
}

function renderPatches() {
  patchGrid.innerHTML = "";

  patches.forEach((name, index) => {
    const button = document.createElement("button");
    button.textContent = name;
    button.dataset.patch = String(index + 1);
    button.addEventListener("click", () => {
      activePatch = index;
      renderPatches();
      sendMidiMock("programChange", { program: index });
      log(`Byttet til patch: ${name}`);
    });

    if (activePatch === index) {
      button.classList.add("active");
    }

    patchGrid.appendChild(button);
  });
}

function renderTracks() {
  tracks.forEach((trackName, index) => {
    const fragment = trackTemplate.content.cloneNode(true);
    const card = fragment.querySelector(".track-card");
    const title = fragment.querySelector("h3");
    title.textContent = trackName;

    fragment.querySelectorAll("[data-track-action]").forEach((button) => {
      button.addEventListener("click", () => {
        const action = button.dataset.trackAction;
        sendMidiMock("cc", { track: index + 1, action });
        log(`${trackName}: ${action}`);
        if (action === "clear") {
          card.classList.remove("active");
        } else {
          card.classList.add("active");
        }
      });
    });

    trackGrid.appendChild(fragment);
  });
}

function setupTransport() {
  document.querySelectorAll("[data-action]").forEach((button) => {
    button.addEventListener("click", () => {
      sendMidiMock("transport", { action: button.dataset.action });
      log(`Transport: ${button.dataset.action}`);
    });
  });

  const tempoInput = document.querySelector("#tempo");
  tempoInput.addEventListener("change", () => {
    const bpm = Number(tempoInput.value);
    sendMidiMock("tempo", { bpm });
    log(`Tempo satt til ${bpm} BPM`);
  });

  document.querySelector("#tap-tempo").addEventListener("click", () => {
    const now = Date.now();
    tapTimes.push(now);
    tapTimes = tapTimes.slice(-6);

    if (tapTimes.length < 2) {
      return;
    }

    const intervals = tapTimes.slice(1).map((time, i) => time - tapTimes[i]);
    const avg = intervals.reduce((sum, value) => sum + value, 0) / intervals.length;
    const bpm = Math.round(60000 / avg);

    if (bpm >= 30 && bpm <= 240) {
      tempoInput.value = String(bpm);
      sendMidiMock("tempo", { bpm, source: "tap" });
      log(`Tap tempo: ${bpm} BPM`);
    }
  });
}

renderPatches();
renderTracks();
setupTransport();
log("RC-600 Live UI klar.");
