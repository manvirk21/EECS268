from boardgames import BoardGame

# This is the start of the Executive class that will work directly with the file.
class Executive:
    def __init__(self, filename):
        self.filename = filename

    def build(self):
        global games
        games = []
        for value in self.filename:
            value = value.strip().split("\t")
            game = BoardGame(value[0], int(value[1]), float(value[2]), float(value[3]), int(value[4]), int(value[5]))
            games.append(game)
        return games
#This builds the list of all the board game objects.

    def run(self):
        self.build()
        choice = 0
        while choice != 6:
            print("\nWhat would you like to do? \n1. Print all games \n2. Print all games from a year \n3. Print a "
                  "ranking range \n4. The People VS Dr. Gibbons \n5. Print based on play time \n6. Exit the program \n")
            choice = int(input("Enter your choice number: "))
            if choice == 1: #This will print all the games in the file formatted nicely.
                for game in games:
                    print(f"{game.name} ({game.year}) [GR={game.gibrating}, PR={game.pubrating}, MP={game.minplayer}, "
                          f"MT={game.playtime}]")
            if choice == 2: #This choice will look up a year and print all the games in that year.
                count = 0
                try:
                    game_year = int(input("What year do you want to look up? "))
                    for game in games:
                        if game_year == game.year:
                            print(f'{game.name} ({game.year}) [GR={game.gibrating}, PR={game.pubrating}, MP='
                                  f'{game.minplayer}, MT={game.playtime}]')
                            count += 1
                    if count == 0:
                        print("No games found...")
                except:
                    print("Invalid input. Try again! \n")
            if choice == 3: #Takes in 2 rankings and looks at the games with the gibrating between those numbers
                try:
                    min_rank = float(input("Enter the minimum rank you want to look at: "))
                    max_rank = float(input("Enter the maximum rank you want to look at: "))
                    count = 0
                    for game in games:
                        if min_rank <= game.gibrating <= max_rank:
                            print(f'{game.name} ({game.year}) [GR={game.gibrating}, PR={game.pubrating}, MP='
                                  f'{game.minplayer}, MT={game.playtime}]')
                            count += 1
                    if count == 0:
                        print("No games found...")
                except:
                    print("Invalid input. Try again! \n")
            if choice == 4: #Compares the difference between the pubrating and gibrating
                try:
                    num = float(input("Enter the number to see the difference between the public and Gibbons rating: "))
                    count = 0
                    for game in games:
                        if (game.pubrating - game.gibrating) >= num:
                            print(f'{game.name} ({game.year}) [GR={game.gibrating}, PR={game.pubrating}, MP='
                                  f'{game.minplayer}, MT={game.playtime}]')
                            count += 1
                        elif (game.gibrating - game.pubrating) >= num:
                            print(f'{game.name} ({game.year}) [GR={game.gibrating}, PR={game.pubrating}, MP='
                                  f'{game.minplayer}, MT={game.playtime}]')
                            count += 1
                    if count == 0:
                        print("No games found...")
                except:
                    print("Invalid input. Try again! \n")
            if choice == 5: #This prints the games with the minimum playtime entered and below that time.
                try:
                    min_time = int(input("Enter the minimum playtime you want to search in minutes: "))
                    count = 0
                    for game in games:
                        if min_time >= game.playtime:
                            print(f'{game.name} ({game.year}) [GR={game.gibrating}, PR={game.pubrating}, MP='
                                  f'{game.minplayer}, MT={game.playtime}]')
                            count += 1
                    if count == 0:
                        print("No games found...")
                except:
                    print("Invalid input. Try again! \n")
            if choice == 6:
                print("Exiting...")
