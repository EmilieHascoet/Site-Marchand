# Importation des différents modules
from tkinter import *
import time

############################################# Fenêtre de connexion #####################################################

# Création d'une fenetre connexion et définition de ses paramètres
FenetreConnexion = Tk()
FenetreConnexion.resizable(False, False)
FenetreConnexion.title('Connexion [ Filmanga ]')
FenetreConnexion.config(width=1286, height=700)

# Création d'une zone de dessin dans la fenêtre connexion
CanevasConnexion = Canvas(FenetreConnexion, width=1288, height=700, bg='white')
CanevasConnexion.place(x=-2, y=-2)

################################################## Fenêtre Shop ########################################################

# Création d'une fenetre shop et définitions de ses paramètres
FenetreShop = Toplevel()
FenetreShop.resizable(False, False)
FenetreShop.title('Film [ Filmanga ]')
FenetreShop.config(width=1288, height=700)
# Cache la fenetre shop
FenetreShop.withdraw()

########################################################################################################################
######################################## Fenêtre Shop, Barre de navigation #############################################
########################################################################################################################

# Création d'un frame pour la barre de nagivation
FrameNavigation = Frame(FenetreShop, width=1088, height=100, bg='black')
FrameNavigation.place(x=5, y=5)


def film():
    """ Modifie la FenetreShop pour correspondre à l'onglet film du site."""
    # Modifie le titre de la fenêtre
    FenetreShop.title('Film [ Filmanga ]')
    # Réinitialise la couleur des onglets et supprime les éléments indésirables
    clean_shop()
    # Modifie la couleur pour indiquer sur quel onglet on est
    Film.config(bg='#98f796')
    # Affiche les dvd film dans le CanevasShop
    shop(0, 8)


# Affiche le texte "Film" en tant que bouton
Film = Button(FrameNavigation, text="Film", bg='#98f796', padx=30, pady=50,
              font=('MV Boli', 20), borderwidth=0, highlightthickness=0, cursor="heart",
              command=film)
Film.place(x=152, y=50, anchor=CENTER)

# Affiche le logo du site en tant que bouton pour aller à la page "film"
Logo2 = PhotoImage(file='Design/Logo2.png')
BoutonLogo = Button(FrameNavigation, image=Logo2, highlightthickness=0,
                    borderwidth=0, activebackground='black', cursor="heart", command=film)
BoutonLogo.place(x=43, y=50, anchor=CENTER)


def film_scifi():
    """ Modifie la FenetreShop pour correspondre à l'onglet film science
    fiction du site."""
    # Modifie le titre de la fenêtre
    FenetreShop.title('Film/Science-fiction [ Filmanga ]')
    # Réinitialise la couleur des onglets et supprime les éléments indésirables
    clean_shop()
    # Modifie la couleur pour indiquer sur quel onglet on est
    FilmSci.config(fg='#98f796')
    # Affiche les dvd film science-fiction dans le CanevasShop
    shop(8, 16)


# Affiche le texte "Science-fiction" en tant que bouton
FilmSci = Button(FrameNavigation, text="Science-fiction", bg='black',
                 fg='#31bbf7', font=('MV Boli', 13), borderwidth=0, highlightthickness=0,
                 activebackground='black', activeforeground='white', cursor="heart",
                 command=film_scifi)
FilmSci.place(x=330, y=50, anchor=CENTER)


def film_com():
    """ Modifie la FenetreShop pour correspondre à l'onglet film comédie
    du site."""
    # Modifie le titre de la fenêtre
    FenetreShop.title('Film/Comédie [ Filmanga ]')
    # Réinitialise la couleur des onglets et supprime les éléments indésirables
    clean_shop()
    # Modifie la couleur pour indiquer sur quel onglet on est
    FilmCom.config(fg='#98f796')
    # Affiche les dvd film comédie dans le CanevasShop
    shop(16, 24)


# Affiche le texte "Comédie" en tant que bouton
FilmCom = Button(FrameNavigation, text="Comédie", bg='black', fg='#31bbf7',
                 font=('MV Boli', 13), borderwidth=0, highlightthickness=0,
                 activebackground='black', activeforeground='white', cursor="heart",
                 command=film_com)
FilmCom.place(x=480, y=50, anchor=CENTER)

# Importe les images d'erreur 404
ImageErreur = PhotoImage(file='Design/Erreur.png')
ImageErreur2 = PhotoImage(file='Design/Erreur2.png')
ImageErreur3 = PhotoImage(file='Design/Erreur3.png')


def manga():
    """ Modifie la FenetreShop pour correspondre à l'onglet manga du site."""
    # Réinitialise la couleur des onglets et supprime les éléments indésirables
    clean_shop()
    # Modifie le titre de la fenêtre
    FenetreShop.title('Manga/Erreur 404 [ Filmanga ]')
    # Modifie la couleur pour indiquer sur quel onglet on est
    Manga.config(bg='#98f796')
    # Affiche l'image d'erreur 404
    CanevasShop.create_image(675, 295, image=ImageErreur)


# Affiche le texte "Manga" en tant que bouton
Manga = Button(FrameNavigation, text="Manga", pady=50, padx=30,
               font=('MV Boli', 20), borderwidth=0, highlightthickness=0, cursor="heart",
               command=manga)
Manga.place(x=652, y=50, anchor=CENTER)


def manga_surna():
    """ Modifie la FenetreShop pour correspondre à l'onglet manga shounen
    ai du site."""
    # Réinitialise la couleur des onglets et supprime les éléments indésirables
    clean_shop()
    # Modifie le titre de la fenêtre
    FenetreShop.title('Manga/Surnaturel/Erreur 404 [ Filmanga ]')
    # Modifie la couleur pour indiquer sur quel onglet on est
    MangaSurna.config(fg='#98f796')
    # Affiche l'image d'erreur 404
    CanevasShop.create_image(640, 295, image=ImageErreur2)


# Affiche le texte "Suernaturel" en tant que bouton
MangaSurna = Button(FrameNavigation, text="Surnaturel", bg='black',
                    fg='#31bbf7', font=('MV Boli', 13), borderwidth=0, highlightthickness=0,
                    activebackground='black', activeforeground='white', cursor="heart",
                    command=manga_surna)
MangaSurna.place(x=840, y=50, anchor=CENTER)


def manga_sei():
    """ Modifie la FenetreShop pour correspondre à une l'onglet manga seinen
    du site."""
    # Réinitialise la couleur des onglets et supprime les éléments indésirables
    clean_shop()
    # Modifie le titre de la fenêtre
    FenetreShop.title('Manga/Seinen/Erreur 404 [ Filmanga ]')
    # Modifie la couleur pour indiquer sur quel onglet on est
    MangaSei.config(fg='#98f796')
    # Affiche l'image d'erreur 404
    CanevasShop.create_image(647, 295, image=ImageErreur3)


# Affiche le texte "Seinen" en tant que bouton
MangaSei = Button(FrameNavigation, text="Seinen", bg='black', fg='#31bbf7',
                  font=('MV Boli', 13), borderwidth=0, highlightthickness=0,
                  activebackground='black', activeforeground='white', cursor="heart",
                  command=manga_sei)
MangaSei.place(x=990, y=50, anchor=CENTER)

############################################ Fenêtre Shop, Connexion ###################################################

# Création d'une zone de dessin pour la partie connexion du shop
CanevasSign = Canvas(FenetreShop, width=185, height=100, bg='black')
CanevasSign.place(x=1096, y=3)

# Création d'un texte qui indique quel utilisateur est connecté
TexteConnecte = Label(CanevasSign, text="Vous ne\npouvez pas\nfaire \
d'achat\nsans compte", fg='#31bbf7', bg='black', font=('Georgia', 10))
TexteConnecte.place(x=55, y=52, anchor=CENTER)

# Bouton déconnection et changer mdp
BoutonDeco = Button(CanevasSign, text='Deconnexion', bg='white',
                    pady=2, padx=3, font=('Impact', 10), cursor="heart", command=lambda: deconnexion())

BoutonChangerMdp = Button(CanevasSign, text='Changer Mdp', bg='white',
                          pady=2, padx=3, font=('Impact', 10), cursor="heart",
                          command=lambda: [deconnexion(), page_nouveau_mdp()])


def sign_in():
    """ Modifie le design de la FenetreConnection pour que l'utilisateur
    puisse se connecter à son compte client."""
    global page
    # Cache la fenêtre d'aucun utilisateur connecté
    FenetreNonConnecte.withdraw()
    # Initialise page pour connaître si on est sur la page sign in ou sign up
    page = 1
    # Supprime tous les objets du Canevas Log
    CanevasLog.delete(ALL)
    # Cache l'entrée mdp2
    EntreeMdp2.place_forget()

    # Textes et entrées pseudo et mdp
    CanevasLog.create_text(32, 23, text="Nom d'utilisateur",
                           font=('MV Boli', 12, 'bold'), anchor=NW)
    EntreePseudo.place(x=32, y=50)
    CanevasLog.create_text(32, 123, text="Mot de passe",
                           font=('MV Boli', 12, 'bold'), anchor=NW)
    EntreeMdp.place(x=32, y=150)
    # Place la case à cocher pour afficher le mot de passe
    CaseVoirMdp.place(x=32, y=220)
    # Modifie les boutons connexion, mdp oublié, swap et retour
    BoutonConnexion.config(text="Se connecter", command=se_connecter, padx=39)
    BoutonConnexion.place(x=255, y=273, anchor=CENTER)
    BoutonMdpOublie.config(text="Mot de passe oublié ?", command=mdp_oublie)
    BoutonMdpOublie.place(x=9, y=304)
    BoutonSwap.config(text="Nouveau sur Filmanga ?", command=sign_up)
    BoutonSwap.place(x=333, y=326, anchor=SE)
    BoutonRetour.config(text="Visiteur", padx=53,
                        command=lambda: [FenetreConnexion.withdraw(), FenetreShop.deiconify()])
    BoutonRetour.place(x=85, y=273, anchor=CENTER)

    # Cache la fenetre shop
    FenetreShop.withdraw()
    # Affiche la fenêtre connexion
    FenetreConnexion.deiconify()


# Bouton pour se connecter
BoutonSignIn = Button(CanevasSign, text='Sign in', bg='white',
                      pady=2, padx=8, font=('Impact', 10), cursor="heart", command=sign_in)
BoutonSignIn.place(x=112, y=15)


def sign_up():
    """ Modifie le design de la FenetreConnection pour que l'utilisateur
    puisse se créer un compte."""
    global page, CriterePseudo, CritereMdp
    # Cache la fenêtre d'aucun utilisateur connecté
    FenetreNonConnecte.withdraw()
    # Initialise page pour connaître si on est sur la page sign in ou sign up
    page = 2
    # Supprime tous les objets du Canevas Log
    CanevasLog.delete(ALL)
    # Cache l'entrée mdp2
    EntreeMdp2.place_forget()

    # Textes et entrées pseudo et mdp
    CanevasLog.create_text(32, 23, text="Nom d'utilisateur",
                           font=('MV Boli', 12, 'bold'), anchor=NW)
    CriterePseudo = CanevasLog.create_text(32, 80, text="La taille du nom \
d'utilisateur doit être compris\nentre un et dix caractères", fill='#002ee8',
                                           anchor=NW)
    EntreePseudo.place(x=32, y=50)
    CanevasLog.create_text(32, 123, text="Mot de passe",
                           font=('MV Boli', 12, 'bold'), anchor=NW)
    CritereMdp = CanevasLog.create_text(32, 180, text="Utilisez au moins trois \
caractères avec des lettres\nminuscules, majuscules et des chiffres",
                                        fill='#002ee8', anchor=NW)
    EntreeMdp.place(x=32, y=150)
    # Affiche la case à cocher pour afficher le mot de passe
    CaseVoirMdp.place(x=32, y=220)
    # Modifie les bouton connexion, mdp oublié, swap et retour
    BoutonConnexion.config(text="Créer son compte", command=creer_compte,
                           padx=24)
    BoutonMdpOublie.config(text="Mot de passe oublié ?", command=mdp_oublie)
    BoutonSwap.config(text="Déjà enregistré ?", command=sign_in)
    BoutonRetour.config(text="Visiteur", padx=53,
                        command=lambda: [FenetreConnexion.withdraw(), FenetreShop.deiconify()])

    # Cache la fenetre shop
    FenetreShop.withdraw()
    # Affiche la fenêtre connexion
    FenetreConnexion.deiconify()


# Bouton pour créer un compte
BoutonSignUp = Button(CanevasSign, text='Sign up', bg='white',
                      pady=2, padx=7, font=('Impact', 10), cursor="heart", command=sign_up)
BoutonSignUp.place(x=112, y=60)

################################################ Fenêtre Shop, Articles ################################################

# Zone de dessin dans la fenêtre shop
CanevasShop = Canvas(FenetreShop, width=1288, height=590, bg='#f7f596')
CanevasShop.place(x=-2, y=108)

# Liste avec les paramètres des 24 boutons
BoutonAjouter = [(Button(FenetreShop, text='Ajouter au sac à dos', relief=FLAT,
                         bg='#31bbf7', cursor="star")) for x in range(24)]


def shop(premiermoinsun, dernier):
    """Prend en paramètre deux nombres (premiermoinsun int,dernier int), qui
    permettra de choisir quelle partie de la liste "Articles".
    Affiche dans la zone de dessin de la fenêtre shop (CanevasShop) les
    articles + leur prix + le bouton ajouter au panier."""
    # Initialisation de j
    j = -1
    for i in range(premiermoinsun, dernier):
        # Ajoute +1 à j à chaque itération
        j += 1
        # Image de l'article
        CanevasShop.create_image((j % 4) * 315 + 175, (j // 4) * 295 + 120,
                                 image=Articles[i][0])
        # Texte du nom de l'article
        CanevasShop.create_text((j % 4) * 315 + 175, (j // 4) * 290 + 240,
                                text=Articles[i][1], font=('Georgia', 13))
        # Texte du prix de l'article
        CanevasShop.create_text((j % 4) * 315 + 235, (j // 4) * 290 + 275,
                                text=str(Articles[i][2]) + ' €', font=('Arial', 14, 'bold'),
                                fill='#c738c9')
        # Définit la command du bouton associé à l'article
        BoutonAjouter[i].place(x=(j % 4) * 315 + 75, y=(j // 4) * 290 + 370)
        exec('BoutonAjouter[i].config(command=lambda: plus_panier\
        (4,' + str(i) + '))')


# Liste contenant toutes les infos sur tous les films et mangas
Articles = [
    [PhotoImage(file='Articles/1/1.png'), 'Big Fish', 19.99],
    [PhotoImage(file='Articles/1/2.png'), 'Les Noces Funèbres', 11.99],
    [PhotoImage(file='Articles/1/3.png'), 'Alice au Pays des Merveilles', 11.99],
    [PhotoImage(file='Articles/1/4.png'), 'Mars Attacks', 14.99],
    [PhotoImage(file='Articles/1/5.png'), 'Tex Avery', 49.99],
    [PhotoImage(file='Articles/1/6.png'), 'La saga Twilight', 59.99],
    [PhotoImage(file='Articles/1/7.png'), "The Big Bang Theory", 44.99],
    [PhotoImage(file='Articles/1/8.png'), "L'autobus à impériale", 39.99],
    [PhotoImage(file='Articles/2/1.png'), 'Avatar', 14.99],
    [PhotoImage(file='Articles/2/2.png'), 'Pixels + stickers', 24.99],
    [PhotoImage(file='Articles/2/3.png'), 'I, Robot', 14.99],
    [PhotoImage(file='Articles/2/4.png'), 'Je suis une légende', 14.99],
    [PhotoImage(file='Articles/2/5.png'), 'Interstellar', 11.99],
    [PhotoImage(file='Articles/2/6.png'), 'Abyss', 11.99],
    [PhotoImage(file='Articles/2/7.png'), 'Bienvenue à Gattaca', 9.99],
    [PhotoImage(file='Articles/2/8.png'), "Minority Report", 9.99],
    [PhotoImage(file='Articles/3/1.png'), 'Ghostbusters', 14.99],
    [PhotoImage(file='Articles/3/2.png'), 'Beetlejuice', 11.99],
    [PhotoImage(file='Articles/3/3.png'), 'Tanguy', 19.99],
    [PhotoImage(file='Articles/3/4.png'), "Bienvenue chez les ch'tis", 11.99],
    [PhotoImage(file='Articles/3/5.png'), 'Podium', 9.99],
    [PhotoImage(file='Articles/3/6.png'), 'Le petit Nicolas', 9.99],
    [PhotoImage(file='Articles/3/7.png'), 'Charlie et la Chocolatrie', 11.99],
    [PhotoImage(file='Articles/3/8.png'), "Nanny McPhee", 9.99]
]

# Liste contenant toutes les images plus petites pour le panier
ImagesPanier = [PhotoImage(file='Panier/1/1.png'),
                PhotoImage(file='Panier/1/2.png'), PhotoImage(file='Panier/1/3.png'),
                PhotoImage(file='Panier/1/4.png'), PhotoImage(file='Panier/1/5.png'),
                PhotoImage(file='Panier/1/6.png'), PhotoImage(file='Panier/1/7.png'),
                PhotoImage(file='Panier/1/8.png'), PhotoImage(file='Panier/2/1.png'),
                PhotoImage(file='Panier/2/2.png'), PhotoImage(file='Panier/2/3.png'),
                PhotoImage(file='Panier/2/4.png'), PhotoImage(file='Panier/2/5.png'),
                PhotoImage(file='Panier/2/6.png'), PhotoImage(file='Panier/2/7.png'),
                PhotoImage(file='Panier/2/8.png'), PhotoImage(file='Panier/3/1.png'),
                PhotoImage(file='Panier/3/2.png'), PhotoImage(file='Panier/3/3.png'),
                PhotoImage(file='Panier/3/4.png'), PhotoImage(file='Panier/3/5.png'),
                PhotoImage(file='Panier/3/6.png'), PhotoImage(file='Panier/3/7.png'),
                PhotoImage(file='Panier/3/8.png')]

# affiche les dvd film dans le CanevasShop
shop(0, 8)

########################################################################################################################
#################################### Fichier contenant les paniers utilisateurs ########################################

# On lit le fichier CSV avec les paniers
FichierPaniers = open('paniers.csv', 'r')
Donnees2 = FichierPaniers.read().split('\n')[:-1]
FichierPaniers.close()

# Construction du dico panier
DicoPaniers = {}
for line in Donnees2:
    Line = line.split(';')
    DicoPaniers[Line[0]] = {}
    for i in range(len(Articles)):
        DicoPaniers[Line[0]][i] = 0
    for i in range(len(Line[1:])):
        DicoPaniers[Line[0]][i] = int(Line[1 + i])

############################################## Fenêtre Shop, Panier ####################################################

# Importe le panier d'achat + Création du bouton
image_panier = PhotoImage(file='Design/Panier.png')
image_panier2 = PhotoImage(file='Design/Panier2.png')
BoutonPanier = Button(CanevasSign, image=image_panier, borderwidth=0,
                      highlightthickness=0, activebackground='black', cursor="heart",
                      command=lambda: [actualise_panier(1)])

# Texte qui indique combien il y a d'articles dans le panier
TexteArticle = Label(CanevasSign, fg='yellow', bg='black')

Panier = {}

# Fenetre d'erreur car pas d'utilisateur connecter
FenetreNonConnecte = Toplevel()
FenetreNonConnecte.resizable(False, False)
FenetreNonConnecte.title("Pas d'utilisateur connecté")
FenetreNonConnecte.config(width=500, height=175, bg='white')
# Cache la fenetre non connecte
FenetreNonConnecte.withdraw()

# Création d'une frame pour le titre de la fenêtre
FrameNonConnecte = Frame(FenetreNonConnecte, width=500, height=40,
                         relief=FLAT, bg='#31bbf7')
FrameNonConnecte.place(x=0, y=0)
# Titre de la fenêtre
Label(FrameNonConnecte, text="Aucun utilisateur n'est connecté", bg='#31bbf7',
      font=('Times New Roman', 13, 'bold')).place(x=10, y=8)

# Texte de renseignement
Label(FenetreNonConnecte, text="Si vous voulez ce dvd dans votre sac à dos \
vous devez d'abord soit vous créer\nun compte sur ce site ou alors vous \
connecter à un compte existant.\n\nAvouez que dans le fond vous le voulez \
vraiment ce dvd :D", bg='white',
      justify=LEFT).place(x=220, y=83, anchor=CENTER)

# Bouton pour se connecter
Button(FenetreNonConnecte, text='Se connecter !', bg='#31bbf7',
       fg='white', cursor="heart", font=('Verdana', 10),
       command=lambda: sign_in()).place(x=125, y=145, anchor=CENTER)
# Bouton pour créer un compte
Button(FenetreNonConnecte, text='Créer un compte !', bg='#31bbf7',
       fg='white', cursor="heart", font=('Verdana', 10),
       command=lambda: sign_up()).place(x=375, y=145, anchor=CENTER)


def plus_panier(page, numero_article):
    """ Prend comme paramètres le numéro de la page de CanevasPanier(page int)
    sur laquelle on veut ajouter l'article du panier + le numéro de l'article
    (numero_article str).
    Si un utilisateur est connecté : ajoute l'article du panier utilisateur et
    sauvegarde le panier.
    Sinon affiche un message d'erreur."""
    global nombre_articles
    try:
        # Ajoute un article en plus dans le dico Panier
        Panier[numero_article] += 1
        # Sauvegarde le panier
        sauvegarde_panier()
        # Modifie le nombre d'articles total
        nombre_articles += 1
        TexteArticle.config(text=nombre_articles)
        if page != 4:
            # Actualise le panier
            actualise_panier(page)
    except:
        # Ouvre une fenêtre d'erreur
        FenetreNonConnecte.deiconify()


def moins_panier(page, numero_article):
    """ Prend comme paramètres le numéro de la page de CanevasPanier(page int)
    sur laquelle on veut retirer l'article du panier + le numéro de l'article
    (numero_article str).
    Retourne l'article du panier utilisateur, sauvegarde le panier."""
    global nombre_articles
    # Ajoute un article en plus dans le dico Panier
    Panier[numero_article] += -1
    # Sauvegarde le panier
    sauvegarde_panier()
    # Modifie le nombre d'articles total
    nombre_articles += -1
    TexteArticle.config(text=nombre_articles)
    # Actualise le panier
    actualise_panier(page)


def passer_commande(debitement):
    """Prend comme paramètre le prix total(debitement str) de tous les
    articles dans le panier.
    Si il y a des articles dans le panier passe la commande, vide le panier de
    l'utilisateur et affiche un petit texte comme quoi la commande est bien
    passé.
    Sinon, affiche un texte comme quoi il n'y a rien dans le panier.
    Puis amène l'utilisateur sur le Canevas Shop du site"""
    global nombre_articles, Panier
    if float(debitement) > 0:
        # Retire tous les articles du panier
        for i in range(len(Articles)):
            Panier[i] = 0
        DicoPaniers[pseudo] = Panier
        nombre_articles = 0
        TexteArticle.config(text=nombre_articles)
        # Sauvegarde le panier
        sauvegarde_panier()
        # Actualise le panier
        actualise_panier(1)
        CanevasPanier.create_text(546, 295, text="Vous venez d'être débité de "
                                                 + str(debitement) + "€\n\nJe vous remercie d'avoir passer commande "
                                                                     "chez Filmanga\net je vous souhaite une "
                                                                     "agréable journée ;)", justify=CENTER,
                                  fill='#31bbf7', font=('Georgia', 15, 'bold'))
    else:
        CanevasPanier.create_text(546, 295, text="Vous n'avez actuellement \
aucun article dans votre sac à dos.\nMais vous pouvez allez faire un tour \
dans\nnotre magasin pour le remplir :D", justify=CENTER, fill='#31bbf7',
                                  font=('Georgia', 15, 'bold'))


# Zone de dessin pour le panier dans la FenetreShop
CanevasPanier = Canvas(FenetreShop, width=1093, height=590, bg='#f7f596')
CanevasPanier2 = Canvas(FenetreShop, width=1093, height=590, bg='#f7f596')
CanevasPanier3 = Canvas(FenetreShop, width=1093, height=590, bg='#f7f596')

# Liste des paramètres des 24 boutons '+' du panier
BoutonPlus = [(Button(FenetreShop, text='+', relief=FLAT,
                      bg='#31bbf7', cursor="star")) for x in range(24)]
# Liste des paramètres des 24 boutons '-' du panier
BoutonMoins = [(Button(FenetreShop, text='-', relief=FLAT, padx=3,
                       bg='#31bbf7', cursor="star")) for x in range(24)]

# Zone de dessin pour l'espace commande dans la FenetreShop
CanevasCommande = Canvas(FenetreShop, width=192, height=590, bg='#f7f596')
CanevasCommande.create_line(0, 0, 0, 590, width=3)
# Texte Du prix total de la commande
TextePrixTotal = Label(CanevasCommande, font=('Arial', 15, 'bold'),
                       fg='#3f48cc', bg='#f7f596')
TextePrixTotal.place(x=96, y=205, anchor=CENTER)
# Bouton pour passer commande
Button(CanevasCommande, text='Passer commande', font='Georgia', cursor="star",
       bg='#98f796', command=lambda: passer_commande(prix_total)).place(x=96, y=255,
                                                                        anchor=CENTER)
# Importation des images pour la pagination
UnOn = PhotoImage(file='Pagination/1on.png')
UnOff = PhotoImage(file='Pagination/1off.png')
DeuxOn = PhotoImage(file='Pagination/2on.png')
DeuxOff = PhotoImage(file='Pagination/2off.png')
TroisOn = PhotoImage(file='Pagination/3on.png')
TroisOff = PhotoImage(file='Pagination/3off.png')
FlecheDroite = PhotoImage(file='Pagination/FlècheDroite.png')
FlecheGauche = PhotoImage(file='Pagination/FlècheGauche.png')

# Boutons pagination
BoutonFlecheGauche = Button(CanevasCommande, image=FlecheGauche, borderwidth=0,
                            highlightthickness=0, command=lambda: [actualise_panier(pagination - 1)])
BoutonFlecheGauche.place(x=20, y=550)
BoutonUn = Button(CanevasCommande, image=UnOn, borderwidth=0,
                  highlightthickness=0, cursor="star", command=lambda: [actualise_panier(1)])
BoutonUn.place(x=50, y=550)
BoutonDeux = Button(CanevasCommande, image=DeuxOff, borderwidth=0,
                    highlightthickness=0, cursor="star", command=lambda: [actualise_panier(2)])
BoutonDeux.place(x=80, y=550)
BoutonTrois = Button(CanevasCommande, image=TroisOff, borderwidth=0,
                     highlightthickness=0, cursor="star", command=lambda: [actualise_panier(3)])
BoutonTrois.place(x=110, y=550)
BoutonFlecheDroite = Button(CanevasCommande, image=FlecheDroite, borderwidth=0,
                            highlightthickness=0, command=lambda: [actualise_panier(pagination + 1)])
BoutonFlecheDroite.place(x=140, y=550)

# Liste des zone de dessin panier dans la fenêtre shop
ListeCanevas = [CanevasPanier, CanevasPanier2, CanevasPanier3, CanevasCommande]


def actualise_panier(fenetre):
    """ Prend comme paramètres le numéro de la page de CanevasPanier(page int)
    sur laquelle on veut modifier le design et afficher le panier client, avec
    ces achats, le prix total et de tel sorte qu'il puisse modifier la quantités
    de chache articles."""
    global pagination, prix_total
    # Initialise la valeur pagination pour le système de retour/suivant
    pagination = fenetre
    # Réinitialise la couleur des onglets et supprime les éléments indésirables
    clean_shop()
    # Modifie la couleur de l'onglet connection
    CanevasSign.config(bg='#98f796')
    BoutonPanier.config(image=image_panier2)
    TexteConnecte.config(bg='#98f796')
    # Place la zone de dessin de commande
    CanevasCommande.place(x=1095, y=108)
    # Modifie le titre de la fenêtre
    FenetreShop.title('Panier Client [ Filmanga ]')
    # Affiche le Canevas Panier en fonction de la fenetre + modifie la pagination
    if fenetre == 1:
        CanevasPanier.place(x=-2, y=108)
        BoutonUn.config(image=UnOn)
        BoutonDeux.config(image=DeuxOff)
        BoutonTrois.config(image=TroisOff)
        BoutonFlecheGauche.config(state=DISABLED, cursor="arrow")
        BoutonFlecheDroite.config(state=NORMAL, cursor="star")
    if fenetre == 2:
        CanevasPanier2.place(x=-2, y=108)
        BoutonDeux.config(image=DeuxOn)
        BoutonUn.config(image=UnOff)
        BoutonTrois.config(image=TroisOff)
        BoutonFlecheGauche.config(state=NORMAL, cursor="star")
        BoutonFlecheDroite.config(state=NORMAL, cursor="star")

    if fenetre == 3:
        CanevasPanier3.place(x=-2, y=108)
        BoutonTrois.config(image=TroisOn)
        BoutonUn.config(image=UnOff)
        BoutonDeux.config(image=DeuxOff)
        BoutonFlecheGauche.config(state=NORMAL, cursor="star")
        BoutonFlecheDroite.config(state=DISABLED, cursor="arrow")

    # Initialise la variable i qui permettra de bien placer les articles
    i = -1
    # Initialise la variable prix_total
    prix_total = 0.0
    for cle, valeur in Panier.items():
        if valeur > 0:
            i += 1
            # Définit la valeur du prix de l'article arrondi à 2 décimales
            prix_article = round(Articles[cle][2] * valeur, 2)
            if i <= 8 and fenetre == 1:
                # Texte du nom de l'article
                CanevasPanier.create_text((i // 3) * 370 + 150, (i % 3) * 200 + 25,
                                          text=Articles[cle][1], font=('Georgia', 13, 'bold'))
                # Image de l'article
                CanevasPanier.create_image((i // 3) * 370 + 150, (i % 3) * 200 + 112,
                                           image=ImagesPanier[cle])
                # Texte du prix de l'article
                CanevasPanier.create_text((i // 3) * 370 + 280, (i % 3) * 195 + 90,
                                          text=str(prix_article) + ' €', font=('Arial', 14, 'bold'),
                                          fill='#de74e0')
                # Texte quantité
                CanevasPanier.create_text((i // 3) * 370 + 278, (i % 3) * 195 + 136,
                                          text=valeur, fill='#31bbf7', font='bold')
                # Boutons pour ajuster la quantité
                BoutonMoins[cle].place(x=(i // 3) * 370 + 252, y=(i % 3) * 195 + 243,
                                       anchor=CENTER)
                exec('BoutonMoins[cle].config(command=lambda: moins_panier\
                (1,' + str(cle) + '))')
                BoutonPlus[cle].place(x=(i // 3) * 370 + 304, y=(i % 3) * 195 + 243,
                                      anchor=CENTER)
                exec('BoutonPlus[cle].config(command=lambda: plus_panier\
                (1,' + str(cle) + '))')

            if 9 <= i <= 17 and fenetre == 2:
                # Texte du nom de l'article
                CanevasPanier2.create_text(((i - 9) // 3) * 370 + 150, ((i - 9) % 3) * 200 + 25,
                                           text=Articles[cle][1], font=('Georgia', 13, 'bold'))
                # Création de l'image de l'article
                CanevasPanier2.create_image(((i - 9) // 3) * 370 + 150,
                                            ((i - 9) % 3) * 200 + 112, image=ImagesPanier[cle])
                # Texte du prix de l'article
                CanevasPanier2.create_text(((i - 9) // 3) * 370 + 280, ((i - 9) % 3) * 195 + 90,
                                           text=str(prix_article) + ' €', font=('Arial', 14, 'bold'),
                                           fill='#de74e0')
                # Texte quantité
                CanevasPanier2.create_text(((i - 9) // 3) * 370 + 278,
                                           ((i - 9) % 3) * 195 + 136, text=valeur, fill='#31bbf7', font='bold')
                # Boutons pour ajuster la quantité
                BoutonMoins[cle].place(x=((i - 9) // 3) * 370 + 252,
                                       y=((i - 9) % 3) * 195 + 243, anchor=CENTER)
                exec('BoutonMoins[cle].config(command=lambda: moins_panier\
                (2,' + str(cle) + '))')
                BoutonPlus[cle].place(x=((i - 9) // 3) * 370 + 304, y=((i - 9) % 3) * 195 + 243,
                                      anchor=CENTER)
                exec('BoutonPlus[cle].config(command=lambda: plus_panier\
                (2,' + str(cle) + '))')

            if i >= 18 and fenetre == 3:
                # Création du texte du nom de l'article
                CanevasPanier3.create_text(((i - 18) // 3) * 370 + 150,
                                           ((i - 18) % 3) * 200 + 25, text=Articles[cle][1],
                                           font=('Georgia', 13, 'bold'))
                # Image de l'article
                CanevasPanier3.create_image(((i - 18) // 3) * 370 + 150,
                                            ((i - 18) % 3) * 200 + 112, image=ImagesPanier[cle])
                # Texte du prix de l'article
                CanevasPanier3.create_text(((i - 18) // 3) * 370 + 280,
                                           ((i - 18) % 3) * 195 + 90, text=str(prix_article) + ' €',
                                           font=('Arial', 14, 'bold'), fill='#de74e0')
                # Texte quantité
                CanevasPanier3.create_text(((i - 18) // 3) * 370 + 278,
                                           ((i - 18) % 3) * 195 + 136, text=valeur, fill='#31bbf7', font='bold')
                # Boutons pour ajuster la quantité
                BoutonMoins[cle].place(x=((i - 18) // 3) * 370 + 252,
                                       y=((i - 18) % 3) * 195 + 243, anchor=CENTER)
                exec('BoutonMoins[cle].config(command=lambda: moins_panier\
                (3,' + str(cle) + '))')
                BoutonPlus[cle].place(x=((i - 18) // 3) * 370 + 304,
                                      y=((i - 18) % 3) * 195 + 243, anchor=CENTER)
                exec('BoutonPlus[cle].config(command=lambda: plus_panier\
                (3,' + str(cle) + '))')

            # Augmente la valeur du prix total
            prix_total += prix_article

    # Arondi la valeur du prix total à deux décimales
    prix_total = str(round(prix_total, 2))
    # Texte Prix total de la commande
    TextePrixTotal.config(text='Prix total :\n' + prix_total + ' €')


########################################## Fenêtre Shop, clean FenetreShop #############################################

def clean_shop():
    """ Permet de supprimer tous les éléments dans les Canevas Shop et Panier
    qui sont dans la FenetreShop.
    Modifie la couleur des onglets(Boutons) pour correspondre à la couleur
    initiale des boutons avant de les avoir cliqués dessus."""
    # Supprime tous les objets du Canevas Shop
    CanevasShop.delete(ALL)
    # Cache et supprime tous les éléments des zones de dessin Panier
    for Canevas in ListeCanevas:
        Canevas.place_forget()
        Canevas.delete(ALL)
    # Supprime les boutons "+", et "-" du panier et "ajouter au panier"
    for i in range(len(BoutonPlus)):
        BoutonPlus[i].place_forget()
        BoutonMoins[i].place_forget()
        BoutonAjouter[i].place_forget()

    # Réinitialise la couleur des onglets
    Film.config(bg='white')
    Manga.config(bg='white')
    FilmSci.config(fg='#31bbf7')
    MangaSurna.config(fg='#31bbf7')
    FilmCom.config(fg='#31bbf7')
    MangaSei.config(fg='#31bbf7')
    CanevasSign.config(bg="black")
    BoutonPanier.config(image=image_panier)
    TexteConnecte.config(bg='black')


########################################################################################################################
######################################## Fenêtre message de déconnexion ################################################

# fenetre de déconnexion
FenetreDeconnexion = Toplevel()
FenetreDeconnexion.resizable(False, False)
FenetreDeconnexion.title('Session expirée')
FenetreDeconnexion.config(width=500, height=175, bg='white')
# Cache la fenetre de déconnexion
FenetreDeconnexion.withdraw()

# Création d'une frame pour le titre
FrameDeconnexion = Frame(FenetreDeconnexion, width=500, height=40,
                         relief=FLAT, bg='#31bbf7')
FrameDeconnexion.place(x=0, y=0)
# Titre de la fenêtre
Label(FrameDeconnexion, text='Session expirée', bg='#31bbf7',
      font=('Times New Roman', 13, 'bold')).place(x=10, y=8)

# Texte d'inactivité
Label(FenetreDeconnexion, text="Vous allez être déconnecté dû à une \
inactivité trop longue. S'il vous plait choisissez\nde rester connecté \
parmi nous.\n\nAutrement, vous allez être déconnecté automatiquement \
dans", bg='white', justify=LEFT).place(x=250, y=83, anchor=CENTER)
# Texte compte à rebours
secondes_restantes = IntVar()
Label(FenetreDeconnexion, textvariable=secondes_restantes, bg='white',
      font=('Arial', 9, 'bold')).place(x=363, y=95)

# Bouton pour rester connecté
Button(FenetreDeconnexion, text='Restez Connecté !', bg='#31bbf7',
       fg='white', cursor="heart", font=('Verdana', 10),
       command=lambda: FenetreDeconnexion.withdraw()).place(x=125, y=145, anchor=CENTER)
# Bouton pour se déconnecter
Button(FenetreDeconnexion, text='Se déconnecter !', bg='#31bbf7',
       fg='white', cursor="pirate", font=('Verdana', 10),
       command=lambda: deconnexion()).place(x=375, y=145, anchor=CENTER)


########################################### Fenêtre Shop, Deconnexion ##################################################

def deconnexion():
    """Réinitialise la FenetreShop comme elle l'était initialement lorsque
    personne n'était connecté.
    Déconnecte l'utilisateur et le fais revenir sur la FenetreConnexion."""
    global Panier, nombre_articles
    # Supprime tous les éléments liés au compte client
    TexteConnecte.config(text="Vous ne\npouvez pas\nfaire d'achat\nsans compte")
    TexteConnecte.place(x=55, y=52, anchor=CENTER)
    TexteArticle.place_forget()
    BoutonPanier.place_forget()
    BoutonDeco.place_forget()
    BoutonChangerMdp.place_forget()
    BoutonSignIn.place(x=112, y=15)
    BoutonSignUp.place(x=112, y=60)
    Panier = {}
    nombre_articles = 0
    # Cache la fenetre shop
    FenetreShop.withdraw()
    # Cache la fenetre deconnexion
    FenetreDeconnexion.withdraw()
    # Affiche la fenêtre pour se connecter
    sign_in()
    # Modifie le CanevasShop
    film()


def compte_a_rebours():
    """Réalise un compte à rebours, défilant, de 20 secondes avant de
    déconnecter l'utilisateur."""
    # Calcule le temps écoulé depuis l'ouverture de la fenêtre deconnexion
    temps_ecoulee = time.time() - temps
    # Modifie la valeur de la variable secondes_restantes
    secondes_restantes.set(int(20 - temps_ecoulee))
    # deconnecte l'utilisateur quand il reste 0 seconde
    if secondes_restantes.get() == 0 and 'normal' == FenetreDeconnexion.state():
        deconnexion()
    else:
        FenetreDeconnexion.after(1000, compte_a_rebours)


def verification():
    """Vérifie si l'utilisateur a été inactif pendant 40 secondes étant encore
    connecté sur la fenêtre du shop. Si tel est le cas, envoie un message pour
    prévenir l'utilisateur de la deconnexion."""
    global temps
    if time.time() - last_time >= 40 and 'normal' == FenetreShop.state():
        # initialise le temps pour le compte à rebours
        temps = time.time()
        # Affiche la fenetre deconnexion
        FenetreDeconnexion.deiconify()
        # Lance le compte à rebours
        compte_a_rebours()


def mouvement(event):
    """Redéfinit le temps à chaque mouvement de souris, et au bout de 40
    secondes, si l'utilisateur est connecté à son compte client, appelle la
    fonction "verification"."""
    global last_time
    # Redéfinit last_time avec le temps au moment du mouvement de souris
    last_time = time.time()
    if BoutonPanier.winfo_ismapped() and 'normal' != FenetreDeconnexion.state():
        # Lance la fonction 'verification' au bout de 40 secondes
        FenetreShop.after(40000, verification)


FenetreShop.bind("<Motion>", mouvement)

########################################################################################################################
########################################### Fenêtre Connexion, Disign ##################################################
########################################################################################################################

# Affiche une longue bande son en largueur
Bande = PhotoImage(file='Design/Bande.png')
CanevasConnexion.create_image(260, 600, image=Bande)
CanevasConnexion.create_image(750, 600, image=Bande)
CanevasConnexion.create_image(1240, 600, image=Bande)
# Affiche une image de Mononoke Hime à partir
MononokeHime = PhotoImage(file='Design/PrincessMononoke.png')
CanevasConnexion.create_image(230, 260, image=MononokeHime)
# Affiche une image de Castle in the sky
Laputa = PhotoImage(file='Design/Laputa.png')
CanevasConnexion.create_image(1065, 266, image=Laputa)

# Création d'un bouton comme logo pour swap entre le site et le log
logo = PhotoImage(file='Design/Logo.png')
Button(FenetreConnexion, image=logo, borderwidth=0, highlightthickness=0,
       activebackground='white', cursor="heart",
       command=lambda: [FenetreConnexion.withdraw(),
                        FenetreShop.deiconify()]).place(x=644, y=90, anchor=CENTER)

####################################### Fichier contenant les idendifiants #############################################

# On lit le fichier CSV
FichierUtilisateurs = open('utilisateurs.csv', 'r')
Donnees = FichierUtilisateurs.read()
FichierUtilisateurs.close()
# Construction d'un tableau avec les données du fichier CSV
Tableau = Donnees.split('\n')
for i in range(len(Tableau)):
    Tableau[i] = Tableau[i].split(';')
# Construction d'un dictionnaire avec les données du fichier CSV
DicoUtilisateurs = {}
for i in Tableau:
    DicoUtilisateurs[i[0]] = i[1]

######################################### Fenêtre Connexion, Se connecter ##############################################

# zone de dessin pour l'espace log in/up
CanevasLog = Canvas(FenetreConnexion, width=340, height=335, bg='#31bbf7')
CanevasLog.place(x=473, y=180)

# Entrée pseudo
EntreePseudo = Entry(CanevasLog, width=27, font='Georgia')
# Entrée mot de passe
EntreeMdp = Entry(CanevasLog, width=27, font='Georgia', show="★")


def se_connecter():
    """ Permet à l'utilisateur de se connecter sur le site
    Retourne des messages d'erreurs adaptés si jamais l'utilisateur rencontre
    des problèmes pour se connecter."""
    global pseudo, nombre_articles, Panier
    # Récupère ce qu'il y avait dans les entrées
    pseudo = EntreePseudo.get()
    mdp = EntreeMdp.get()
    # Supprime ce qu'il y avait dans l'entrée mot de passe
    EntreePseudo.delete(0, END)
    EntreeMdp.delete(0, END)
    # Supprime le message d'erreur en réinitialisant la mise en page
    sign_in()

    # Affiche un texte si il n'y a pas de pseudo
    if pseudo == '':
        CanevasLog.create_text(32, 80, fill='red', anchor=NW,
                               text="⚠️ Entrez votre nom d'utilisateur")
    # Affiche un texte si le pseudo ne correspond à aucun compte existant
    elif pseudo not in DicoUtilisateurs:
        CanevasLog.create_text(32, 80, text="⚠️ Votre nom d'utilisateur ne \
semble correspondre\nà aucun compte existant", fill='red', anchor=NW)
    # Connecte l'utilisateur et met à jour son panier
    elif DicoUtilisateurs[pseudo] == mdp:
        Panier = DicoPaniers[pseudo]
        nombre_articles = 0
        for valeur in Panier.values():
            nombre_articles += valeur
        connexion()

    # Affiche l'utilisateur n'a pas entré de mdp
    elif mdp == '':
        EntreePseudo.insert(0, pseudo)
        CanevasLog.create_text(32, 180, fill='red', anchor=NW,
                               text='⚠️ Entrez votre mot de passe')
    # Affiche un texte si le mdp ne correspond pas au pseudo
    else:
        CanevasLog.create_text(32, 180, fill='red', anchor=NW,
                               text='⚠️ Mot de passe incorrect')
        # Affiche le nom d'utilisateur
        EntreePseudo.insert(0, pseudo)


# Création du bouton pour se connecter ou créer son compte
BoutonConnexion = Button(CanevasLog, pady=5, bg='#52a548', fg='white',
                         cursor="heart", font='Impact')

# Création d'un bouton pour revenir en arrière ou aller sur le site
BoutonRetour = Button(CanevasLog, pady=5, bg='#52a548', fg='white',
                      cursor="heart", font='Impact')

# Création du bouton swap pour swap entre se connecter et créer un compte
BoutonSwap = Button(CanevasLog, fg='white', bg='#31bbf7', font=('bold', 10),
                    activebackground='#31bbf7', borderwidth=0, highlightthickness=0, cursor="heart")

####################################### Fenêtre Connexion, Créer un compte #############################################

# Listes des lettres minuscules et majuscules
ListeMinusculeASCII = [x for x in range(97, 123)]
ListeMajusculeASCII = [x for x in range(65, 91)]


def creer_compte():
    """ Permet à l'utilisateur de se créer un compte sur le site.
    Retourne des messages d'erreurs adaptés si jamais l'utilisateur rencontre
    des problèmes pour se créer un compte."""
    global pseudo, nombre_articles, Panier
    # Récupère ce qu'il y avait dans les entrées
    pseudo = EntreePseudo.get()
    mdp = EntreeMdp.get()
    # Supprime ce qu'il y avait dans l'entrée mot de passe
    EntreePseudo.delete(0, END)
    EntreeMdp.delete(0, END)
    # Supprime les messages d'erreur
    sign_up()
    CanevasLog.delete(CriterePseudo)
    CanevasLog.delete(CritereMdp)

    # Initialisations des variables
    lettres_minuscule = 0
    lettres_majuscule = 0
    chiffres = 0
    # Test si le mdp comporte une lettre minuscule, majuscule et un chiffre
    for caractere in mdp:
        if ord(caractere) in ListeMinusculeASCII:
            lettres_minuscule = 1
        if ord(caractere) in ListeMajusculeASCII:
            lettres_majuscule = 1
        if caractere.isdigit():
            chiffres = 1

    # Affiche un texte si l'utilisateur a déjà un compte
    if pseudo in DicoUtilisateurs:
        CanevasLog.create_text(32, 80, text="⚠️ Ce nom d'utilisateur est \
déjà utilisé.\nVeuillez en choisir un autre.", fill='red', anchor=NW)
    # Affiche un texte si la taille du pseudo ne correspond pas au attente
    elif not 1 <= len(pseudo) <= 10:
        CanevasLog.create_text(32, 80, text="⚠️ Votre nom d'utilisateur doit \
comporter au moins\nun caractère et au maximum dix", fill='red', anchor=NW)

    # Affiche un texte si la taille du mdp ne correspond pas au attente
    elif not 3 <= len(mdp) <= 20:
        CanevasLog.create_text(32, 180, text='⚠️ Votre mot de passe \
doit comporter au moins\ntrois caractères et au maximum quinze caractères',
                               fill='red', anchor=NW)
        # Affiche le nom d'utilisateur
        EntreePseudo.insert(0, pseudo)
    # Affiche un texte si le mdp ne possède pas au moins une lettre minuscule
    elif lettres_minuscule < 1:
        CanevasLog.create_text(32, 180, fill='red', anchor=NW,
                               text='⚠️ Votre mot de passe doit comporter au moins\nune lettres minuscule')
        # Affiche le nom d'utilisateur
        EntreePseudo.insert(0, pseudo)
    # Affiche un texte si le mdp ne possède pas au moins une lettre majuscule
    elif lettres_majuscule < 1:
        CanevasLog.create_text(32, 180, fill='red', anchor=NW,
                               text='⚠️ Votre mot de passe doit comporter au moins\nune lettres majuscule')
        # Affiche le nom d'utilisateur
        EntreePseudo.insert(0, pseudo)
    # Affiche un texte si le mdp ne possède pas au moins un chiffre
    elif chiffres < 1:
        CanevasLog.create_text(32, 180, fill='red', anchor=NW,
                               text='⚠️ Votre mot de passe doit comporter au moins\nun chiffre')
        # Affiche le nom d'utilisateur
        EntreePseudo.insert(0, pseudo)

    # Ajoute les identifiants aux dictionnaires et connecte l'utilisateur
    else:
        DicoUtilisateurs[pseudo] = mdp
        Panier = {}
        for i in range(len(Articles)):
            Panier[i] = 0
        DicoPaniers[pseudo] = Panier
        nombre_articles = 0
        connexion()


################################## Fenêtre Connexion, Cacher/Afficher mot de passe #####################################

def show_password():
    """Quand on est sur la page sign in ou sign up.
    Cache ou Affiche en clair le mot de passe selon si la case (CaseVoirMdp)
    est cochée ou non."""
    # Affiche le mot de passe(1 = on), quand la case est cochée
    if off_on.get() == 1:
        EntreeMdp.config(show='')
        EntreeMdp2.config(show='')
    # Cache le mot de passe(0 = off), quand la case est décochée
    else:
        EntreeMdp.config(show='★')
        EntreeMdp2.config(show='★')


# Mémorise un entier
off_on = IntVar()
# Création d'une case à cocher pour voir/cacher le mot de passe
CaseVoirMdp = Checkbutton(CanevasLog, command=show_password, variable=off_on,
                          text='Afficher le mot de passe', bg='#31bbf7', activebackground='#31bbf7')

###################################### Fenêtre Connexion, Mot de passe oublié ##########################################

EntreeMdp2 = Entry(CanevasLog, width=27, font='Georgia', show="★")


def confirmer():
    """Vérifie si le nouveau mot de passe rempli les critères demandés. Si tel
    est le cas, remplace l'ancien mot de passe de l'utilisateur par le nouveau,
    entré par ce dernier. Puis affiche la page pour se connecter"""
    global page
    page = 1
    # Récupère ce qu'il y avait dans les entrées
    mdp1 = EntreeMdp2.get()
    mdp2 = EntreeMdp.get()
    # Supprime ce qu'il y avait dans les entrées
    EntreeMdp2.delete(0, END)
    EntreeMdp.delete(0, END)
    # Supprime les message d'erreur
    page_nouveau_mdp()
    CanevasLog.delete(CritereMdp1)

    # Initialisations des variables
    lettres_minuscule = 0
    lettres_majuscule = 0
    chiffres = 0
    # Test si le mdp comporte une lettre minuscule, majuscule et un chiffre
    for caractere in mdp1:
        if ord(caractere) in ListeMinusculeASCII:
            lettres_minuscule += 1
        if ord(caractere) in ListeMajusculeASCII:
            lettres_majuscule += 1
        if caractere.isdigit():
            chiffres += 1
    # Affiche un texte si la taille du mdp ne correspond pas au attente
    if not 3 <= len(mdp1) <= 20:
        CanevasLog.create_text(32, 80, text='⚠️ Votre mot de passe \
doit comporter au moins\ntrois caractères et au maximum quinze caractères',
                               fill='red', anchor=NW)
    # Affiche un texte si le mdp ne possède pas au moins une lettre minuscule
    elif lettres_minuscule < 1:
        CanevasLog.create_text(32, 80, fill='red', anchor=NW,
                               text='⚠️ Votre mot de passe doit comporter au moins\nune lettres minuscule')
    # Affiche un texte si le mdp ne possède pas au moins une lettre majuscule
    elif lettres_majuscule < 1:
        CanevasLog.create_text(32, 80, fill='red', anchor=NW,
                               text='⚠️ Votre mot de passe doit comporter au moins\nune lettres majuscule')
    # Affiche un texte si le mdp ne possède pas au moins un chiffre
    elif chiffres < 1:
        CanevasLog.create_text(32, 80, fill='red', anchor=NW,
                               text='⚠️ Votre mot de passe doit comporter au moins\nun chiffre')
    # Affiche un texte si le new mdp correspond déjà à l'ancien mdp
    elif DicoUtilisateurs[pseudo] == mdp1:
        CanevasLog.create_text(32, 80, fill='red', anchor=NW,
                               text='⚠️ Ce mot de passe correspond déjà à votre\nancien mot de passe')
    # Affiche un texte si les deux mdp ne correspondent pas
    elif mdp1 != mdp2:
        CanevasLog.create_text(32, 180, fill='red', anchor=NW,
                               text='⚠️ Les deux mots de passe ne correspondent pas')
        # Affiche le 1er mot de passe entré
        EntreeMdp2.insert(0, mdp1)
    # Modifie le mdp de l'utilisateur et le connecte
    else:
        DicoUtilisateurs[pseudo] = mdp1
        # Supprime tous les éléments du CanevasLog
        clean_connexion()
        # Modifie la valeur de off_on pour décocher la CaseVoirMdp
        off_on.set(0)
        CaseVoirMdp.deselect()
        show_password()
        # Sauvegarde le nouveau mdp
        sauvegarde_identifiants()
        # Texte certification du nouveau mot de passe + deconnexion
        CanevasLog.create_text(170, 160, text='Votre mot passe pour le compte ' + str(pseudo) +
                                              '\na bien été modifié\n\n' + str(pseudo) + ' : ' + str(mdp2),
                               font=('Georgia', 12, 'bold'), fill='#effc00', justify=CENTER)
        FenetreConnexion.after(6000, sign_in)


def page_nouveau_mdp():
    """ Modifie le CanevasLog pour que l'utilisateur puisse changer son mot de
    passe."""
    global CritereMdp1

    # Supprime tous les objets du Canevas Log
    CanevasLog.delete(ALL)
    # Cache l'entrée pseudo
    EntreePseudo.place_forget()

    # Textes et entrées des mdp
    CanevasLog.create_text(32, 23, text="Nouveau mot de passe",
                           font=('MV Boli', 12, 'bold'), anchor=NW)
    EntreeMdp2.place(x=32, y=50)
    CanevasLog.create_text(32, 123, text="Confirmation du mot de passe",
                           font=('MV Boli', 12, 'bold'), anchor=NW)
    EntreeMdp.place(x=32, y=150)
    # Texte critère mdp
    CritereMdp1 = CanevasLog.create_text(32, 80, text="Utilisez au moins trois \
caractères avec des lettres\nminuscules, majuscules et des chiffres", anchor=NW,
                                         fill='#002ee8')
    # Place la case à cocher pour afficher le mot de passe
    CaseVoirMdp.place(x=32, y=220)
    # Modifie les boutons retour et connexion
    BoutonRetour.config(text="Retour", command=mdp_oublie)
    BoutonConnexion.config(text="Confirmer", command=confirmer, padx=50)


def continuer():
    """ Vérifie si le pseudo entré par l'utilisateur correspond bien à un compte
    existant. Si c'est le cas, lance la fonction 'page_nouveau_mdp' qui
    modifiera le CanevasLog pour que l'utilisateur puisse changer son mot de
    passe."""
    global pseudo
    # Récupère le pseudo entré
    pseudo = EntreePseudo.get()
    # Supprime ce qu'il y avait dans l'entrée pseudo
    EntreePseudo.delete(0, END)
    # Supprime le message d'erreur en réinitialisant la mise en page
    mdp_oublie()

    # Affiche un texte si le pseudo ne correspond à aucun compte existant
    if pseudo not in DicoUtilisateurs:
        CanevasLog.create_text(32, 203, text="⚠️ Votre nom d'utilisateur ne \
semble correspondre\nà aucun compte existant", anchor=NW, fill='red')
    else:
        # Affiche la page pour pouvoir modifier son mdp
        page_nouveau_mdp()


def mdp_oublie():
    """ Modifie le CanevasLog pour que l'utilisateur puisse entrer son pseudo
    et par la suite changer son mot de passe."""
    # Supprime tous les objets du Canevas Log
    CanevasLog.delete(ALL)
    # Cache l'entrée mdp
    EntreeMdp2.place_forget()

    # Cache l'entrée mot de passe
    EntreeMdp.place_forget()
    EntreeMdp.delete(0, END)
    # Modifie les boutons retour, connexion et mdp oublié
    BoutonConnexion.config(text="Continuer", command=continuer, padx=50)
    if page == 1:
        BoutonRetour.config(text='Retour', command=sign_in, padx=56)
        BoutonMdpOublie.config(text="Déjà enregistré ?", command=sign_in)
    else:
        BoutonRetour.config(text='Retour', command=sign_up, padx=56)
        BoutonMdpOublie.config(text="Nouveau sur Filmanga ?", command=sign_up)

    # Titre "Mot de passe oublié ?"
    CanevasLog.create_text(170, 40, text="Mot de passe oublié ?",
                           font=('MV Boli', 18, 'bold'))
    # Place le texte pour l'explication
    CanevasLog.create_text(170, 100, text="Veuillez entrer votre nom \
d'utilisateur. Nous allons\nvous envoyer un mail pour obtenir un nouveau\nmot \
de passe d'ici quelques secondes.", fill='#effc00', font=('Times New Roman', 11),
                           justify=CENTER)

    # Texte et entrée pour le pseudo
    CanevasLog.create_text(32, 145, text="Nom d'utilisateur",
                           font=('MV Boli', 12, 'bold'), anchor=NW)
    EntreePseudo.place(x=32, y=172)
    # Cache la case à cocher pour afficher le mot de passe
    CaseVoirMdp.place_forget()
    # Modifie la valeur de off_on pour décocher la CaseVoirMdp
    off_on.set(0)
    CaseVoirMdp.deselect()
    show_password()


# Création du bouton pour récupérer ou changer son mot de passe
BoutonMdpOublie = Button(CanevasLog, fg='white', bg='#31bbf7', font=('bold', 10),
                         activebackground='#31bbf7', relief=FLAT, borderwidth=0, highlightthickness=0,
                         cursor="heart")

# Design de la fenêtre connexion pour pouvoir se connecter
sign_in()

######################################### Fenêtre Connexion, clean CanevasLog ##########################################

# Liste contenant tous les boutons et entree du CanevasLog
Objets = [BoutonRetour, BoutonConnexion, BoutonMdpOublie, BoutonSwap,
          EntreeMdp, EntreeMdp2, EntreePseudo, CaseVoirMdp]


def clean_connexion():
    """ Permet de supprimer tous les éléments dans le CanevasLog qui sont dans
    la FenetreConnection."""
    # Supprime tous les objets du CanevasLog
    CanevasLog.delete(ALL)
    # Supprime tous les éléments restant du CanevasLog
    for objet in Objets:
        objet.place_forget()


########################################## Sauvegardes dans un fichier CSV #############################################

def sauvegarde_identifiants():
    """ Réalise une sauvegarde des identifiants(dico) dans un fichier CSV."""
    # Construction d'un tableau à partir du DicoUtilisateurs
    Tableau2 = ''
    for cle, valeur in DicoUtilisateurs.items():
        Tableau2 = Tableau2 + str(cle) + ';' + str(valeur) + '\n'
    Tableau2 = Tableau2[0:len(Tableau2) - 1]
    # Sauvegarde le tableau des identifiants dans un fichier CSV
    fichier_utilisateurs2 = open('utilisateurs.csv', 'w')
    fichier_utilisateurs2.write(Tableau2)
    fichier_utilisateurs2.close()


def sauvegarde_panier():
    """ Réalise une sauvegarde du panier client(dico) dans un fichier CSV."""
    # Sauvegarde le panier à partir du DicoPaniers
    File = open('paniers.csv', 'w')
    for item in DicoPaniers.items():
        File.write(item[0])
        for number in item[1].values():
            File.write(';' + str(number))
        File.write('\n')
    File.close()


# Liste contenant les 5 images du décompte
ImagesCountDown = ['CountDown/5.png', 'CountDown/4.png', 'CountDown/3.png',
                   'CountDown/2.png', 'CountDown/1.png']


########################### Affiche la fenêtre shop avec un compte utilisateur enregistré ##############################

def connexion():
    """ Réalise une sauvegarde des identifiants(dico) dans un fichier CSV et une
    sauvegarde du panier client.
    Réalise un compte à rebours(Canvas) et un message de bienvenue avant de
    fermer la fenêtre de connexion(tkinter) et d'ouvrir la fenetre shop(tkinter)
    du site en ayant connecté la personne."""
    global last_time
    sauvegarde_identifiants()
    sauvegarde_panier()
    # Supprime tous les éléments du CanevasLog
    clean_connexion()

    # Texte de bienvenue
    if page == 1:
        CanevasLog.create_text(165, 155, text="Bon retour parmi nous :D\n\n\n\n\
Annonce du jour :\n\nMalheureusement tous les mangas\nsont en rupture de \
stock", font=('Georgia', 12, 'bold'), justify=CENTER, fill='#effc00')
    else:
        CanevasLog.create_text(165, 165, text="Je vous remercie d'avoir créé\n\
un compte chez Filmanga.\n\n\n\nAnnonce du jour :\n\nMalheureusement tous les \
mangas\nsont en rupture de stock", font=('Georgia', 12, 'bold'), justify=CENTER,
                               fill='#effc00')

    # Initialise la variable i
    a = 0
    # Parcours les images une à une et les affiches 1 par 1 comme un décompte
    for image in ImagesCountDown:
        image_decompte = PhotoImage(file=image)
        CanevasConnexion.create_image(447 + a, 600, image=image_decompte)
        # Update la fenêtre connexion et met en pause le programme pendant 1sec
        FenetreConnexion.update()
        time.sleep(1)
        # Augment la variable i pour décaler de 3 crans les images
        a += 99

    # Cache la fenetre connexion
    FenetreConnexion.withdraw()
    # Affiche la fenetre shop
    FenetreShop.deiconify()
    # Modifie la valeur de off_on pour décocher la CaseVoirMdp
    off_on.set(0)
    CaseVoirMdp.deselect()
    show_password()
    # Place le texte avec le pseudo
    TexteConnecte.config(text=pseudo)
    TexteConnecte.place(x=45, y=18, anchor=CENTER)
    # Place le panier d'achat et le texte
    BoutonPanier.place(x=15, y=30)
    TexteArticle.config(text=nombre_articles)
    TexteArticle.place(x=66, y=45, anchor=CENTER)
    # Cache les deux bouton sign up/sign in
    BoutonSignIn.place_forget()
    BoutonSignUp.place_forget()

    # Bouton déconnexion et changer mdp
    BoutonDeco.place(x=92, y=15)
    BoutonChangerMdp.place(x=92, y=60)
    # Affiche la page film
    film()
    # Lance la fonction 'verification' pour vérifier l'inactivité
    last_time = time.time()
    FenetreShop.after(40000, verification)


FenetreShop.mainloop()
