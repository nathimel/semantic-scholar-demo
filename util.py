import argparse

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--paper_id",
        type=str,
        default="CorpusId:222139105",
        help="Semantic Scholar compatible paper id to begin graph traversal. See https://api.semanticscholar.org/api-docs/graph#tag/Paper-Data/operation/get_graph_get_paper for a list of supported types IDs.",
    )
    parser.add_argument(
        "--max_depth",
        type=int,
        default=0,
        help="The maximum depth of the graph traversal to execute, where root node has depth -1. I wouldn't recommend higher than 1.",
    )
    parser.add_argument(
        "--vectors",
        type=str,
        default="vectors.npy",
        help="Numpy filename for storing vector (SPECTER) embeddings of each document, in binary.",
    )
    parser.add_argument(
        "--titles",
        type=str,
        default="titles.npy",
        help="Numpy filename for storing titles for each publication, in binary.",
    )
    parser.add_argument(
        "--plot",
        type=str,
        default="plot.png",
        help="Plot of publication vectors in 2D literature space (PCA) will be saved to this file as png.",
    )
    args = parser.parse_args()
    return args