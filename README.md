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
# 🖱️ AI Virtual Mouse: Modal Interaction Pro

https://github.com/user-attachments/assets/45b813c7-e02c-4ea5-92dc-2792acfe9ace

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

