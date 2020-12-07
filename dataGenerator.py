import numpy as np


def getVirtualEdgesToJamFactors(edgeKernel, numberOfEdge, numberOfJamFactor):
    IFREdgesToJamFactors = np.array([((0.9, 0.0), (0.0, 1.0), (0.0, 1.0), (0.0, 1.0)),
                                     ((0.2, 0.7), (0.4, 0.4), (0.2, 0.3), (0.0, 1.0)),
                                     ((0.2, 0.6), (0.0, 1.0), (0.0, 1.0), (0.7, 0.2)),
                                     ((0.2, 0.6), (0.4, 0.5), (0.3, 0.4), (0.0, 1.0)),
                                     ((0.3, 0.7), (0.0, 1.0), (0.4, 0.3), (0.0, 1.0)),
                                     ((0.0, 1.0), (0.0, 1.0), (0.1, 0.8), (0.6, 0.3)),
                                     ((0.0, 1.0), (0.5, 0.4), (0.8, 0.1), (0.0, 1.0))],
                                    dtype=edgeKernel)
    return IFREdgesToJamFactors
