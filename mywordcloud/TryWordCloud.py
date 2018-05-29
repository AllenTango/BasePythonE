import wordcloud
from scipy.misc import imread

mask = imread("tonyjaramillo.png")
# mask = imread("idokungfoo-avatar.jpg")
f = open('CodeOfConduct.txt', 'r', encoding='utf-8')
t = f.read()
w = wordcloud.WordCloud(mask=mask, \
                        max_words = 200, background_color="white", width=460, height=460)
w.generate(t)
w.to_file("CodeOfConduct.png")
