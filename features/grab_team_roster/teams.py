class Team:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Teams:
    def __init__(self):
        self.boston_celtics = Team("Boston Celtics", "1610612738")
        self.brooklyn_nets = Team("Brooklyn Nets", "1610612751")
        self.new_york_knicks = Team("New York Knicks", "1610612752")
        self.philadelphia_76ers = Team("Philadelphia 76ers", "1610612755")
        self.toronto_raptors = Team("Toronto Raptors", "1610612761")
        self.denver_nuggets = Team("Denver Nuggets", "1610612743")
        self.minnesota_timberwolves = Team(
            "Minnesota Timberwolves", "1610612750"
        )
        self.oklahoma_city_thunder = Team(
            "Oklahoma City Thunder", "1610612760"
        )
        self.portland_trail_blazers = Team(
            "Portland Trail Blazers", "1610612757"
        )
        self.utah_jazz = Team("Utah Jazz", "1610612762")
        self.chicago_bulls = Team("Chicago Bulls", "1610612741")
        self.cleveland_cavaliers = Team("Cleveland Cavaliers", "1610612739")
        self.detroit_pistons = Team("Detroit Pistons", "1610612765")
        self.indiana_pacers = Team("Indiana Pacers", "1610612754")
        self.milwaukee_bucks = Team("Milwaukee Bucks", "1610612749")
        self.golden_state_warriors = Team(
            "Golden State Warriors", "1610612744"
        )
        self.la_clippers = Team("LA Clippers", "1610612746")
        self.los_angeles_lakers = Team("Los Angeles Lakers", "1610612747")
        self.phoenix_suns = Team("Phoenix Suns", "1610612756")
        self.sacramento_kings = Team("Sacramento Kings", "1610612758")
        self.atlanta_hawks = Team("Atlanta Hawks", "1610612737")
        self.charlotte_hornets = Team("Charlotte Hornets", "1610612766")
        self.miami_heat = Team("Miami Heat", "1610612748")
        self.orlando_magic = Team("Orlando Magic", "1610612753")
        self.washington_wizards = Team("Washington Wizards", "1610612764")
        self.dallas_mavericks = Team("Dallas Mavericks", "1610612742")
        self.houston_rockets = Team("Houston Rockets", "1610612745")
        self.memphis_grizzlies = Team("Memphis Grizzlies", "1610612763")
        self.new_orleans_pelicans = Team("New Orleans Pelicans", "1610612740")
        self.san_antonio_spurs = Team("San Antonio Spurs", "1610612759")


teams = Teams()
