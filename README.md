Providentia
===========

Goddess of forethought

CONFIGURATION
=============
- Create a new virtualenv
```
cd Providentia/
virtualenv venv
```
- Enter the virtual environment
```
source venv/bin/activate
```

- Add the requirements
```
pip install -r requirements.txt
```
- Modify the enviromental variable as you like. Check the section environmental variable.
```
e.g.
export NUMBER_KEYWORDS=2
```

RUNNING
=======
```
python app.py
```

ENVIRONMENTAL VARIABLES
=======================
- NUMBER_KEYWORDS: Number the keywords for document (default is 4)
- HIERARCHICAL_CLUSTERING_T: Similarity threshold to prune the tree to a set of final clusters. (default is 0.8)
- HIERARCHICAL_CLUSTERING_IMAGE: Image name for the dendrogram
- HIERARCHICAL_CLUSTERING_DPI: DPI for the dendrogram image
- RSS_DATA_SOURCE_TYPE: Type of data source for the RSS (default is JSON)

