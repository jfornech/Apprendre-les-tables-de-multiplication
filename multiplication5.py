# coding: utf8
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GObject
from gi.repository import GdkPixbuf
import random
from time import gmtime, strftime
import math


class Multiplication(Gtk.Window):
    def __init__(self):

        self.angle1 = 0
        self.angle2 = 0

        self.gladefile = "fenetre3.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)

        self.cssProvider = Gtk.CssProvider()
        self.cssProvider.load_from_path('style.css')
        self.screen = Gdk.Screen.get_default()
        self.styleContext = Gtk.StyleContext()
        self.styleContext.add_provider_for_screen(self.screen, self.cssProvider, Gtk.STYLE_PROVIDER_PRIORITY_USER)

        # objet GTK
        self.window = self.builder.get_object("window1")
        self.window_table = self.builder.get_object("window2")
        self.window_bravo = self.builder.get_object("window3")
        self.window_table_revision = self.builder.get_object("window4")

        self.fixed = self.builder.get_object("fixed")


        self.q_image1 = self.builder.get_object("image1")
        self.q_image2 = self.builder.get_object("image2")
        self.image_bravo = self.builder.get_object("image3")

        self.combo_table = self.builder.get_object("combo_table")
        self.combo_temps = self.builder.get_object("combobox_temps")
        self.test = int(self.combo_temps.get_active_text())
        self.tps_question = self.test * 5
        self.table = self.builder.get_object("comboboxtext1")
        self.bouton_lancer = self.builder.get_object("bouton_lancer")
        self.bouton_quitter = self.builder.get_object("bouton_quitter")
        self.bouton1 = self.builder.get_object("button_reponse1")
        self.bouton1.set_label("")
        self.bouton2 = self.builder.get_object("button_reponse2")
        self.bouton2.set_label("")
        self.bouton3 = self.builder.get_object("button_reponse3")
        self.bouton3.set_label("")
        self.label1 = self.builder.get_object("label1")
        self.label2 = self.builder.get_object("label2")
        self.label_bravo = self.builder.get_object("label_bravo")

        self.label_table_titre = self.builder.get_object("label_table_titre")
        self.label_table_0 = self.builder.get_object("label_table_0")
        self.label_table_1 = self.builder.get_object("label_table_1")
        self.label_table_2 = self.builder.get_object("label_table_2")
        self.label_table_3 = self.builder.get_object("label_table_3")
        self.label_table_4 = self.builder.get_object("label_table_4")
        self.label_table_5 = self.builder.get_object("label_table_5")
        self.label_table_6 = self.builder.get_object("label_table_6")
        self.label_table_7 = self.builder.get_object("label_table_7")
        self.label_table_8 = self.builder.get_object("label_table_8")
        self.label_table_9 = self.builder.get_object("label_table_9")
        self.label_table_10 = self.builder.get_object("label_table_10")

        self.label_table_multiplicateur_0 = self.builder.get_object("label_table_multiplicateur_0")
        self.label_table_multiplicateur_1 = self.builder.get_object("label_table_multiplicateur_1")
        self.label_table_multiplicateur_2 = self.builder.get_object("label_table_multiplicateur_2")
        self.label_table_multiplicateur_3 = self.builder.get_object("label_table_multiplicateur_3")
        self.label_table_multiplicateur_4 = self.builder.get_object("label_table_multiplicateur_4")
        self.label_table_multiplicateur_5 = self.builder.get_object("label_table_multiplicateur_5")
        self.label_table_multiplicateur_6 = self.builder.get_object("label_table_multiplicateur_6")
        self.label_table_multiplicateur_7 = self.builder.get_object("label_table_multiplicateur_7")
        self.label_table_multiplicateur_8 = self.builder.get_object("label_table_multiplicateur_8")
        self.label_table_multiplicateur_9 = self.builder.get_object("label_table_multiplicateur_9")
        self.label_table_multiplicateur_10 = self.builder.get_object("label_table_multiplicateur_10")

        self.label_resultat_0 = self.builder.get_object("label_table_resultat_0")
        self.label_resultat_1 = self.builder.get_object("label_table_resultat_1")
        self.label_resultat_2 = self.builder.get_object("label_table_resultat_2")
        self.label_resultat_3 = self.builder.get_object("label_table_resultat_3")
        self.label_resultat_4 = self.builder.get_object("label_table_resultat_4")
        self.label_resultat_5 = self.builder.get_object("label_table_resultat_5")
        self.label_resultat_6 = self.builder.get_object("label_table_resultat_6")
        self.label_resultat_7 = self.builder.get_object("label_table_resultat_7")
        self.label_resultat_8 = self.builder.get_object("label_table_resultat_8")
        self.label_resultat_9 = self.builder.get_object("label_table_resultat_9")
        self.label_resultat_10 = self.builder.get_object("label_table_resultat_10")

        self.bouton1.set_sensitive(False)
        self.bouton2.set_sensitive(False)
        self.bouton3.set_sensitive(False)

        self.progressbar1 = self.builder.get_object("progressbar1")
        self.progressbar1.hide()

        # Gestion des images
        self.image0 = 'images-0.png'
        self.image1 = 'images-1.png'
        self.image2 = 'images-2.png'
        self.image3 = 'images-3.png'
        self.image4 = 'images-4.png'
        self.image5 = 'images-5.png'
        self.image6 = 'images-6.png'
        self.image7 = 'images-7.png'
        self.image8 = 'images-8.png'
        self.image9 = 'images-9.png'
        self.image10 = 'images-10.png'

        self.img = GdkPixbuf.Pixbuf.new_from_file('images-init.png')
        self.q_image1.set_from_pixbuf(self.img)
        self.q_image2.set_from_pixbuf(self.img)



        self.window.show()

        self.list_reponse = []
        self.list_reponse_fausse = []
        self.list_multiplicateur = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

        self.dico_reponse = {'0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [],
                             '10': []}

        self.list_test_table = ['1']  # Choix de la table sélectionnée
        # question_en_cours= []
        self.compteur_question = 0
        self.question_posee = 0
        self.nombre_de_question = 5
        self.reponse_juste = 0
        self.reponse_fausse = 0

    def on_window1_destroy(self, *args):
        Gtk.main_quit(*args)

    def on_button_table_fermer_clicked(self, *args):
        global time_out
        self.window_table.hide()
        self.on_timeout(True)

    def on_quitter_clicked(self, *args):
        Gtk.main_quit(*args)

    def on_afficher_table_Clicked(self, *args):
        self.affiche_table()

    def on_button_bravo_clicked(self, *args):
        self.window_bravo.hide()

    def lancer_clicked(self, button):
        global time_out
        self.questionnaire(self.list_test_table[0])
        self.label1.set_text("")
        self.bouton_lancer.set_sensitive(False)
        self.bouton_quitter.set_sensitive(False)
        self.table.set_sensitive(False)
        self.combo_temps.set_sensitive(False)
        self.bouton1.show()
        self.bouton2.show()
        self.bouton3.show()
        self.bouton1.set_sensitive(True)
        self.bouton2.set_sensitive(True)
        self.bouton3.set_sensitive(True)
        self.progressbar1.show()
        self.time_out = GObject.timeout_add(int(self.tps_question), self.on_timeout, )
        print (int(self.tps_question)/10)
        self.test1 = GObject.timeout_add(100, self.move1)  # call every min
        self.test2 = GObject.timeout_add(100, self.move2)  # call every min

    def reponse1_clicked(self, button):
        t = self.question_en_cours[0]
        m = self.question_en_cours[1]
        rep1 = button.get_label()
        self.reponse(table=t, multiplicateur=m, reponse=rep1)
        self.questionnaire(self.list_test_table[0])
        self.progressbar1.set_fraction(0.0)

    def reponse2_clicked(self, button):
        t = self.question_en_cours[0]
        m = self.question_en_cours[1]
        rep1 = button.get_label()
        self.reponse(table=t, multiplicateur=m, reponse=rep1)
        self.questionnaire(self.list_test_table[0])
        self.progressbar1.set_fraction(0.0)

    def reponse3_clicked(self, button):
        t = self.question_en_cours[0]
        m = self.question_en_cours[1]
        rep1 = button.get_label()
        self.reponse(table=t, multiplicateur=m, reponse=rep1)
        self.questionnaire(self.list_test_table[0])
        self.progressbar1.set_fraction(0.0)

    def table_change(self, button):
        for a in self.table.get_active_text():
            self.list_test_table = []
            self.list_test_table.append(a)

    def on_combobox_temps_changed(self, button):
        self.tps_question = button.get_active_text()

    def change_image(self, tableau):

        a = random.randrange(start=0, stop=2)

        self.image_a = tableau[a]
        if a == 1:
            self.image_b = tableau[0]
        if a == 0:
            self.image_b = tableau[1]

        self.imga = GdkPixbuf.Pixbuf.new_from_file('images-' + str(self.image_a) + '.png')
        self.imgb = GdkPixbuf.Pixbuf.new_from_file('images-' + str(self.image_b) + '.png')

        self.q_image1.set_from_pixbuf(self.imga)
        self.q_image2.set_from_pixbuf(self.imgb)

    def reponse(self, table, multiplicateur, reponse):
        m = int(multiplicateur)
        t = int(table)
        r = int(reponse)
        original_list = self.dico_reponse.get(m)
        new_list = []
        if original_list is None:
            new_list.append(self.verification(table=int(t), multiplicateur=int(m), reponse=int(r)))
            self.dico_reponse[str(m)] = new_list
        else:
            for item in original_list:
                new_list.append(item)
                new_list.append(self.verification(table=int(t), multiplicateur=int(m), reponse=int(r)))
            self.dico_reponse[str(m)] = new_list

    def date_heure(self):
        a = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        return a

    def affiche_table(self):
        t1 = self.table.get_active_text()
        t1.split()
        t = t1[-1]

        self.label_table_titre.set_markup("<big><big>Table de " + str(t) + "</big></big>")
        for a in range(0, 11):
            b = int(t) * a

            # exec('global label_table_multiplicateur_' + str(a))
            # exec('global label_table_' + str(a))
            # exec('global label_resultat_' + str(a))
            exec('self.label_table_multiplicateur_' + str(a) + '.set_markup("<big><b>{}</b></big>".format(' + str(
                a) + '))')
            exec('self.label_table_' + str(a) + '.set_markup("<big><b>{}</b></big>".format(' + str(t) + '))')
            exec('self.label_resultat_' + str(a) + '.set_markup("<big><b>{}</b></big>".format(' + str(b) + '))')

        self.window_table.show()

    def multiplicateur(self):

        self.question_posee += 1
        result = self.list_multiplicateur[-1]
        #print(result)
        return result

    def verification(self, table, multiplicateur, reponse):
        print (str(table) + " x " + str(multiplicateur) + " = " +str(reponse))
        if table * multiplicateur == reponse:
            self.label1.set_text("OK")
            self.reponse_juste += 1
            self.list_multiplicateur.pop()
            print("Juste")
            print(self.list_multiplicateur)
            random.shuffle(self.list_multiplicateur)  # mélange la liste
            return "OK"

        else:
            self.bonne_reponse = table * multiplicateur
            self.label1.set_markup(
                "<big>Attention : {} x {} = <b>{}</b></big>".format(table, multiplicateur, self.bonne_reponse))
            self.list_reponse_fausse.append(multiplicateur)

            # incrémente le compteur des réponses fausses
            self.reponse_fausse += 1

            # Reactive le multiplicateur en cas de faute
            self.list_multiplicateur.append(multiplicateur)
            self.question_posee -= 1

            print (self.list_multiplicateur)
            random.shuffle(self.list_multiplicateur)  # mélange la liste
            print("Faux")
            return "Faux"

    def reponse_temps_ecoule(self):
        '''
        Repose les questions utiniquement sur les fautes réalisées
        '''
        t = self.question_en_cours[0]
        m = self.question_en_cours[1]
        self.reponse(table=t, multiplicateur=m, reponse=99)
        self.questionnaire(self.list_test_table[0])
        self.progressbar1.set_fraction(0.0)

    def question(self, table, multiplicateur):
        '''
        Pose les questions de 0 à 10 pour la table de multiplication sélectionnées
        :param table:
        :param multiplicateur:
        :return:
        '''
        t = table  # Table
        m = multiplicateur
        # q = str(table) + ' x ' + str(m)  # Formatage de la question


        self.question_en_cours = []
        self.question_en_cours.append(table)
        self.question_en_cours.append(m)
        self.change_image(self.question_en_cours)

        # Genére l'erreur la plus probable,
        # soit sur le multiplicateur soit sur la table (+/- 1)
        lst = [1, -1, 0]  # (+/- 1)
        erreur_table_ou_multiplicateur = [0, 1]  # soit sur le multiplicateur, soit sur la table
        random.shuffle(erreur_table_ou_multiplicateur)  # mélange la liste
        random.shuffle(lst)  # mélange la liste

        if erreur_table_ou_multiplicateur[0] == 0:
            self.reponse1 = int(t) * (int(m) + lst[0])
            self.reponse2 = int(t) * (int(m) + lst[1])
            self.reponse3 = int(t) * (int(m) + lst[2])

        else:
            self.reponse1 = int(m) * (int(t) + lst[0])
            self.reponse2 = int(m) * (int(t) + lst[1])
            self.reponse3 = int(m) * (int(t) + lst[2])

        self.bouton1.set_label(str(self.reponse1))
        self.bouton2.set_label(str(self.reponse2))
        self.bouton3.set_label(str(self.reponse3))

    def on_timeout(self, q=True):
        """
        Update value on the progress bar
        """

        data = self.progressbar1.get_fraction()
        old_time = GObject.get_current_time()
        time = GObject.get_current_time()

        if q is True:
            if data < 1 and int(self.compteur_question) < int(self.nombre_de_question):
                self.progressbar1.set_fraction(self.progressbar1.get_fraction() + 0.005)

            elif data == 1 and int(self.compteur_question) < int(self.nombre_de_question):
                self.reponse_temps_ecoule()

            elif self.compteur_question == 0 and self.nombre_de_question == 0 and len(self.list_reponse_fausse) == 0:
                self.progressbar1.set_fraction(0)
                self.fin()
            return True
        elif q is False:
            return False

    def questionnaire(self, table):

        self.nombre_de_question = len(self.list_multiplicateur)
        #self.label2.set_text( "Erreurs : " + str(len(self.list_reponse_fausse)) + "    " + str(self.compteur_question) + "/" + str(self.nombre_de_question))

        # Pose une série de questions
        #if self.compteur_question < self.nombre_de_question:
        if len(self.list_multiplicateur) > 0:
            self.question(table, self.multiplicateur())
            #self.compteur_question += 1

        # Travail des erreurs

        # elif int(len(self.list_reponse_fausse)) > 0:
        #
        #     self.label2.set_markup("<span foreground='red' size='large'>Travail des fautes </span>")
        #     self.question(table, self.list_reponse_fausse[-1])
        #     self.list_reponse_fausse.pop()

        # Affiche les résultats
        else:
            GObject.source_remove(self.test1)
            GObject.source_remove(self.test2)
            GObject.source_remove(self.time_out)
            self.fin()

    def affiche_table_revision(self):
        global reponse_fausse
        t1 = self.table.get_active_text()
        t1.split()
        t = t1[-1]
        self.label_table_titre.set_markup("<big><big>Révision table de " + str(t) + "</big></big>")
        for a in self.list_reponse_fausse:
            b = int(t) * a
            exec('self.label_table_multiplicateur_' + str(a) + '.set_markup("<big><b>{}</b></big>".format(' + str(
                a) + '))')
            exec('self.label_table_' + str(a) + '.set_markup("<big><b>{}</b></big>".format(' + str(t) + '))')
            exec('self.label_resultat_' + str(a) + '.set_markup("<big><b>{}</b></big>".format(' + str(b) + '))')

        self.window_table.show()

    def fin(self):
        self.img = GdkPixbuf.Pixbuf.new_from_file('images-init.png')

        self.q_image1.set_from_pixbuf(self.img)
        self.q_image2.set_from_pixbuf(self.img)

        question_en_cours = []

        fautes = self.reponse_fausse

        self.bouton_lancer.set_sensitive(True)
        self.table.set_sensitive(True)
        self.combo_temps.set_sensitive(True)
        self.bouton1.set_sensitive(False)
        self.bouton2.set_sensitive(False)
        self.bouton3.set_sensitive(False)

        if fautes == 0:
            self.img = GdkPixbuf.Pixbuf.new_from_file('Cute-Hamster-1.jpg')
            self.image_bravo.set_from_pixbuf(self.img)
            self.label_bravo.set_markup("<span foreground='green' size='x-large'><b>Bravo ! 0 faute </b></span>")
            self.window_bravo.show()
        elif fautes == 1:
            self.img = GdkPixbuf.Pixbuf.new_from_file('marmotte.jpg')
            self.image_bravo.set_from_pixbuf(self.img)
            self.label_bravo.set_markup("<span foreground='orange' size='x-large'>1 seule faute, c'est bien !</span>")
            self.window_bravo.show()

        elif fautes == 2:
            self.img = GdkPixbuf.Pixbuf.new_from_file('mouche.png')
            self.image_bravo.set_from_pixbuf(self.img)
            self.label_bravo.set_markup("<span foreground='orange' size='x-large'>2 fautes, c'est moyen ...</span>")
            self.window_bravo.show()

        elif fautes == 3:
            self.img = GdkPixbuf.Pixbuf.new_from_file('chameau.png')
            self.image_bravo.set_from_pixbuf(self.img)
            self.label_bravo.set_markup("<span foreground='orange' size='x-large'>3 fautes ...</span>")
            self.window_bravo.show()

        else:
            self.q_image1.clear()
            self.q_image2.clear()
            self.label1.set_markup("<span foreground='red' size='x-large'>" + str(fautes) + " fautes </span>")

        self.bouton1.hide()
        self.bouton2.hide()
        self.bouton3.hide()
        self.bouton_quitter.set_sensitive(True)
        self.progressbar1.hide()
        self.compteur_question = 0
        self.question_posee = 0
        self.nombre_de_question = 0
        self.reponse_juste = 0
        self.list_reponse_fausse = []
        self.list_multiplicateur = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def move1(self ):
        self.centre = 100
        self.rayon = 65

        self.x = self.centre + (math.cos(self.angle1) * self.rayon)
        self.y = self.centre + (math.sin(self.angle1) * self.rayon)
        self.angle1= self.angle1 + 0.05

        if self.angle1 == 360 :
            self.angle1 = 0

        #print ("x1: "+ str(self.x) + " y1: "+ str(self.y) + " a1: "+ str(self.angle1) )
        self.fixed.move(self.q_image1, self.x, self.y)

        return self.x

    def move2(self ):
        self.centre = 100
        self.rayon = -65

        self.x = self.centre + (math.cos(self.angle2) * self.rayon)
        self.y = self.centre + (math.sin(self.angle2) * self.rayon)
        self.angle2= self.angle2 + 0.05
        if self.angle2 == 360 :
            self.angle2 = 0

        #print ("x2: "+ str(self.x) + " y2: "+ str(self.y) + " a2: "+ str(self.angle2) )
        self.fixed.move(self.q_image2, self.x, self.y)

        return self.x

def main():
    # Enter the event loop
    Gtk.main()
    return 0

if __name__ == '__main__':
    test = Multiplication()


    main()
