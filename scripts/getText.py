from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)



articles = open('scripts/articles.txt')

for article in articles:
    html = urllib.request.urlopen(article).read()
    # currentArticle = open(article)
    title = input(f'What is the title we should use for the article at URL {article} ?\n--> ')
    articleWriter = open(f'Articles/scripted/{title}.txt','w')
    articleWriter.write(text_from_html(html))