from collections import defaultdict

def merge_predictions(tri_preds, l2_preds, l3_preds, k=3):

    scores = defaultdict(int)

    for i, word in enumerate(l3_preds):
        scores[word] += 3 - i

    for i, word in enumerate(l2_preds):
        scores[word] += 2 - i

    for i, word in enumerate(tri_preds):
        scores[word] += 1 - i

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return [word for word, _ in ranked[:k]]
