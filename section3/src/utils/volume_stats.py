"""
Contains various functions for computing statistics over 3D volumes
"""
import numpy as np

def Dice3d(a, b):
    """
    This will compute the Dice Similarity coefficient for two 3-dimensional volumes
    Volumes are expected to be of the same size. We are expecting binary masks -
    0's are treated as background and anything else is counted as data

    Arguments:
        a {Numpy array} -- 3D array with first volume
        b {Numpy array} -- 3D array with second volume

    Returns:
        float
    """
    if len(a.shape) != 3 or len(b.shape) != 3:
        raise Exception(f"Expecting 3 dimensional inputs, got {a.shape} and {b.shape}")

    if a.shape != b.shape:
        raise Exception(f"Expecting inputs of the same shape, got {a.shape} and {b.shape}")

    # TASK: Write implementation of Dice3D. If you completed exercises in the lessons
    # you should already have it.
    a = np.where(a > 0, 1, 0)
    b = np.where(b > 0, 1, 0)
    
    n_ab = (a * b).sum()
    n_a = a.sum()
    n_b = b.sum()
    return 2.0 * n_ab / (n_a + n_b)
    

def Jaccard3d(a, b):
    """
    This will compute the Jaccard Similarity coefficient for two 3-dimensional volumes
    Volumes are expected to be of the same size. We are expecting binary masks - 
    0's are treated as background and anything else is counted as data

    Arguments:
        a {Numpy array} -- 3D array with first volume
        b {Numpy array} -- 3D array with second volume

    Returns:
        float
    """
    if len(a.shape) != 3 or len(b.shape) != 3:
        raise Exception(f"Expecting 3 dimensional inputs, got {a.shape} and {b.shape}")

    if a.shape != b.shape:
        raise Exception(f"Expecting inputs of the same shape, got {a.shape} and {b.shape}")

    # TASK: Write implementation of Jaccard similarity coefficient. Please do not use 
    # the Dice3D function from above to do the computation ;)
    a = np.where(a > 0, 1, 0)
    b = np.where(b > 0, 1, 0)
    
    n_a_or_b = np.where(a + b > 0, 1, 0).sum()
    n_a_and_b = (a*b).sum()
    return 1.0*n_a_and_b / n_a_or_b

def Sensitivity(vol_pred, vol_true):
    """
    This will compute the sensitivity for two 3-dimensional volumes.
    The sensitivety is defined by TP / (TP + FN).

    Arguments:
        vol_pred {Numpy array} -- 3D array given as a prediction.
        vol_true {Numpy array} -- 3D array given as a ground truth.

    Returns:
        float
    """
    
    vol_pred = np.where(vol_pred > 0, 1, 0)
    vol_true = np.where(vol_true > 0, 1, 0)

    return 1.0*(vol_pred * vol_true).sum() / vol_true.sum()
    

def Specificity(vol_pred, vol_true):
    """
    This will compute the specificity for two 3-dimensional volumes.
    The specificity is defined by TN / (TN + FP).

    Arguments:
        vol_pred {Numpy array} -- 3D array given as a prediction.
        vol_true {Numpy array} -- 3D array given as a ground truth.

    Returns:
        float
    """
    
    ## flip 1, 0 values
    vol_pred_neg = np.where(vol_pred > 0, 0, 1)
    vol_true_neg = np.where(vol_true > 0, 0, 1)
    
    return 1.0*(vol_pred_neg * vol_true_neg).sum() / vol_true_neg.sum()
        