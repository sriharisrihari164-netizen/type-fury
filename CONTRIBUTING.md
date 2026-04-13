# Contributing to Type Fury

We welcome contributions to **Type Fury**! Whether you're adding new game modes, fixing bugs, or expanding our vocabulary, here's how to get started.

## 📝 Modifying Word Lists

The game uses several word pools defined in the `game.js` constant `COMMON_WORDS` and mode-specific pools inside the game loops.

### Adding New Words
To expand the general pool, add strings to the `COMMON_WORDS` array (starting around line 100).
- **Format**: All lowercase strings.
- **Example**:
  ```javascript
  const COMMON_WORDS = [
      "syntax", "matrix", "cybernetic", ...
  ];
  ```

---

## 🎨 Design Guidelines

Type Fury adheres to a strict "Neon Cyberpunk" design system.
- **Colors**: Use HSL and opacity for glow effects (e.g., `hsla(190, 100%, 50%, 0.8)`).
- **Typography**: The primary fonts are `Orbitron` and `Share Tech Mono`.
- **Transitions**: Use CSS `transition: all 0.3s cubic-bezier(0.19, 1, 0.22, 1);` for premium-feeling interactions.

---

## 🛠 Adding a New Game Mode

If you wish to add a new game mode:
1. **HTML**: Create a new `.screen` div in `index.html`.
2. **CSS**: Add a new `.bg-layer` and mode-specific HUD styles in `style.css`.
3. **JS**:
   - Define a `state` object for the mode.
   - Create a `start[ModeName]` function to initialize the screen.
   - Add a loop function called via `requestAnimationFrame`.
   - register the mode in the `mainMenu` event listeners.

---

## 🚀 Submitting Changes

1. **Fork** the repository.
2. **Create a branch** for your feature (`git checkout -b feat/new-rhythm-mode`).
3. **Test** locally to ensure no performance regressions.
4. **Push** your changes and open a **Pull Request**.

### Testing Checklist
- [ ] No 404 image errors in the console.
- [ ] Sound FX trigger correctly for your new module.
- [ ] High scores are persisted after a page refresh.
