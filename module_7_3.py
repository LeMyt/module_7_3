import io
import re

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        #print(self.file_names)


    def get_all_words(self):
        all_words = {}
        line3 = []
        for i in self.file_names:
            #print(i)
            with open(i, encoding='utf-8') as file:
                for line in file:
                    punctuation = r'[,.!?;:"\(\)\[\]\{\}\<\>\/\ - ]'
                    line = re.sub(punctuation, ' ', line)
                    #print(line)
                    for line2 in line.lower().split():
                        #print(line2)
                        line3.append(line2)
                        #line3.append(line2.split('\n'))
            #print(line3)
            all_words = {i: line3}
            print(all_words)




finder2 = WordsFinder('test.txt')
finder2.get_all_words()
