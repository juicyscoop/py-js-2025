import re

import glob
#glob.glob()

text = """
sdfgergwegfgdfbvqet25623452435t5245t|||tomas@gmail.com2rqgrfqdfqfnorefr3340394
"""

pattern = r"\|\|\|.+@.+\.[com|de|io|rm]"

compiled_pattern = re.compile(pattern)

result = re.search(compiled_pattern, text)

print(result)

found_text = result.group()
print("found_text: ", found_text)

stripped_email = found_text.strip("|||")
print("stripped_email: ", stripped_email)

sliced_email = found_text[3:]
print("sliced_email: ", sliced_email)


