# semantic-scholar-demo

simple demo of semantic scholar literature api

## Requirements

Create a fresh conda environment with the required packages by running

`conda env create --file environment.yml`

## Running

To get a proof of concept plot of PCA-projected abstract embeddings for a handful of crawled publications, run the following scripts with the following optional arguments:

`python collect_papers.py --paper_id CorpusId:222139105 --vectors vectors.npy  --titles titles.npy`

`python visualize.py --plot plot.png`

This will just be the first 5 citations and first 5 references of an arbitrarily chosen starting publication, 'The Computational Origin of Representation'.

## S2AG api

See [the S2AG docs](https://api.semanticscholar.org/api-docs/graph) .

Here is a link to the S2AG documentation on [getting details about a paper](https://api.semanticscholar.org/api-docs/graph#tag/Paper-Data/operation/get_graph_get_paper) in the graph.

I am using the *unofficial* python client for S2AG, source [here](https://github.com/danielnsilva/semanticscholar#).
