import numpy
import nltk

def cosine_distance(feature_vectors, n):
    mat = numpy.empty((n, n))
    for i in xrange(0,n):
        for j in xrange(0,n):
           mat[i][j] = nltk.cluster.util.cosine_distance(feature_vectors[i],feature_vectors[j])
    return mat