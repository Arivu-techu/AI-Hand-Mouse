# AI-Hand-Mouse
A high-precision AI Virtual Mouse using Python, OpenCV, and MediaPipe. Features 21-point skeletal hand tracking, jitter-free cursor smoothing (Linear Interpolation), and intuitive gesture-based clicking.
# 🚀 Features
- **21-Point Skeletal Tracking:** High-fidelity hand landmark detection.
- **Smoothing Algorithm:** Uses Linear Interpolation (Lerp) to eliminate cursor jitter.
- **Natural Gestures:** Euclidean distance logic for "Pinch-to-Click" experience.

# 🛠️ Setup & Usage
1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
2. **Run the Application:**
   `python VM.py`
   ---

## 🎨 UI/UX Design & Human-Computer Interaction (HCI)
I developed this system with a focus on **Feedback Loops** and **Spatial Ergonomics** to ensure a natural user experience.

### 1. Visual Feedback & State Awareness
- **Dynamic HUD:** Implemented a real-time Heads-Up Display that changes colors (Blue for Nav, Green for Scroll) to provide instant visual affordance of the system state.
- **Confirmation Cues:** The 21-point skeletal overlay serves as a constant feedback loop, confirming the AI's detection accuracy and reducing user "input anxiety".

### 2. Interaction Design & Ergonomics
- **The "Active Zone" Solution:** Designed an inner-frame boundary (Frame Reduction) so users can reach all screen corners with 40% less physical hand movement, preventing "gorilla arm" fatigue.
- **Micro-interaction Smoothing:** Applied **Linear Interpolation (Lerp)** to the cursor logic to remove the jitter common in raw CV tracking, creating a premium, stable feel for the end-user.

---
# 🖱️ AI Virtual Mouse: Modal Interaction Pro

https://github.com/user-attachments/assets/45b813c7-e02c-4ea5-92dc-2792acfe9ace
### 🖥️ Real-time Execution
The system provides a live HUD (Heads-Up Display) to inform the user of the active mode and tracking status.

![Real-time Execution](https://github.com/user-attachments/assets/a8bba613-f158-47b5-9642-161bc6127811)

## 🔬 The 2026 Innovation: Modal Interaction Logic
Unlike legacy virtual mice that rely on simple coordinate mapping, this system introduces **Context-Aware States**. It intelligently switches behavior based on hand geometry.

### 🎮 Interaction Modes:
- **🔵 Navigation Mode (Blue):** High-precision cursor control with **Lerp Smoothing** to eliminate jitter.
- **🟢 Scroll Mode (Green):** Triggered by index-middle finger proximity. Maps hand height (Y-axis) directly to system scroll speed.

## 🛠️ Technical Improvements
| Feature | Legacy AI Mice (Old) | My Innovation (v2.1) |
| :--- | :--- | :--- |
| **Logic** | Always active (Accidental clicks) | **Modal Switching** (Nav vs. Scroll) |
| **Movement** | Raw coordinates (Jittery) | **Adaptive Interpolation Mapping** |
| **Function** | Cursor only | **Dynamic Vertical Scrolling** |

| Feature | Legacy AI Mice (Old) | My Innovation (v2.1) |
| :--- | :--- | :--- |
| **Logic** | Always active (Accidental clicks) | **Modal Switching** (Nav vs. Scroll) |
| **Movement** | Raw coordinates (Jittery) | **Lerp Smoothing** + Adaptive Mapping |
