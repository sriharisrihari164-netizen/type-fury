# Project Architecture — Type Fury Engine

This document provides a technical overview of how the **Type Fury** game engine functions, manages state, and handles rendering.

## 1. Modular Engine Structure
The game is encapsulated in a self-executing anonymous function to prevent global scope pollution. It uses a monolithic `game.js` for simplicity and performance in a static-hosted environment.

### Core Modules:
- **SoundFX**: A procedural audio engine built on the Web Audio API. It generates tones, noises (explosions), and basic rhythm patterns without external audio files.
- **State Management**: Independent objects (`racingState`, `neonState`, `galaxyState`) handle logic for each mode.
- **Game Loops**: Uses `requestAnimationFrame` with a Δt (delta time) calculation to ensure physics and animations remain consistent regardless of the user's refresh rate.

---

## 2. State Management
Each game mode is governed by a state object that tracks variables like WPM, level, active words, and particles.

### Example: `racingState`
```javascript
const racingState = {
    active: false,
    level: 1,
    cars: [...],     // Objects tracking AI & Player position
    images: {},      // Preloaded Image elements
    wpm: 0,
    accuracy: 100,
    finished: false
};
```

---

## 3. The Sound Engine (`SoundFX`)
The procedural sound system avoids the latency and bandwidth costs of large MP3 samples.
- **Oscillators**: Uses `sine`, `square`, and `sawtooth` oscillators for UI clicks and game alerts.
- **Gain Nodes**: Manages master volume, music volume, and specific event volumes (e.g., explosions).
- **Rhythm Generation**: Uses `setInterval` tied to the Web Audio clock for rhythmic background pulsing.

---

## 4. Visual Rendering
Visuals are delivered via the HTML5 Canvas API for high-frequency updates.
- **Layered Backgrounds**: Use CSS `background-image` for static layers and canvas for dynamic particles/sprites.
- **Sprite Preloading**: functional images (cars, ships) are pre-initialized as `new Image()` and cached in the respective state's `images` object.
- **Particle Systems**: Every game mode manages a `particles` array, performing per-frame updates for position, opacity, and life-span.

---

## 5. Persistence
Player progress is handled via the `localStorage` API:
- `typefury_racing_level`: Current stage in the racing campaign.
- `typefury_neon_highscore`: Peak score in the Neon Leak mode.
- `typefury_neon_words`: A set of "ever used" words to ensure the player is constantly challenged with new vocabulary.

---

## 6. Deployment Logic
The project is configured for **GitHub Pages**. The `.github/workflows/deploy.yml` automates:
1. Validating the main branch.
2. Uploading the flat file structure as a deployment artifact.
3. Hosting the site with proper CNAME and HTTPS support.
