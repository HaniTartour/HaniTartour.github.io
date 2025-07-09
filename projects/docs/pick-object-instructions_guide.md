[![About Me](https://img.shields.io/badge/About-Hani%20Tartour-orange?style=for-the-badge&logo=readthedocs)](https://hanitartour.github.io/about.html)

# 🛠️ Pick One Object – Instructions Guide

**Tool Name:** Pick One Object  
**Version:** 1.0.0  
**Author:** Hani M. Tartour  
**Platform:** pyRevit + Revit API  
**Last Updated:** July 2025

---

## 🔍 Purpose
Quickly select a Revit element in your model and view its details in a clean, BIMBuddy-styled Windows Form.

---

## 🚀 How to Use

1. Click the `Pick One Object` button under the **Baby Tools** panel.
2. Select any object in your Revit model.
3. A Windows Form will open showing:
   - **Element ID**
   - **Name**
   - **Category**
   - **Level (if available)**

---

## 📌 Notes

- Elements without a `Level` parameter will show `N/A`.
- Works with most element types: walls, beams, doors, annotations, etc.
- Future update will include **copy to clipboard** and **export to JSON**.

---

## 📁 File Location
HT.extension/
└── BabyTools.panel/
└── PickObject.pushbutton/
└── script.py


---

## 📸 Preview

![Pick Form Screenshot](../images/pick-object-demo.png)

---

## 👨‍💻 Powered by

- Python (IronPython)
- Revit API
- pyRevit
- BIMBuddy UI Framework

---
