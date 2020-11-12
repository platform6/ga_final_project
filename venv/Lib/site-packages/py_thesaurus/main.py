import argparse

from py_thesaurus.base_class import Thesaurus

parser = argparse.ArgumentParser(
    description='Get the thesaurus of word from  thesaurus.com/dictionary.com')
parser.add_argument('word', help="Word to get definition/synonym/antonym for")
parser.add_argument('-d', action='store_true',
                    help="get definition")
parser.add_argument('-s', choices=['noun', 'verb', 'adj'],
                    help="get POS specific synonyms")
parser.add_argument('-a', action='store_true',
                    help="get antonyms")

args = parser.parse_args()
# print(args.word)
# print(args.method)


def main():
    new_instance = Thesaurus(args.word)
    if args.d:
        print("Definitions")
        print(new_instance.get_definition())
    if args.s:
        print("Synonyms")
        print(new_instance.get_synonym(args.s))
    if args.a:
        print("Antonyms")
        print(new_instance.get_antonym())
    if not args.d and not args.s and not args.a:
        print("You must specify atleast one of the -d -s -a flags")
