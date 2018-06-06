import wordcloud

# 步骤1：配置对象参数
c = wordcloud.WordCloud()

# 步骤2：加载词云文本
c.generate("WordCloud by Python")

# 步骤3：输出词云文本
c.to_file("pywordcloud.png")