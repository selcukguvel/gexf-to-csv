# gexf-to-csv

In order to convert the GEXF (Graph Exchange XML Format) files to the CSV files (nodes.csv and edges.csv)
use the command:

```python main.py yourFileName.gexf```


Note: _Python 3.6_ is recommended.

## Output CSV Files

### nodes.csv
This CSV file has two columns: nodeID and nodeName.
This CSV file can be used to convert the id's of the edges to the node's real names.

### edges.csv
This CSV file has three columns: SourceID, TargetID and weight.
"SourceID" and "TargetID" represents the id of the source and target nodes.
"weight" represents the weight of the edge. 
