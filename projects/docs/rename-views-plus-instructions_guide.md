[![About Me](https://img.shields.io/badge/About-Hani%20Tartour-orange?style=for-the-badge&logo=readthedocs)](https://hanitartour.github.io/about.html)

# 📘 Rename Views+ — pyRevit Tool Documentation
**Author:** Hani M Tartour  
**Tool Version:** v1.0.0  
**Last Updated:** July 2025  

---

## 1. 📌 Tool Overview
**Rename Views+** is a productivity-focused pyRevit plugin designed to batch rename Revit views intelligently. With a live grid preview, category filters, find/replace options, and Excel integration, it enables clean, fast, and organized naming across entire models — in seconds.

---

## 2. 🚀 Key Features
- 🔁 Live preview of renamed views with color-coded indicators  
- 🔍 Filter views by discipline, view type, duplication, or keyword  
- 📤 Export/Import naming schema via Excel (CSV format)  
- 🔠 Find & Replace logic  
- 🖌 Add prefix/suffix to selected views  
- 🎨 Custom Windows Form UI (styled with BIMBuddy design)  
- 🧠 Designed for large-scale Revit models and automation workflows  

---

## 3. 🔧 Installation Steps
1. Make sure **pyRevit** is installed and configured for Revit.  
2. Clone or download the `HT-Toolbox` extension from GitHub:  
   ```bash
   https://github.com/HaniTartour/HT-Toolbox
   ```  
3. Place the extension folder under your pyRevit extensions directory:  
   ```
   %APPDATA%\pyRevit\Extensions\
   ```
4. Restart Revit or run `pyrevit reload`  
5. You’ll find **Rename Views+** under the `HT Toolbox` tab.

---

## 4. 📸 User Interface Preview
Screenshots available inside the project’s `/projects/rename-views.html` page:  
- Main tool window  
- Select views dialog  
- Rename options panel  
- Final result preview  

---

## 5. 🧰 How It Works
### ① View Collector
Collects all views (floor plans, elevations, sections, etc.) excluding templates, schedules, and system views.

### ② Filter Engine
Lets you filter by:
- View type (e.g., Floor Plan, Elevation)
- Discipline
- Name contains / doesn’t contain
- Duplicate view patterns

### ③ Rename Engine
Applies:
- Prefix
- Suffix
- Find & Replace (case-insensitive, optional full match)
- Live validation to avoid conflicts  

### ④ Preview Grid
Color-coded DataGridView:
- ✅ Green: Clean rename  
- 🟡 Yellow: Duplicate or warning  
- 🔴 Red: Conflict with existing view  

### ⑤ Apply Changes
Bulk applies all rename actions to the selected views.

---

## 6. 📄 Excel Integration
**Export Template**  
- Use the `Export to Excel` button  
- Output: `.csv` with columns:  
  ```
  Original Name | New Name | View Type | Discipline
  ```

**Import for Batch Rename**  
- Prepare a CSV following the export format  
- Use `Import from Excel` and validate before applying

---

## 7. 🧪 Use Cases
- Renaming construction documentation views for submission  
- Preparing a template set with consistent naming standards  
- Reorganizing views from consultants into a unified format  
- Filtering and renaming only duplicated or temp views  

---

## 8. ⚙️ Settings Explained
| Setting         | Description                                         | Example                  |
|------------------|-----------------------------------------------------|---------------------------|
| Prefix           | Add text to the beginning of view names             | `ARC-`                    |
| Suffix           | Add text to the end of view names                   | `-REV1`                   |
| Find             | Find this text inside view names                    | `TEMP`                    |
| Replace With     | Replace found text with this value                  | `R1`                      |
| Filter Keyword   | Filter views containing certain word                | `Section`                 |

---

## 9. 🧼 Best Practices
- Always run with **filters** enabled to limit renaming scope.  
- Export a backup CSV before applying changes.  
- Avoid renaming linked model views.  
- Double-check for **duplicate names** in the preview grid.

---

## 10. ⚠️ Warnings & Edge Cases
- Certain views (like Area Plans or Legend Views) may be restricted by Revit API.  
- Read-only views or template-based views will be skipped automatically.  
- Revit may not allow duplicate view names — the grid will highlight these in **red**.

---

## 11. 💡 Tips & Tricks
- Use **Ctrl+Click** or **Shift+Click** to multi-select in preview grid.  
- Combine **Prefix** + **Find/Replace** for maximum flexibility.  
- Use the **keyword filter** to isolate a specific building block/floor quickly.  
- Rename duplicated views (e.g. `Floor Plan (1)`) with the **Replace (1)** logic.

---

## 12. 🔄 Future Roadmap
- ✅ Integrated duplicate name resolver  
- 🧩 Save/load renaming schemes  
- ⏳ Progress bar during renaming large view sets  
- 🔧 Parameter-based renaming (e.g. based on Level or Scope Box)

---

## 13. 👨‍💻 Developer Notes
- Built with:  
  - IronPython + Revit API  
  - Windows Forms (System.Windows.Forms)  
  - Embedded inside `HT-Toolbox` pyRevit extension  
- Organized into:  
  - `rename_views_form.py` (UI Logic)  
  - `rename_views_core.py` (Collector/Renamer)  
  - `excel_handler.py` (Optional)  

---

## 14. 📚 Resources
- [pyRevit Documentation](https://www.notion.so/pyRevit-Docs)  
- [Revit API Docs](https://www.revitapidocs.com/)  
- [Hani’s GitHub – Rename Views+ Repo](https://github.com/HaniTartour/HT-Toolbox)  
- [Download User Guide (PDF)](../assets/docs/rename-views-instructions.pdf)

---

## 15. 🏁 Conclusion
Rename Views+ is not just a utility — it's a **time-saver**, **QA enforcer**, and **productivity booster** for Revit professionals. Whether you're tidying views for publishing, organizing a chaotic model, or just hate repetitive clicking — this tool is your friend.

---

### ✨ Made with 💙 by Hani M Tartour
_Stay tuned for updates on [GitHub](https://github.com/HaniTartour)!_