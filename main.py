import requests
import json

class WordSearch:

    def __init__(self, search_word):
        self.search_word = search_word
        self.word_dict = self.find_related_words()
        self.word_list = self.get_list_of_related_words()

    def find_related_words(self):
        word_dict = {}
        url = "https://words.bighugelabs.com/api/2/be375f40e850c9dacdc82a3deaa1bb87/"+self.search_word+"/json"
        response = requests.request("GET", url)
        word_dict = json.loads(response.text)
        return word_dict

    def get_list_of_related_words(self):
        word_list = []
        for key, value in self.word_dict.items():
            inner_dict = value
            for x, y in inner_dict.items():
                if x != 'ant':
                    for word in y:
                        word_list.append(word)
        return word_list

def main():
    word = WordSearch('fire')
    print(word.word_list)


# the driver code
if __name__ == '__main__':
    main()
