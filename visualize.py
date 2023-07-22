import numpy as np
import plotnine as pn
import pandas as pd
from util import get_args
from sklearn.decomposition import PCA

def main(args):

    vectors_fn = args.vectors
    titles_fn = args.titles
    plot_fn = args.plot

    vectors = np.load(vectors_fn) # shape (num_publications, 768)
    titles = np.load(titles_fn) # shape (num_publications,)

    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(vectors)

    print(f"Explained variation per principal component: {pca.explained_variance_ratio_}")

    data = pd.DataFrame(pca_result, columns = ['pca1', 'pca2'])
    data['title'] = titles
    plot = (
        pn.ggplot(data=data, mapping=pn.aes(x="pca1", y="pca2"))
        + pn.geom_point(
            color="blue",
            shape="o",
            size=2,
            alpha=0.6,
        )
        + pn.geom_text(
            pn.aes(label="title"),
            va="bottom",
            size=6,
            nudge_x=10, 
        )        
        + pn.xlab("First principle component")
        + pn.ylab("Second principle component")
        + pn.scale_color_cmap("cividis")
    )

    plot.save(plot_fn, width=10, height=10, dpi=300)

if __name__ == "__main__":
    args = get_args()
    main(args)