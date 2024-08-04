class WordsFinder:
    def __init__(self, *args):
        self.file_names = list(args)

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read()
                for i in punctuation:
                    text = text.replace(i, ' ')
                words = text.lower().split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        all_find = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            for i in words:
                if i == word:
                    index = words.index(i) + 1
                    all_find[name] = index
                    break
        return all_find

    def count(self, word):
        all_count = {}
        word = word.lower()

        for name, words in self.get_all_words().items():
            sum_word = 0
            for i in words:
                if i == word:
                    sum_word += 1
            all_count[name] = sum_word
        return all_count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
