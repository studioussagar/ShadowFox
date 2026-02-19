from spellchecker import SpellChecker

class OptimizedVocabSpellChecker:

    def __init__(self, vocab):
        self.vocab = set(vocab)
        self.spell = SpellChecker(language=None)
        self.spell.word_frequency.load_words(vocab)

    def split_and_correct(self, token):
        n = len(token)
        dp = [None] * (n + 1)
        dp[0] = (0, [])

        correction_cache = {}

        for i in range(n):
            if dp[i] is None:
                continue

            current_cost, current_words = dp[i]

            for j in range(i + 1, n + 1):
                piece = token[i:j]

                if piece in self.vocab and (len(piece) >= 2 or piece in {"i", "a"}):
                    new_cost = current_cost
                    new_words = current_words + [piece]

                    if dp[j] is None or new_cost < dp[j][0]:
                        dp[j] = (new_cost, new_words)

                elif len(piece) >= 3:

                    if piece not in correction_cache:
                        corrected = self.spell.correction(piece)
                        correction_cache[piece] = corrected if corrected else piece

                    corrected = correction_cache[piece]

                    if corrected != piece and corrected in self.vocab:
                        new_cost = current_cost + 1
                        new_words = current_words + [corrected]

                        if dp[j] is None or new_cost < dp[j][0]:
                            dp[j] = (new_cost, new_words)

        if dp[n] is not None:
            return dp[n][1]

        if token not in correction_cache:
            corrected = self.spell.correction(token)
            correction_cache[token] = corrected if corrected else token

        return [correction_cache[token]]

    def split(self, sentence):
        words = sentence.split()
        new_words = []

        for word in words:
            if word in self.vocab:
                new_words.append(word)
            else:
                new_words.extend(self.split_and_correct(word))

        return " ".join(new_words)
