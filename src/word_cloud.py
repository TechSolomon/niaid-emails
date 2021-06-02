# Word Cloud & Data Visualization

import os
import sys

from wordcloud import WordCloud, STOPWORDS

os.chdir(sys.path[0])

# Read Text
text = open('foia_emails.txt', mode='r', encoding='utf-8').read()
stopwords = STOPWORDS

wc = WordCloud(
    background_color='white',
    stopwords=stopwords,
    height=600,
    width=400
)

wc.generate(text)
print(">> Generating the word cloud...")

# Store to File
wc.to_file('foia_emails_output.png')
print(">> Finished generating and saved to src/foia_emails_output.png.")
