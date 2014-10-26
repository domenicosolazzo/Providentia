
import pylab
from hcluster import linkage, dendrogram
from providentia.configurations.config import ConfigurationManager
class HierarichicalCluster(object):
    """
    Agglomerative or hierarchical clustering. Here clusters are grown by fusing neighboring documents to form a tree.
    The structure of that tree may change radically among different days but we can choose a similarity threshold to
    prune the tree to a set of final clusters. That similarity metric can be constant over days.
    """
    def __init__(self, t):
        config_manger = ConfigurationManager()
        self.t = config_manger.HIERARCHICAL_CLUSTERING_T
        self.cluster_image = config_manger.HIERARCHICAL_CLUSTERING_IMAGE
        self.dpi = config_manger.HIERARCHICAL_CLUSTERING_DPI

    def fetch_clusters(self, mat, n):
        """
        Fetch the cluster from the similarity matrix
        :param mat: The similarity matrix
        :param n: The length of the corpus
        :return: The clusters
        """
        Z = linkage(mat, 'single')
        dendrogram(Z, color_threshold=self.t)

        pylab.savefig(self.cluster_image ,dpi=self.dpi)
        clusters = self.__extract_clusters(Z,self.t,n)
        return clusters

    def __extract_clusters(self,Z,threshold,n):
       clusters={}
       ct=n
       for row in Z:
          if row[2] < threshold:
              n1=int(row[0])
              n2=int(row[1])

              if n1 >= n:
                 l1=clusters[n1]
                 del(clusters[n1])
              else:
                 l1= [n1]

              if n2 >= n:
                 l2=clusters[n2]
                 del(clusters[n2])
              else:
                 l2= [n2]
              l1.extend(l2)
              clusters[ct] = l1
              ct += 1
          else:
              return clusters

