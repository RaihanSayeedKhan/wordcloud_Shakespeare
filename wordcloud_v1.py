"""
# Date: 09/07/2020
# Created by Raihan Sayeed Khan
# book title: The Complete Works of William Shakespeare
# Author:  William Shakespeare
# link: http://www.gutenberg.org/ebooks/100
# wordcloud helpful resources:
    - https://www.datacamp.com/community/tutorials/wordcloud-python
"""

# import
import codecs # to open utf-8 file
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

path = r'.\100-0.txt' # path to file
# reading file
with codecs.open(path, encoding='utf-8') as f:
    text = f.readlines()

text = [x for x in text if x.strip()] # removing whitespace elements 
text = text[62:] # deleting everything before the content
text = [y for y in text if not y.strip().isnumeric()] # getting rid of numbers
text = ''.join(text) # joining all the elements to a single string

# words 'not' to include
stpwrds = ['i', 'I', 'my', 'you', 'You', 'thee', 'Thee', 'he', 'He', 'she',
           'She', 'us', 'one', 'mine', 'thy', 'thou', 'whose', 'tis','upon', 'thus','though', 'll']

article = ['a', 'A', 'an', 'An', 'the', 'The']

from_file = ['_Exit'] # commands inside the file

misc= ['sir', 'Sir', 'madam', 'Madam', 'ay', 'Ay', 'Yea','nay', 'Nay', 'mylord', 
       'th', 'QUEEN', 'DUKE', 'KING', 'PRINCE', 'father', 'mother','son', 'daughter','brother', 'sister','man',
       'men', 'woman', 'women', 'will', 'll', 'ti', 'yet', 'much', 'hath', 'Enter', 'now', 'eye']

names = ['FALSTAFF', 'OTHELLO', 'CLEOPATRA', 'ANTONIO', 'ANTONY', 'HAMLET', 'BRUTUS', 'IAGO', 'ROMEO', 'CAESAR', 'ROSALIND', 'KINGHENRY', 'EMILIA', 'PETRUCHIO', 'KINGRICHARD', 
         'DESDEMONA', 'HELENA', 'BEROWNE', 'TIMON', 'PANDARUS', 'CORIOLANUS', 'TROLIUS', 'MACBETH', 'OLIVIA'
         'JULIET','POMPEY', 'LUCIUS', 'PALAMON', 'CLAUDIO', 'CELIA', 'THESEUS', 'CRESSIDA', 'BENEDICK', 'CASSIUS'
         'SEBASTIAN', 'SIRTOBY', 'PORTIA', 'LEONTES', 'TROILUS', 'TITUS', 'LEONATO', 'ARCITE', 'Isay',
         'MENENIUS', 'VIOLA', 'HORATIO', 'DONPEDRO', 'ANGELO', 'OLIVIA', 'CASSIO', 'BEATRICE', 'BERTRAM', 'VALENTINE',
         'PROTEUS', 'ISABELLA', 'PERICLES', 'TRANIO']

places = ['GLOUCESTER', 'WARWICK', 'BUCKINGHAM', 'ORLANDO', 'SUFFOLK', 'SICINIUS']

# joining all the lists along with default STOPWORDS
stopwords = set(list(STOPWORDS)+stpwrds+misc+from_file+names+places)
# set command make sures only unique elements are used

# generating wordcloud
wc = WordCloud(stopwords=stopwords, background_color="white", max_font_size=50, 
               min_font_size=10, max_words=100, random_state = 1, colormap = 'viridis')
wc.generate(text)

# plotting wordcloud
fig1 = plt.figure(figsize = (6, 4))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()

# saving the image
#wc.to_file("./wordcloud_Shakespeare.png") # resolution is not good
fig1.savefig('wordcloud_Shakespeare.png', dpi = 600)

