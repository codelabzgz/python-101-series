from newspaper import Article

def getArticle(url= "https://www.fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones"):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    return article.summary