# OpenQMD Documentation Bundle

This directory contains the consolidated documentation set for OpenQMD Phase II (October 2025).  
It integrates both internal technical insights and external-facing motor/generator applicability reports.

---

## Contents

| File | Purpose |
|------|----------|
| **OpenQMD_Internal_Memo.md** | Internal coordination summary covering DE2→DE4→QMD development, deliverable tracking, and testing status. |
| **QMD_Motor_Generator_Applicability.md** | External-ready documentation showing how QMD applies to motor/generator and turbine architectures. |

---

## Usage Notes
These documents are Markdown-native and directly viewable on GitHub.  
They serve as the reference documentation layer for all simulations under `/OpenQMD/simulations/`.

If editing locally:
```bash
cd OpenQMD/docs
code OpenQMD_Internal_Memo.md
code QMD_Motor_Generator_Applicability.md
```

Commit using:
```bash
git add .
git commit -m "Add DE2→DE4→QMD insight memo and motor/generator documentation"
git push origin main
```

---
