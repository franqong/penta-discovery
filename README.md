<p align="center">
  <img src="assets/discovery.svg" width="200" alt="Discovery">
</p>

Discovery is a music exploration tool developed as a final project for the **Code in Place 2026** course (Stanford University). It is designed to help users discover new music, view lyrics, and get recommendations in a clean, interactive interface.

## What is Discovery?

Discovery is a focused prototype aimed at simplifying the way we find and experience music. Built entirely in Python, it serves as a proof of concept for features that will eventually be integrated into [**Penta**](https://github.com/franqong/penta), a broader social platform for music enthusiasts. The project emphasizes modular architecture, ensuring that its core logic can be seamlessly reused in future developments.

## Core Features

*   **Search & Explore:** Search for songs and artists using real-time API data.
*   **Lyrics View:** Instantly access lyrics for discovered tracks.
*   **Smart Recommendations:** Get suggestions for similar music based on your current search.
*   **Audio Previews:** Listen to 30-second previews to get a feel for the music.
*   **MVC Architecture:** A clean, modular codebase separated into Model, View, and Controller.

## Reusability & Penta

One of the key goals of Discovery is the reusability of its **Model**. The logic developed here for API communication and recommendation algorithms is designed to function as a standalone module, which will later be ported to the Penta ecosystem as part of its backend infrastructure.

## Project Structure

*   `main.py`: Entry point that initializes the application.
*   `modelo.py`: Data logic, API calls, and recommendation algorithms.
*   `vista.py`: Graphical user interface built with `tkinter`.
*   `controlador.py`: Event handling and communication between model and view.

## Technology Stack

*   **Language:** [Python](https://www.python.org/)
*   **GUI Library:** [Tkinter](https://docs.python.org/3/library/tkinter.html)
*   **APIs:** Integrations for music data and lyrics (e.g., Deezer API).

---

A Code in Place final project. Looking forward to building more on this foundation.