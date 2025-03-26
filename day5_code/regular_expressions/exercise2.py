import re

def read_text_file(filename):
    # Precist text ze souboru filename -> vratit tento text
    with open(filename, 'r') as file:
        return file.read() # Vracime string

def match_examples(input_text):
    # Find all occurrences of the word 'love'
    #pattern1 = r'[\s"]?[lL]ove[\s\.,!?"]'
    #compiled_pattern1 = re.compile(pattern1)

    # Find all occurrences that match the pattern <sure>%
    #pattern2 = r'<sure>%'
    #compiled_pattern2 = re.compile(pattern2)

    # Find all occurrences of words that end with "?"
    # Rozdelovani slov (odradkovani) timto patternem nezachytime!
    #pattern3 = r'[a-zA-Z\']+\?{1}'
    #compiled_pattern3 = re.compile(pattern3)

    # Find all words that contain the string "fair" (case-insensitive)
    pattern4 = r'[a-zA-Z]*fair\w*[\.!\?,]?'
    compiled_pattern4 = re.compile(pattern4, re.IGNORECASE)

    # findall - pouzijeme findall protoze hledame vsechny vyskyty "love", a ne jen jeden
    #search_result = re.search(compiled_pattern1, input_text)

    search_results = re.findall(compiled_pattern4, input_text)
    print(f"search_result: {search_results}")
    print(f"number of matched text parts: {len(search_results)}.")


filename = "text_en.txt"
hamlet = read_text_file(filename)
match_examples(hamlet)
