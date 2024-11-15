import pandas as pd
import networkx as nx
import os



script_dir=os.path.dirname(os.path.abspath(__file__))
file_path=os.path.join(script_dir, "com-amazon.ungraph.txt")


df = pd.read_csv(file_path, delimiter="\t", header=None, names=["source", "target"])


#Using networkx to create an undirected grpah
G = nx.from_pandas_edgelist(df, source='source', target='target')

#Finding the most popular product node using degree. 
degree_table=pd.DataFrame(G.degree(), columns=['id', 'degree']).sort_values(by='degree', ascending=False)
most_popular=degree_table.head(1)  
most_popular_id =most_popular['id'].values[0]

# level-1 co-occurences of most popular product
co_occurrences=df[(df['source'] == most_popular_id) | (df['target'] == most_popular_id)]

#2nd level co-occurrences (products co-purchased with the 1st-level products)
level1 = co_occurrences['source'].astype(int).tolist() + co_occurrences['target'].astype(int).tolist()
level1 = list(set(level1))  

level2 = df[df['source'].isin(level1) | df['target'].isin(level1)]
level2.to_csv('Filtered-data-nodelinkk.csv', index=False, header=['source', 'target'])