
class ArticleAlreadyExistException(Exception):
    def __init__(self, message):
        self.message = message


class NonExistantArticleException(Exception):
    def __init__(self, message):
        self.message = message


class ModelInMemory:
    def __init__(self, articles):
        self.articles = articles

    def __str__(self):
        return "inmemory"

    def get_all_articles(self):
        return self.articles

    def update_article(self, title, new_text):
        for article in self.articles:
            if article.title == title:
                article.text = new_text
                return
        raise NonExistantArticleException("Article '{}' does not exist".format(title))


    def create_article(self, title, text):
        for article in self.articles:
            if article.title == title:
                raise ArticleAlreadyExistException("Article '{}' already exists".format(title))
        new_article = Article(title, text)
        self.articles.append(new_article)

    def delete_article(self, title):
        for article in self.articles:
            if article.title == title:
                self.articles.remove(article)
                return
        raise NonExistantArticleException("Article '{}' does not exist".format(title))


class ModelInMemory1:
    def __str__(self):
        return "inmemory1"


class ModelInMemory2:
    def __str__(self):
        return "inmemory2"


class Article:
    def __init__(self, title, text):
        self.text = text
        self.title = title

    def get_title(self):
        return self.title

    def get_text(self):
        return self.text
