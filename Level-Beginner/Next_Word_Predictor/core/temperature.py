import numpy as np

def sample_with_temperature(preds, temperature=1.0, k=3):
    preds = np.log(preds + 1e-9) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)

    top_indices = preds.argsort()[-k:][::-1]
    return top_indices
