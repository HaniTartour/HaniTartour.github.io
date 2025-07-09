[![About Me](https://img.shields.io/badge/About-Hani%20Tartour-orange?style=for-the-badge&logo=readthedocs)](https://hanitartour.github.io/about.html)

# 📦 Clone From GitHub – User Guide
> Version 1.0 – Last Updated: July 2025  
> Author: [Hani M. Tartour](https://www.linkedin.com/in/hanimtartour)  
> Tool Category: pyRevit Extension Manager

---

## 🚀 Overview

**Clone From GitHub** is a pyRevit-powered utility that allows Revit users to seamlessly:

- Clone public GitHub repositories containing pyRevit extensions
- Automatically validate and register them
- Refresh the pyRevit ribbon to reflect new tools instantly  
Perfect for power users, BIM managers, and automation enthusiasts!

---

## 📂 Installation & Access

1. Ensure [pyRevit](https://github.com/eirannejad/pyRevit) is installed and running.
2. Locate the `CloneBuddy` panel inside your custom pyRevit ribbon.
3. Click on **"Clone From GitHub"** to launch the interface.

---

## 🧰 How It Works

1. **Paste** a GitHub repository URL (e.g., `https://github.com/HaniTartour/MyExtension`)
2. Click **"Clone"**  
   → The tool will:
   - Download the repo into a `CloneBuddyExtensions` folder
   - Validate structure (e.g., check for `.extension` suffix, `extension.json`)
   - Auto-fix missing or malformed metadata
3. Click **"Reload pyRevit"**  
   → Newly cloned tools will appear in your ribbon!

---

## 📎 Notes

- Only public repositories are supported (for now).
- Your extensions are organized inside:

- Uses the built-in `git` command-line tools.
- Requires internet access for cloning.

---

## 🧪 Troubleshooting

| Issue                        | Solution                                 |
|-----------------------------|------------------------------------------|
| ❌ Invalid repo URL          | Double-check the GitHub link             |
| 🚫 Missing extension.json    | Use the **"Fix Metadata"** button        |
| 🔄 Extension not showing     | Use the **"Reload pyRevit"** option      |
| 🧱 Cloned folder is empty    | Confirm the repo has content             |

---

## 📌 Roadmap (vNext)

- [ ] Support for private repos (token-based auth)
- [ ] Clone multiple repositories in batch
- [ ] Auto-update for previously cloned tools

---

## 🤝 Credits

Developed with 💙 by **Hani M. Tartour**  
Follow updates on [GitHub](https://github.com/HaniTartour)

