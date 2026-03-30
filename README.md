# RC-600 Live UI (prototype)

Et enkelt, lokalt web-grensesnitt for livebruk med **Boss RC-600**.

## Hva den gjør nå

- Transportknapper (Start, Stop, Rec, Undo, Redo)
- Tap tempo + BPM input
- Patch-knapper (program change)
- Track-kort med raske handlinger (Rec/Play/Stop/Clear)
- Enkel MIDI-logg (foreløpig mock)

## Kjøring

Åpne `index.html` direkte i nettleser, eller start en lokal server:

```bash
python3 -m http.server 8080
```

Gå til `http://localhost:8080`.

## Neste steg for ekte RC-600-kontroll

1. Bytt `sendMidiMock()` i `app.js` til Web MIDI API (`navigator.requestMIDIAccess`).
2. Mapp knapper til riktig **CC/PC/SysEx** etter ditt RC-600 setup.
3. Lagre flere live-sett i `localStorage`.
4. Legg til MIDI feedback for track-status/LED-lignende visning.
