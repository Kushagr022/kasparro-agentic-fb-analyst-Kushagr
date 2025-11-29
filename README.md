# 🚀 Kasparro Agentic Facebook Analyst

## 🏢 Enterprise-Grade Multi-Agent System for Autonomous Facebook Ads Performance Analysis

A sophisticated, self-directed agentic system that revolutionizes digital marketing analytics by autonomously diagnosing Facebook Ads performance, identifying ROAS fluctuations, and generating data-driven creative recommendations using advanced AI agents.

---

## 🌟 Key Innovations

### 🤖 Intelligent Multi-Agent Architecture  
This system implements a cutting-edge multi-agent architecture where five specialized AI agents collaborate seamlessly to perform complex marketing analytics tasks that traditionally require human experts.

### 📊 Advanced Performance Diagnostics  
Beyond basic analytics, our system diagnoses the root causes behind ROAS changes, identifying subtle patterns like:

- Audience fatigue  
- Creative burnout  
- Seasonal fluctuations  
- Demographic shifts  
- Competitive impacts  

### 🎨 AI-Powered Creative Intelligence  
The system doesn't just identify problems — it generates actionable creative solutions by analyzing existing high-performing content and suggesting data-driven improvements.

---

## 🏗️ System Architecture Deep Dive

### 🔥 Agent Specialization & Workflow

| Agent | Role | Core Capabilities | Output |
|-------|------|-------------------|--------|
| **Planner Agent** 🎯 | Strategic Orchestrator | Query decomposition, task planning | Structured task list |
| **Data Agent** 📊 | Data Intelligence Engine | Data loading, validation, summaries | Data report |
| **Insight Agent** 💡 | Pattern Recognition Expert | Hypothesis generation, anomaly detection | Insights |
| **Evaluator Agent** ✅ | Validation & Assurance | Confidence scoring, statistical checks | Validated insights |
| **Creative Agent** 🎨 | Creative Intelligence System | Content analysis, idea generation | Creatives.json |

---

## 🔄 Data Flow Pipeline

```
User Query
   ↓
Planner Agent
   ↓
Data Agent
   ↓
Insight Agent
   ↓
Evaluator Agent
   ↓
Creative Agent
   ↓
Outputs → insights.json, creatives.json, report.md, logs/
```

---

## 🔬 Technical Implementation

### 🛠️ Core Technologies
- Python 3.7+
- pandas for data analysis
- JSON for structured output
- Modular multi-agent architecture

### 📈 Analytics Capabilities
- ROAS trend analysis  
- CTR correlation studies  
- Audience segmentation  
- Creative performance benchmarking  
- Time-series fluctuations detection  

### 🎯 Feature Set Summary

#### Performance Diagnostics
- Automatic root-cause analysis  
- Campaign-level benchmarking  
- Audience fatigue detection  
- Confidence-based scoring  

#### Creative Intelligence
- Pattern-based ad messaging  
- Audience-specific suggestions  
- CTA + headline + script generation  
- Data-driven creative refresh cues  

---

## 📁 Project Structure

```
kasparro-agentic-fb-analyst/
├── run.py
├── data/
│   └── synthetic_fb_ads_undergarments_sample.csv
├── agent_graph.md
│
├── src/
│   ├── run.py
│   ├── agents/
│   ├── planner_agent.py
│   ├── data_agent.py
│   ├── insight_agent.py
│   ├── evaluator_agent.py
│   └── creative_agent.py
├── outputs/
│   ├── insights.json
│   ├── creatives.json
│   └── report.md
│
├── config/
│   └── config.yaml
│
├── requirements.txt
```

---

## 🚀 Quick Start Guide

### 1️⃣ Environment Setup

```bash
git clone <repo-url>
cd kasparro-agentic-fb-analyst
pip install -r requirements.txt
```

### 2️⃣ Run the System

```bash
python src/run.py "Analyze ROAS drop" --data-path "synthetic_fb_ads_undergarments_sample.csv" --sample
```

### 3️⃣ View Results

✔ **outputs/insights.json** — Validated performance insights  
✔ **outputs/creatives.json** — AI-generated creatives  
✔ **outputs/report.md** — Executive summary  
✔ **logs/** — Audit trail  
