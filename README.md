# 🍳 KitchenSync: Hardware-Assisted KPT Signal Enrichment

**A submission for the Zomathon Hackathon (Problem Statement 1)** **Team:** [Your Team Name] | **University:** Siksha 'O' Anusandhan (SOA) University

---

## 📖 Overview
[cite_start]Accurate Kitchen Prep Time (KPT) prediction is critical for optimizing rider assignments and setting reliable customer ETAs[cite: 53, 57]. [cite_start]Currently, KPT models rely heavily on merchant-marked "Food Ready" (FOR) signals, which suffer from operational bias and lack visibility into offline "kitchen-wide rush" (dine-in/competitor orders)[cite: 60, 63]. 

[cite_start]**KitchenSync** is a dual-component system designed to enrich input signals and provide an objective view of the true kitchen load using AI-first hardware-assisted instrumentation[cite: 66, 70, 89]. 

---

## 🚀 The Solution: Dual-Signal Architecture

We propose a shift from purely manual, biased inputs to a hybrid model:

### 1. "The Eye" (Hardware-Assisted AI Rush Detection)
[cite_start]To capture kitchen rush beyond Zomato-only orders, we built a lightweight Computer Vision (CV) pipeline using OpenCV. 
* **How it works:** A basic camera points at the kitchen's physical order ticket rail. The CV model continuously counts the physical receipts. 
* **The Value:** It translates offline physical load into an objective digital signal, completely bypassing human bias.

### 2. "The Pulse" (Frictionless Merchant UI)
[cite_start]To de-noise the current FOR signals[cite: 84], we designed a frictionless 3-state input system (Swamped 🔴, Steady 🟡, Quiet 🟢) that requires zero app navigation, allowing chefs to instantly update the KPT baseline during peak hours.

---

## 📈 Impact on Success Metrics
[cite_start]This system directly addresses Zomato's core success metrics[cite: 74]:
* [cite_start]**Average Rider Wait Time & Idle Time:** Decreases significantly by delaying rider dispatch until "The Eye" confirms the physical ticket queue is moving[cite: 75, 78].
* [cite_start]**ETA Prediction Error (P50/P90):** Improves by feeding the existing KPT models cleaner, unbiased ground-truth data[cite: 76].
* [cite_start]**Order Delay and Cancellation Rates:** Dynamic checkout ETAs based on true kitchen load manage customer expectations better, reducing cancellations[cite: 77].

---

## 🛠️ Tech Stack
* **Python 3.x:** Core backend logic.
* **OpenCV (`cv2`):** Real-time image processing and contour detection for the ticket-counting simulation.
* **NumPy:** Array operations for image thresholding.

---

## ⚙️ How to Run the Simulation ("The Eye")
This repository contains the prototype for the AI-first ticket counting module.

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YourUsername/KitchenSync-Zomathon.git](https://github.com/YourUsername/KitchenSync-Zomathon.git)
   cd KitchenSync-Zomathon
