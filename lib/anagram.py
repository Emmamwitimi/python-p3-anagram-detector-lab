# your code goes here!
class Anagram:

    def __init__(self,word):
        self.word = word
        self.sorted_word = sorted(word)

    def match(self,list):
        matches=[]
        for list_item in list:
            if sorted(list_item) == self.sorted_word:
                matches.append(list_item)

        return matches

