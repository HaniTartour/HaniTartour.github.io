[![About Me](https://img.shields.io/badge/About-Hani%20Tartour-orange?style=for-the-badge&logo=readthedocs)](https://hanitartour.github.io/about.html)

# 🛠️ Shaft Opening Converter – Instructions Guide

This guide covers how to use the **Shaft Opening Converter** Dynamo scripts to visualize and compare shaft openings from host and linked Revit models.

---

## 📌 What This Tool Does

These Dynamo scripts generate **DirectShape geometry** from *Shaft Opening* elements in both:
- The **host Revit model** (e.g. Structural model)
- A **linked Revit model** (e.g. Architecture model)

This makes the shafts visible and realistic inside the 3D environment, in Revit and downstream platforms like **Navisworks**, even if they were not modeled with solids.

---

## 🧰 Included Files

- `Host-shaft to solid.dyn`  
  → Converts shaft openings in the current model into solid **DirectShapes**.

- `LinkedModel-shaft to solid.dyn`  
  → Converts shaft openings in a *linked* model into solid **DirectShapes** in the host model.

---

## 🔧 Requirements

- Revit 2022 or later  
- Dynamo 2.x  
- Model with shaft openings  
- Optional: Linked architectural model

---

## 🧭 How To Use

### 🔹 For Host Shaft Openings
1. Open the host model (e.g., structural).
2. Launch Dynamo inside Revit.
3. Open `Host-shaft to solid.dyn`.
4. Run the script.
5. You’ll see solids generated in place of shaft openings.

### 🔹 For Linked Model Shaft Openings
1. Ensure your architectural model is linked.
2. Launch Dynamo in the host model.
3. Open `LinkedModel-shaft to solid.dyn`.
4. Pick the link instance when prompted.
5. The script will extract shaft locations from the link and create solids in your current model.

---

## 💡 Why This Tool Is Useful

- Visual comparison between architectural vs structural shafts.
- Enables **clash detection** in Navisworks (solids are exported in NWC).
- Adds clarity for coordination meetings and drawing outputs.

---

## 📸 Demo / Screenshots

Coming soon...

---

## 🔁 Tips

- Use color-coded DirectShapes to easily differentiate host vs link shafts.
- Use **section boxes** in Revit to isolate shaft solids for QA/QC.

---

Built with 💙 by Hani Tartour
