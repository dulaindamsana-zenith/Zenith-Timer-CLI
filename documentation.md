# Zenith Timer - User Manual

Welcome to **Zenith Timer**, created by Dulain Damsana! This documentation explains how to navigate and operate the command-line interface (CLI) for Zenith Timer.

---

## 🚀 Getting Started

When you launch Zenith Timer, you will see a banner welcoming you to the application followed by a menu listing all available options:

```text
 _____________________
| + --------------- + |
|     Our Options     |
| + --------------- + |
| =================== |
| > Current Time      |
| > Timer             |
| > Docs              |
| > Exit              |
|_____________________|
```

To run a command, type your choice at the `[?] Enter a option:` prompt and press **Enter**.

---

## 📋 Available Commands

### 1. `Current Time`
Displays a static snapshot of the current local date and time formatted as `YYYY--MM--DD = HH:MM:SS`.

* **How to trigger:** Type any of the following:
  * `current time`
  * `current_time`
  * `current-time`
* **Behavior:** Outputs the current date and time once and then returns to the main options menu.

---

### 2. `Timer`
Starts a continuous live-updating clock on your terminal screen displaying the full breakdown of time (Year, Month, Day, Hour, Minute, and Seconds).

* **How to trigger:** Type `timer`.
* **Behavior:** Updates every second in real time on the same line.
* **How to Stop:** Press `Ctrl + C` on your keyboard. This stops the timer and safely returns you to the main menu.

---

### 3. `Docs`
Displays a notification reminding you to view this documentation file (`documentation.md`).

* **How to trigger:** Type any of the following:
  * `docs`
  * `doc`
  * `documentation`

---

### 4. `Exit`
Safely quits the Zenith Timer program.

* **How to trigger:** Type any of the following:
  * `exit`
  * `close`
  * `quit`

---

## ❓ Input Handling & Errors

* **Case Sensitivity:** Inputs are **case-insensitive** (e.g., typing `TIMER`, `Timer`, or `timer` will all work).
* **Unknown Inputs:** If you type an unrecognized command, Zenith Timer will display an error message (`> ERROR: Option not found`) and reprint the options menu for you.