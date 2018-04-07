import variables, classvar
from Battle import Battle
from pygame import Rect
from play_sound import stop_music, stop_effect

def initiatebattle(enemy):
    variables.settings.state = "battle"
    classvar.player.change_of_state()
    enemy.sethealth()
    classvar.player.heal()
    classvar.battle = Battle(enemy)

    variables.dirtyrects = [Rect(0,0,variables.width,variables.height)]
    stop_effect()
    stop_music()
    
