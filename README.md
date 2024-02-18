# Causality in Geospatial Modeling

This repository is inspired by LLM-Geo, an AI-powered geospatial analysis autonomous GIS agent for spatial analysis.

# Installation

Clone or download the repository, rename `your_config.ini` as `config.ini`. Then put your OpenAI API key in the `config.ini` file. We also test OpenAI GPT-4 API so for. Lower version may be not capable to generate correct results.

# How to use
This tool is used to get a causal graph for a research question. Please input the research question in the Jupyter notebook (`causal_graph.ipynb`). If you do not like to use OpenAI API, you can also copy the generate prompt to ChatGPT to get the code for graph.

# Limitation
- The causal graph is based on commonsense, not very detailed and accurate.

# To do list
- Add a review module
- Generate hierarchical casual graph
