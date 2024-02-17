# Causality in Geospatial Modeling

This repository is inspired by LLM-Geo, an AI-powered geospatial analysis autonomous GIS agent for spatial analysis.

# Installation

Clone or download the repository, rename `your_config.ini` as `config.ini`. Then put your OpenAI API key in the `config.ini` file. Please use GPT-4, the lower versions such as 3.5 do no have enough reasoning ability to generate correct solution graph and operation code.

# How to use
This tool is used to get a causal graph for a phenomenon of several. Please input the phenomenon in the Jupyter notebook. If you do not like to use OpenAI API, you can also copy the generate prompt to ChatGPT to get the code for graph.

# Limitation
- The causal graph is based on commonsense, not very detailed.
- My previous idea is to use a question, e.g, "How a higher education attainment affect income level", rather than some terms. Only use terms for phenomena seems not a good idea after my implementation. Will modify the code for question input which can contains more context.