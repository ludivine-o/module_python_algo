from blog_model_db import ModelDB
from blog_controller import Controller

def main():
    controller = Controller(ModelDB())
    while True:
        choice_letter = input(
            "\n(L)ister (M)odifer (A)jouter (S)upprimer (Q)uitter: ").upper()
        if choice_letter == "A":
            title = input("entrez le titre : ")
            text = input("entrez le texte : ")
            controller.create_article(title, text)
        elif choice_letter == "S":
            title = input("entrez le titre à supprimer : ")
            controller.delete_article(title)
        elif choice_letter == "L":
            articles = controller.get_all_articles()
            for article in articles:
                print([article.get_title(), article.get_text()])
        elif choice_letter == "M":
            title = input("entrez le titre : ")
            text = input("entrez le texte : ")
            controller.update_article(title, text)
        elif choice_letter == "Q":
            break
        else:
            print("commande non reconnue")


if __name__ == '__main__':
    main()

