import numpy as np
from util import get_args
from semanticscholar import SemanticScholar
from semanticscholar.Paper import Paper

def traverse_publications(
    seed_paper: Paper,
    depth: int = -1, 
    max_depth: int = 0,
 ) -> list[Paper]:
    """Traverse the Semantic Scholar Academic Graph by starting with a paper and visiting its references and citations.
    
    Args:
        seed_paper: paper to start graph traversal

        depth: the current depth of traversal. The first seed paper will have depth -1 by convention, and all references and citations of this paper will have depth 0, their references and citations depth 1, etc. 

        max_depth: the maximum depth to traverse. N.B. I have not had the patience to run past max_depth 1.

    Returns:
        a list of publications
    """

    papers = [seed_paper]

    print(f"Depth = {depth}")
    print(f"Title: {seed_paper.title}")

    if depth >= max_depth:
        return papers

    # N.B.: deep traversals will take forever

    # should get a maximum of 10 ** (max_depth + 1) vectors
    for item in seed_paper.references[:5] + seed_paper.citations[:5]:
        if item.paperId is not None:
            paper = sch.get_paper(item.paperId)
            traversed = traverse_publications(paper, depth + 1, max_depth)
            papers.extend(traversed)
        else:
            print("skipping publication with no paperId")

    return papers

def main(args):

    paper_id = args.paper_id
    vectors_fn = args.vectors
    titles_fn = args.titles
    max_depth = args.max_depth

    # Build up some literature space by traversing the S2AG

    # start with an initial paper
    seed_paper = sch.get_paper(paper_id)

    # start recursive call
    papers = traverse_publications(seed_paper, max_depth=max_depth)

    print(f"Number of publications crawled: {len(papers)}")

    vectors = [np.array(paper.embedding['vector']) for paper in papers]
    np.save(vectors_fn, vectors) # shape (number_publications, 768)

    titles = [paper.title for paper in papers]
    np.save(titles_fn, titles) # shape (number_publications,)

if __name__ == "__main__":
    args = get_args()
    sch = SemanticScholar()
    main(args)
