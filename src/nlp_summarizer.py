from textrank4zh import TextRank4Keyword, TextRank4Sentence

class NewsSummarizer:
    def __init__(self):
        self.tr4s = TextRank4Sentence()  # Initialize TextRank4Zh for sentence summarization

    def summarize(self, text, top_n=3):
        self.tr4s.analyze(text=text, lower=True, source='all')
        summarized_sentences = self.tr4s.get_key_sentences(num=top_n)
        summary = ' '.join([sentence.sentence for sentence in summarized_sentences])
        return summary
