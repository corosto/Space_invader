import game
import main_menu
from music import Music


g = game.Game()  # stworzenie obiektu gry
mm = main_menu.MainMenu()  # stworzenie obiektu menu

Music.play()  # włączenie muzyki
mm.main_menu()  # jak włączy się program to pokaże się główne menu
