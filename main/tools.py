import datetime as __dt

__year = __dt.date.today()
__to = int(__year.strftime("%Y"))

def url(lang : str ="int", years : str =f"{__to}{__to+1}", country : str =None, league : str =None) :

    return f"https://{lang}.soccerway.com/national/{country}/{league}/{years}/regular-season/tables/"