# 📦 Sort Packages

A simple robotic automation function for classifying packages into the correct stack based on **volume and mass**.

---

## 🚀 Rules
- A package is **bulky** if:
  - Volume ≥ 1,000,000 cm³ **OR**
  - Any dimension ≥ 150 cm
- A package is **heavy** if:
  - Mass ≥ 20 kg

### Dispatch Stacks
- **STANDARD** → neither bulky nor heavy
- **SPECIAL** → either bulky OR heavy
- **REJECTED** → both bulky AND heavy

---

## 🛠️ Usage
```bash
python sort_package.py
