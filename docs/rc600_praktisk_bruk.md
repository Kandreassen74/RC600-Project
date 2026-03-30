# Praktisk læringsguide: Boss RC-600 (livebruk)

## 1) Mål med oppsettet
Denne guiden er laget for øving og livebruk med Boss RC-600, med fokus på:
- trygg og rask betjening under konsert
- tydelig struktur for spor (tracks), rytme og låtdeler
- repeterbare økter slik at du bygger muskelminne

## 2) Foreslått grunnoppsett på RC-600
- Track 1: Tromme/perkusjon-loop
- Track 2: Basslinje
- Track 3: Harmoni (pads/akkorder)
- Track 4: Riff/komp
- Track 5: Lead/one-shot
- Track 6: FX/tekstur/overganger

Tips:
- Hold samme funksjon per track i alle låter.
- Gi patchene navn etter låt + del (f.eks. "SongA_Intro").
- Bruk lik farge-/nivålogikk på alle patcher.

## 3) 4-ukers øvingsplan

### Uke 1 – Kontroll og timing
- Mål: Kunne starte/stoppe/record uten å se ned lenge.
- Økt A (20 min): Start/Stop/Undo/Redo i 80–100 BPM.
- Økt B (20 min): Tap tempo i 4/4 og sjekk stabil BPM.
- Økt C (20 min): Bytt mellom 3 patcher uten timing-brudd.

### Uke 2 – Layering og arrangement
- Mål: Bygge vers/refreng med 2–4 tracks.
- Økt A: Spill inn tromme + bass med quantize.
- Økt B: Legg harmoni og mut track raskt.
- Økt C: Øv overgang vers -> refreng på cue.

### Uke 3 – Liveflyt
- Mål: Simulere låter fra start til slutt.
- Økt A: 1 komplett låt, ingen stopp.
- Økt B: 2 låter i serie med patch-bytte.
- Økt C: Feilhåndtering (bevisst feil + recovery).

### Uke 4 – Scene-simulering
- Mål: Tåle press og holde stabil struktur.
- Økt A: Spill stående med monitornivå lik scene.
- Økt B: Øv med metronom av/på.
- Økt C: 15-min mini-sett med logging etterpå.

## 4) Sjekkliste før øving/live
- Riktig output-routing og nivå
- Riktig patch-bank lastet
- Tempo/rytme bekreftet
- Expression/CTL-pedaler testet
- Nødprosedyre: Stop All + tilbake til grunnpatch

## 5) Nødprosedyre (hvis noe går galt live)
1. Hold ro, hold tempo med fot eller metronom i øret.
2. Stop problemtrack (ikke stopp alt med en gang).
3. Kjør Undo hvis siste recording var feil.
4. Hvis fortsatt feil: bytt til "sikker" patch og fortsett.
5. Rebuild loop i neste musikalske vindu (4 eller 8 takter).

## 6) Hvordan bruke web-UI i dette repoet
- Bruk patch-knapper for raskt patch-skifte.
- Bruk transport-panel for Start/Stop/Rec/Undo/Redo.
- Bruk track-kort for Rec/Play/Stop/Clear per spor.
- Se MIDI-logg for å bekrefte hvilke kommandoer som sendes.

## 7) Neste nivå
- Koble til Web MIDI (`navigator.requestMIDIAccess`).
- Map eksakte CC/PC/SysEx mot ditt RC-600-oppsett.
- Lagre settlister og låtprofiler i localStorage.
- Legg til visuell feedback for active track/record state.
