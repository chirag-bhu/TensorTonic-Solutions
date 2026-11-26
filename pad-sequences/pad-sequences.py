import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    

    if len(seqs) == 0:
        return np.empty((0, 0), dtype=int)

    if max_len is None:
        max_len = max(len(x) for x in seqs)

    result = []

    for x in seqs:

        x = x[:max_len]

        while len(x) < max_len:
            x.append(pad_value)

        result.append(x)

    return np.array(result, dtype=int)
    
    pass