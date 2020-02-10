
class Controller:
    def __init__(self, model):
        self.model = model

    def __str__(self):
         return "Controller ( model : {} )".format(self.model)

    def get_all_articles(self):
        return self.model.get_all_articles()

    def update_article(self, title, new_text):
        return self.model.update_article(title, new_text)

    def create_article(self, title, text):
        return self.model.create_article(title, text)

    def delete_article(self, title):
        return self.model.delete_article(title)



