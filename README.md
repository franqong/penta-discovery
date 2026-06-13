<p align="center">
  <img src="assets/discovery.svg" width="200" alt="Discovery">
</p>

**Discovery** is a music exploration tool developed as a final project for the **Code in Place 2026** course (Stanford University). It is designed to help users discover new music, view lyrics, and get personalized recommendations within a clean, interactive, and fluid interface.

---

## 📌 Code in Place Context and Project Status

### Original Vision vs. Current Approach
The initial vision for **Discovery** was to connect the application directly to music streaming and lyrics APIs (such as **Deezer**) to play real songs in real-time. 

To keep the project aligned with the topics covered in the course and avoid complexities outside the scope of basic Python (such as advanced network authentication, multithreaded API consumption to prevent GUI freezes, and audio codec management), **the project's scope was redefined**:
* **A Dedicated Prototype:** This project serves as a focused **prototype**. While it currently operates with simulated features, the **original concept remains fully active** and stands as the roadmap for future development (integrating external streaming APIs and real audio playback).
* **Local Database (Mock):** Instead of connecting to the internet, the model uses a static, local database of representative songs (spanning genres like Grunge, Progressive Rock, and Nu Metal) structured using dictionaries and lists in `modelo.py`.
* **Simulated Playback:** No physical audio is played at this time. Instead, it simulates a 30-second preview playback using a non-blocking visual timer on the progress bar and a real-time spinning vinyl animation on the Canvas.
* **Full Feature Set:** Except for actual audio streaming, all other application features (searching, filtering by genre, smart recommendations, interactive navigation, and lyrics display) are **100% operational and functional**.

---

## 🚀 Core Features

* 🔍 **Search & Explore:** Find songs, artists, or albums within the local database using an intelligent search bar.
* 🏷️ **Genre Filters:** Quick shortcuts to filter music by selected genres.
* 📜 **Lyrics View:** Instantly access lyrics for loaded songs with an integrated scrollable text panel.
* 💡 **Smart Recommendations:** An algorithm that suggests 3 similar songs based on the genre of the currently selected track.
* 💿 **Interactive Player:** Playback simulation featuring Play/Pause controls, an interactive progress bar, and vinyl records that physically spin on screen when music is "playing".
* 🏗️ **MVC Architecture:** A clean, modular codebase separated into Model, View, and Controller patterns.

---

## 📂 Project Structure

* **`main.py`** ([main.py](./main.py)): The entry point of the application. It initializes the Tkinter root (`tk.Tk()`), the model, the view, and the controller, and starts the main event loop.
* **`modelo.py`** ([modelo.py](./modelo.py)): Contains the business logic, the local mockup song database, and the recommendation algorithm.
* **`vista.py`** ([vista.py](./vista.py)): Handles everything related to the graphical user interface using Tkinter and dynamic elements drawn on a `Canvas`.
* **`controlador.py`** ([controlador.py](./controlador.py)): Acts as a bridge between the view and the model. It listens for user events, queries data, and updates the screen.

---

## 🧠 C++ Influence and Advanced Python / GUI Concepts
The modular design of this project was heavily influenced by prior experience in **C++** development (such as static typing practices, object-oriented programming, and strict component separation). 

Consequently, the codebase implements several advanced concepts that extend beyond the introductory *Code in Place* syllabus. Below is an overview of these conceptual areas along with suggested documentation to explore their mechanics:

### 1. Object-Oriented Programming (OOP)
* **Where it is used:** In the definition of the main classes (`DiscoveryModel`, `DiscoveryView`, `DiscoveryController`), the `__init__` constructors, object instantiation, and referencing instance attributes/methods using the `self` keyword.
* **Concept:** Encapsulates data and behavior, preventing global state pollution and keeping the architecture clean. In comparison to C++, Python attributes are public by default, and the `this` pointer is explicitly represented by the `self` parameter.
* **📚 Documentation:** [Object-Oriented Programming in Python (Real Python)](https://realpython.com/python3-object-oriented-programming/) | [Classes in Python (Official Doc)](https://docs.python.org/3/tutorial/classes.html)

### 2. MVC Design Pattern (Model-View-Controller)
* **Where it is used:** The architectural layout of the project files.
* **Concept:** Decouples data logic (`modelo.py`), user interface (`vista.py`), and interaction logic (`controlador.py`), rendering the codebase highly modular and maintainable.
* **📚 Documentation:** [Tkinter MVC](https://www.pythontutorial.net/tkinter/tkinter-mvc/)

### 3. Event-Driven Programming and Callbacks
* **Where it is used:** Registering and passing methods as arguments in `set_callbacks` (`controlador.py`, line 18) to react to button clicks or keypresses.
* **Concept:** Functions in Python are first-class objects, meaning they can be passed as parameters to other functions to be executed at a later time (callbacks).
* **📚 Documentation:** [Event Binding in Tkinter](https://www.pythontutorial.net/tkinter/tkinter-event-binding/)

### 4. Lambda Expressions (Anonymous Functions)
* **Where it is used:** In `vista.py` (lines 92, 93, 114, 121, etc.) to define brief inline callbacks when binding mouse events on the canvas.
* **Concept:** Allows declaring quick, unnamed functions in a single line of code.
* **📚 Documentation:** [Lambda Functions in Python (Real Python)](https://realpython.com/python-lambda/)

### 5. Simulated Concurrency in GUI using `.after()`
* **Where it is used:** In `controlador.py` (`self.root.after(1000, self.run_timer)`) and `vista.py` (`self.root.after(50, self.animate_spin)`).
* **Concept:** The main loop of Tkinter (`mainloop`) is single-threaded. Calling `time.sleep()` freezes the entire user interface. The `.after()` method schedules a non-blocking callback to run in the future without halting the GUI.
* **📚 Documentation:** [Tkinter after() Method](https://www.pythontutorial.net/tkinter/tkinter-after/)

### 6. List Comprehensions
* **Where it is used:** In `modelo.py` (line 272) to filter songs by genre from the database in a single, highly readable line.
* **Concept:** A concise and optimized Python syntax for creating new lists based on existing iterables.
* **📚 Documentation:** [List Comprehension in Python (Real Python)](https://realpython.com/list-comprehension-python/)

### 7. Type Hinting
* **Where it is used:** In `controlador.py` (line 6): `def __init__(self, model: DiscoveryModel, view: DiscoveryView, root: tk.Tk):`.
* **Concept:** Annotations that document the expected object types for arguments and variables. This practice was carried over from C++ static typing habits, aiding in error detection during development.
* **📚 Documentation:** [Python Type Checking (Real Python)](https://realpython.com/python-type-checking/)

### 8. Trigonometry on Canvas (The `math` Module)
* **Where it is used:** In `vista.py` (lines 327-333) to animate the spinning line of the vinyl records using `math.cos`, `math.sin`, and `math.pi`.
* **Concept:** Converts polar coordinates (rotation angle and radius) to cartesian coordinates (X, Y) to render rotating lines on the canvas.
* **📚 Documentation:** [Python math Module (Official Doc)](https://docs.python.org/3/library/math.html)

---

## 🎨 Design & Resources
* **Color Palette:** [Color Hunt #222831](https://colorhunt.co/palette/222831393e46948979dfd0b8) (Dark slate, grey, and cream theme).
* **Tkinter Colors:** [Valid GUI Colors List](https://inventwithpython.com/blog/complete-list-tkinter-colors-valid-and-tested.html) (Valid color names and codes).
* **Logo Design:** [Inkscape Vector Editor](https://inkscape.app/) (Used to design `assets/discovery.svg`).

---

## 🛠️ How to Run

1. Ensure Python 3.x is installed on your system.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Run the entry point file:
   ```bash
   python main.py
   ```

---

*A Code in Place final project. Looking forward to building more on this foundation.*