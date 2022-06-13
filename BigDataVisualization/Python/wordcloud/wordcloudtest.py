from wordcloud import WordCloud
import jieba

# with open('2.txt', 'r', encoding='utf-8') as f:
#     text = f.read()

text = "测试"

cut_text = " ".join(jieba.cut(text))
cloud = WordCloud(
    font_path = "d:\粗活意简.ttf", #if the file doesn't exist, just use the english words in docx
    # if use the chinese words in docx, the ttf file and the line should be executed.
    background_color = "white",
    max_words = 4000,
    max_font_size = 60
)
wCloud = cloud.generate(cut_text)
wCloud.to_file('cloud.jpg')
import matplotlib.pyplot as plt
plt.imshow(wCloud, interpolation='bilinear')
plt.axis('off')
plt.show()