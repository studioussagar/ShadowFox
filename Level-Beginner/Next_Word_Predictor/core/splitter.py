from spellchecker import SpellChecker

class OptimizedVocabSpellChecker:

    def __init__(self, vocab):
        self.vocab = set(vocab)
        self.spell = SpellChecker(language=None)
        self.spell.word_frequency.load_words(vocab)

    def split_and_correct(self, token):
        n = len(token)
        dp = [[] for _ in range(n + 1)]
        dp[0] = [(0, [])]  # (cost, words)

        correction_cache = {}

        for i in range(n):
            if not dp[i]:
                continue

            for current_cost, current_words in dp[i]:

                for j in range(i + 1, n + 1):
                    piece = token[i:j]

                    # Exact vocab match
                    if piece in self.vocab and (len(piece) >= 2 or piece in {"i", "a"}):
                        dp[j].append((current_cost, current_words + [piece]))

                    # Try correction
                    elif len(piece) >= 3:

                        if piece not in correction_cache:
                            corrected = self.spell.correction(piece)
                            correction_cache[piece] = corrected if corrected else piece

                        corrected = correction_cache[piece]

                        if corrected != piece and corrected in self.vocab:
                            dp[j].append((current_cost + 1, current_words + [corrected]))

        if dp[n]:
            # Return all candidates sorted by cost
            dp[n].sort(key=lambda x: x[0])
            return [words for _, words in dp[n][:3]]  # top 3 lexical candidates

        # fallback single correction
        corrected = self.spell.correction(token)
        return [[corrected if corrected else token]]

    def split(self, sentence):
        words = sentence.split()
        new_words = []

        for word in words:
            if word in self.vocab:
                new_words.append(word)
            else:
                candidates = self.split_and_correct(word)
                new_words.extend(candidates[0])  # default minimal cost

        return " ".join(new_words)