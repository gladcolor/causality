

#--------------- constants for graph generation  ---------------
graph_role = r'''A professional professor in both natural and socie science, and very good at Python programming. Your interest is to investigate the various phenomeno in an explainable way. You research the causal learning and Bayesian network more than 30 years, and know every detail and latest progress in this field. You have significant experenced on graph theory, application, and implementation. You are also experienced on critial variables in the causal graph.
'''

graph_task_prefix = r'Generate a graph (data structure) only, whose nodes are a series of consecutive entities cause the given phenomena or entities, which is (are): '

graph_reply_exmaple = r"""
```python
import networkx as nx
G = nx.DiGraph()
# Add nodes
nodes = [
    "Heavy Rainfall",
    "Snowmelt",
    "Coastal Storm Surge",
    "Dam or Levee Failure",
    "River Overflow",
    "Urban Drainage Basins",
    "Land Use Changes",
    "Soil Saturation",
    "Urban Flooding"
]

G.add_nodes_from(nodes)

# Add edges to represent causal relationships
edges = [
    ("Heavy Rainfall", "River Overflow"),
    ("Snowmelt", "River Overflow"),
    ("Coastal Storm Surge", "Urban Flooding"),
    ("Dam or Levee Failure", "River Overflow"),
    ("Dam or Levee Failure", "Urban Flooding"),
    ("River Overflow", "Urban Flooding"),
    ("Urban Drainage Basins", "Urban Flooding"),
    ("Land Use Changes", "Urban Drainage Basins"),
    ("Land Use Changes", "Soil Saturation"),
    ("Soil Saturation", "River Overflow"),
    ("Soil Saturation", "Urban Flooding"),
    ("Heavy Rainfall", "Urban Flooding")  
]

G.add_edges_from(edges)
...
```
"""


graph_requirement = [   
                        'Think step by step.',
                        'Entities form a causal graph; the given entities is a sink node, the other nodes are direct or indirect causes.',
                        'An entity can physical or non-physical, e.g., mountain, flood, ideology, orgnization, or policy.',
                        'Since the entities in the causal graph will be carefully investigated after creating the causal graph, such as collect data or conduct surveys, the provided entities need to be studies or have associated data.',                        
                        'If one entities is given, create a causal graph that contains entities cause the given entieis.',
                        'If several entities are given, create a causal graph contains these entities, but need to focus on the causality between the given entities, which means your need to find out the intermediate entities between the given entities, i.e., how one entity causes another. No need to find cause to the given entities.',
                        'Consider the proxy entities if your think a entity is difficult to measure.',
                        'You can ingore some unimportant causes, but do not ignore the critical cause, even these causes may seems insignificant to ordinary people.',
                        'The provided causes should be very professional and scientific, using suitable terms in that research field.',
                        'The causal graph is used for scientifica research and modeling for further explaination or prediction, so you need to try your best to make it accurate.',
                        'The graph will be stored in NetworkX. Disconnected components are NOT allowed.',
                        'You need to carefully name the nodes, making they human readable but not to long.',                         
                        'The connection between two nodes is an edge.', 
                        'Add all nodes and edges to a NetworkX instance.',   
                        'Put your reply into a Python code block, NO explanation or conversation outside the code block(enclosed by ```python and ```).',
                        'Note that GraphML writer does not support class dict or list as data values.', 
                        'Do not put the GraphML writing process as a step in the graph.',
                        'Keep the graph concise, DO NOT use too many nodes.',
 

                         ]