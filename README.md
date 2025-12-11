# StaticSecurityAnalysis
Static Security Analysis of Open Source Projects using Bandit

## Overview
Automated security analysis for Open Source Python codebases using Bandit. Scans code for common vulnerabilities and generates detailed reports in multiple formats.

## Installation

```bash
# Clone and navigate to the project
git clone https://github.com/priyadharshini18-hub/StaticSecurityAnalysis.git
cd StaticSecurityAnalysis

# Install dependencies
pip install -r requirements.txt
```

## Usage

### 1. Run Security Analysis

```bash
python scripts/run_bandit_analysis.py
```

Edit the script to specify your target repository path (line 57-58):
```python
run_bandit_scan("httpie/cli", "httpie")
```

**Generates:**
- `full_scan_*.json` - Complete JSON report
- `full_scan_*.html` - HTML report
- `full_scan_*.txt` - Text report
- `high_severity_*.txt` - High severity issues only

### 2. Filter Security Vulnerabilities

```bash
python filter_security_vulnerabilities.py
```

Update the input file path (line 91) to match your generated report timestamp.

**Output:** `security_vulnerabilities.json` with filtered results and severity breakdown.

## Example Output

```
▶ Running: Full JSON Report
  ✓ Completed

Filtered 15 security vulnerabilities from 45 total issues

Severity breakdown:
  HIGH: 8
  MEDIUM: 7
```

## Project Structure

```
├── scripts/run_bandit_analysis.py       # Main analysis script
├── filter_security_vulnerabilities.py   # Vulnerability filter
├── analysis_results/                    # Generated reports
└── httpie/                              # Sample repository
```

# 🛡️ StaticSecurityAnalysis
**Static Security Analysis of Open Source Projects using Bandit and Semgrep**

---

## 📘 Overview  
This project automates **static security analysis** for open-source Python repositories using two key tools:  

- **Bandit** – Detects common security issues in Python code such as hardcoded passwords, unsafe subprocess calls, and injection risks.  
- **Semgrep** – Performs rule-based static analysis across multiple languages to identify code quality issues, dependency risks, and configuration vulnerabilities in YAML, Docker, and CI/CD files.  

Together, these tools enable both **broad coverage** and **fine-grained rule-based scanning** for open-source projects.

---

## ⚙️ Installation  

```bash
# Clone and navigate to the project
git clone https://github.com/priyadharshini18-hub/StaticSecurityAnalysis.git
cd StaticSecurityAnalysis

# Install dependencies
pip install -r requirements.txt

