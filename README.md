# LLM-Assisted Qualitative Analysis of Educator–AI Conversations

This repository contains code and example data for conducting LLM-assisted qualitative annotation, codebook-aligned postprocessing, and figure generation for large-scale educator–AI conversation analysis.
The workflow supports reproducible mixed-methods research combining human-defined codebooks with LLM-supported annotation at scale.

├── usage_analysis_using_LLM.ipynb<br>
├── JEDM_figures.ipynb<br>
├── system_prompt.py<br>
├── input/<br>
├── ├── qual_map.csv<br>
├── ├── sample.csv<br>
├── ├── invalid_code.csv<br>
├── output/<br>
├── ├── figures/<br>
├── src/<br>
├── ├── connect_anthropic.py<br>
├── ├── connect_openai.py<br>
├── ├── connect_psql.py<br>
├── ├── normalize_nested_json_with_prefix.py<br>
├── .envexample<br>
├── requirements.txt<br>
└── README.md<br>

## Notebooks Overview

### 1. `usage_analysis_using_LLM.ipynb`

This notebook demonstrates the full pipeline for **LLM-assisted qualitative coding**, including:

- Prompt-based annotation of educator–AI messages using large language models  
- Structured extraction of instructional domains, practices, and professional intents  
- Postprocessing and normalization of LLM outputs  
- Mapping model-generated labels back to a human-defined codebook  
- Exporting results for downstream analysis and visualization  

The notebook is designed to scale from sample data to large datasets of real-world educator–AI conversations.

---

### 2. `JEDM_figures.ipynb`

This notebook generates the **descriptive and analytic figures** used in the findings section of the paper, including:

- Domain-level and category-level frequency distributions  
- Educator request vs. AI response comparisons  
- Co-occurrence heatmaps of instructional categories  
- Coverage visualizations aligned with professional teaching frameworks  

All generated figures are saved to the `output/` directory.

---

## Input Data

The `input/` folder includes example files to allow users to run the pipeline end-to-end:

- **`qual_map.csv`**  
  The finalized qualitative codebook used for deductive annotation. This file defines the valid instructional domains, categories, and action items.

- **`sample.csv`**  
  A small, de-identified sample of educator–AI conversations for testing the annotation workflow.

- **`invalid_code.csv`**  
  An example file showing LLM-generated labels that do not exactly match the codebook (e.g., variations such as `"special ed"`, `"sped"`, `"iep"`).  
  This file demonstrates how invalid or noisy outputs are manually reviewed and mapped back to standardized codebook labels during postprocessing.

---

## Output

All generated figures and intermediate outputs are written to the `output/` directory.

- `output/figures/` contains publication-ready visualizations produced by `JEDM_figures.ipynb`.

---

## Environment Setup

### 1. Create your environment file

Copy the example environment file:

```bash
cp .envexample .env
```
These keys are required to run `usage_analysis_using_LLM.ipynb`.

**Do not commit `.env` to version control.**

---

## Getting Started

1. Install required Python dependencies (recommended via a virtual environment).
2. Configure API keys using `.env`.
3. Run `usage_analysis_using_LLM.ipynb` to:
   - Annotate sample educator–AI conversations  
   - Normalize outputs to the codebook  
4. Run `JEDM_figures.ipynb` to reproduce all figures.
