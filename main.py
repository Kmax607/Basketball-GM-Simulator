import random
from colors import green, red, yellow
import sys
import textwrap


draft_picks = 3

team_offense_ovr = 0
team_defense_ovr = 0
team_name = "Max"
team_wins = 0
team_losses = 0

team_won_playoffs = False

coach_wins = 0
coach_losses = 0
coach_chips = 0
coach_mvps = 0
coach_seasons = 0


first_name = ["Max", "Joe", "Teddy", "Xavier", "Miguel", "Anthony", "Richie", "Jeff", "Ethan", "Josh", "Noah", "Eli", "Ed", "Troy", "Annie", "Shirley", "Dean", "Ben", "Jacob", "Kevin", "Christina", "Lou", "Mike", "Michael", "Patrick", "Len", "Paul", "CJ", "John", "Jon", "Ally", "Andre", "Pierce", "Rob", "Joel", "Jacoby", "Mark", "JJ", "Kate", "Katie", "Zach", "Coby", "Brian", "Alfred", "Lamar", "Deshaun", "Mitch", "Chase", "Will", "Roger", "Amy", "Scout", "Molly", "Anna", "Julie", "Julia", "Wendy", "Alex", "Gene", "Roslyn", "Austin", "Tavon", "Collin", "Jacoby", "Jonah", "Thomas", "Taylor", "James", "Mary", "Jen", "Susan", "Sarah", "David", "Abby", "Margaret", "Diane", "Warren", "Joey", "Robin", "Lily", "Monica", "Jim", "Pam", "Ryan", "Carson", "Kelly", "Stan", "Stanley", "Parker", "Marshall", "Brandon", "Kareem", "Jabari", "Logan", "Brittney", "Bridget", "Vincent", "Phil", "Brad", "Peter", "Randy", "Emmanuel", "Clark", "Ava", "Scott", "Adam", "Daniel", "Hannah", "Nelson", "Rick", "Morty", "Summer", "Jerry", "Homer", "Lisa", "Maggie", "Meg", "Chris", "Stew", "Tina", "Louise", "Bob", "Bobby", "Gabe", "Evan", "Rachel", "Emma", "Grace", "Kyle", "Kyra", "Carmen", "Carter", "Steve", "Steven", "Aaron", "Erin", "Charlie", "Morgan", "Quinn", "Robert", "Mack", "Jackson", "Haley", "Luke", "Lucas", "Luka", "Tatiana", "Katarina", "Oliver", "Rhonda", "Harrison", "Harry", "Carla", "May", "April", "June", "Hugh", "Cole", "Allen", "Kenny", "Kevin", "Gwen", "Stacy", "Jeff", "Derek", "Rose", "Jimmy", "Joakim", "Tyler", "Ty", "Nathan", "Nate", "Hila", "Jason", "Fred", "Carrie", "Frances", "Francis", "Malcolm", "Reese", "Hal", "Lois", "Frank", "Jess", "Brooke", "Nolan", "Niko", "Brennan", "Drew", "Dakota", "Olivia", "Tony", "Antonio", "Jack", "Jane", "Ron", "Jude", "Howard", "Bruce", "Doris", "Vandan", "Timothy", "Lane", "Alexis", "Emily", "Ashley", "Jessica", "Lauren", "Laurie", "John", "Michael", "Sam", "Andrew", "Caroline", "Dan", "Megan", "John", "Kyle", "Kyler", "Bruce", "Andy", "Tanner", "Buzz", "Jessie", "Esteban", "Red"]
last_name = ["Kraus", "Chaiken", "Harris", "Smith", "Johnson", "Wufsus", "Rudd", "Kruger", "Shah", "Winger", "Malone", "Barnes", "Bryant", "Ali", "Scott", "Edwards", "Patrick", "Hershey", "Belg", "Snow", "Stark", "Fields", "Kammen", "Greenberg", "Jackson", "Carter", "McGrane", "Kornfeld", "White", "Black", "Turner", "Thomson", "Cranston", "Banks", "Watson", "Young", "Venable", "Watt", "Werth", "Hendricks", "Gilfoyle", "Woods", "Pecan", "Haut", "Hooper", "Liu", "Austin", "Price", "Williams", "Collins", "Jones", "Davis", "Green", "Robinson", "Thomas", "Wright", "Taylor", "Gabriel", "Miller", "King", "Lee", "Lew", "Walker", "Hamilton", "James", "Hill", "Gonzales", "Beasley", "Hall", "Marshall", "Hoover", "Parker", "Houston", "Granger", "Brown", "Garcia", "Sanders", "Rodriguez", "Hernandez", "Wilson", "Anderson", "Moore", "Lee", "Perez", "Clark", "King", "Scott", "Torres", "Adams", "Nelson", "Bighetti", "Baker", "Roberts", "Evans", "Diaz", "Simpson", "Blake", "Griffin", "Lewis", "Evans", "Cox", "Carter", "Tanaka", "Suzuki", "Stoker", "Morgan", "Quinn", "Mack", "Amend", "May", "Vasquez", "Stills", "Miller", "Jeffrey", "Rose", "Butler", "Noah", "Gasol", "Glasnow", "Robinson", "Fielder", "Pera", "Happ", "Souza", "Lavine", "Klein", "Armisen", "Brownstein", "Perkins", "Wilkerson", "Olson", "Franklin", "Brooks", "Nolan", "Ryan", "Shedlock", "Schwartz", "Singer", "Reed", "Richards", "Swanson", "Bush", "Morris", "Potter", "Weasley", "Law", "Luck", "Burback", "Burke", "Shanahan", "Lynch", "Walsh", "Cain", "Kane", "Lane", "Michaels", "Matthews", "Evans", "Trubisky", "Murray", "Allen", "Jobs", "Jeffrey", "Barkley", "Coulton", "Phillips", "Ray", "Durand", "Coughlin", "Davison", "Davis", "Sosa", "Johnson", "Smith", "Bernard", "Schmitt", "Agnew", "Woodley", "Fox", "Dempsey"]


position = ["PG", "SG", "SF", "PF", "C"]


#Defining opposing teams
opponent_1 = "Swamp Monsters" 
opponent_1_off = random.randint(3,9) + (.1 * (random.randint(0,10)))
opponent_1_def = random.randint(3,9) + (.1 * (random.randint(0,10)))
opponent_2 = "Roadkill" 
opponent_2_off = random.randint(3,9) + (.1 * (random.randint(0,10)))
opponent_2_def = random.randint(3,9) + (.1 * (random.randint(0,10)))
opponent_3 = "Talons"
opponent_3_off = random.randint(3,9) + (.1 * (random.randint(0,10)))
opponent_3_def = random.randint(3,9) + (.1 * (random.randint(0,10)))
opponent_4 = "Black Cats" 
opponent_4_off = random.randint(3,9) + (.1 * (random.randint(0,10)))
opponent_4_def = random.randint(3,9) + (.1 * (random.randint(0,10)))
opponent_5 = "Black Cats" 
opponent_5_off = random.randint(3,9) + (.1 * (random.randint(0,10)))
opponent_5_def = random.randint(3,9) + (.1 * (random.randint(0,10)))



money = 10


#starting roster
point_guard = random.choice(first_name) + " " + random.choice(last_name)
shooting_guard = random.choice(first_name) + " " + random.choice(last_name)
small_forward = random.choice(first_name) + " " + random.choice(last_name)
power_forward = random.choice(first_name) + " " + random.choice(last_name)
center = random.choice(first_name) + " " + random.choice(last_name)
#starting players offenses
point_guard_offense = random.randint(0, 8) + (.1 * random.randint(0, 19))
shooting_guard_offense = random.randint(0, 8) + (.1 * random.randint(0, 19))
small_forward_offense = random.randint(0, 8) + (.1 * random.randint(0, 19))
power_forward_offense = random.randint(0, 8) + (.1 * random.randint(0, 19))
center_offense = random.randint(0, 8) + (.1 * random.randint(0, 19))
#starting players defenses
point_guard_defense = random.randint(0, 8) + (.1 * random.randint(0, 19))
shooting_guard_defense = random.randint(0, 8) + (.1 * random.randint(0, 19))
small_forward_defense = random.randint(0, 8) + (.1 * random.randint(0, 19))
power_forward_defense = random.randint(0, 8) + (.1 * random.randint(0, 19))
center_defense = random.randint(0, 8) + (.1 * random.randint(0, 19))
#starting players contracts
point_guard_contract = random.randint(1, 3)
shooting_guard_contract = random.randint(1, 3)
small_forward_contract = random.randint(1, 3)
power_forward_contract = random.randint(1, 3)
center_contract = random.randint(1, 3)
#starting players ages
point_guard_age = random.randint(19, 35)
shooting_guard_age = random.randint(19, 35)
small_forward_age = random.randint(19, 35)
power_forward_age = random.randint(19, 35)
center_age = random.randint(19, 35)


#prints current roster and overalls
def print_team():
  global point_guard
  global shooting_guard
  global small_forward
  global power_forward
  global center
  global point_guard_offense
  global shooting_guard_offense
  global small_forward_offense
  global power_forward_offense
  global center_offense
  global point_guard_defense
  global shooting_guard_defense
  global small_forward_defense
  global power_forward_defense
  global center_defense
  global team_offense_ovr
  global team_defense_ovr
  global point_guard_contract
  global shooting_guard_contract
  global small_forward_contract
  global power_forward_contract
  global center_contract
  global point_guard_age
  global shooting_guard_age
  global small_forward_age
  global power_forward_age
  global center_age
  global point_guard_rookie
  global shooting_guard_rookie
  global small_forward_rookie
  global power_forward_rookie
  global center_rookie
  if point_guard_rookie == True:
    pg_r = " - R"
  else:
    pg_r = ""
  if shooting_guard_rookie == True:
    sg_r = " - R"
  else:
    sg_r = ""
  if small_forward_rookie == True:
    sf_r = " - R"
  else:
    sf_r = ""
  if power_forward_rookie == True:
    pf_r = " - R"
  else:
    pf_r = ""
  if center_rookie == True:
    c_r = " - R"
  else:
    c_r = ""
  print("PG - " + point_guard + " - " + str(point_guard_offense) + " OFF - " + str(point_guard_defense) + " DEF - " + str(point_guard_contract) + " YRS - " + str(point_guard_age) + " AGE" + pg_r)
  print("SG - " + shooting_guard + " - " + str(shooting_guard_offense) + " OFF - " + str(shooting_guard_defense) +  " DEF - " + str(shooting_guard_contract) + " YRS - " + str(shooting_guard_age) + " AGE" + sg_r)
  print("SF - " + small_forward + " - " + str(small_forward_offense) + " OFF - " + str(small_forward_defense) +  " DEF - " + str(small_forward_contract) + " YRS - " + str(small_forward_age) + " AGE" + sf_r)
  print("PF - " + power_forward + " - " + str(power_forward_offense) + " OFF - " + str(power_forward_defense) +  " DEF - " + str(power_forward_contract) + " YRS - " + str(power_forward_age) + " AGE" + pf_r)
  print("C  - " + center+ " - " + str(center_offense) + " OFF - " + str(center_defense) + " DEF - " + str(center_contract) + " YRS - " + str(center_age) + " AGE" + c_r)
  print("OVR - " + str(team_offense_ovr) + " OFF - " + str(team_defense_ovr) + " DEF")
  print()



age_to_retire = [25, 26, 27, 27, 28, 28, 29, 29, 29, 30, 30, 30 , 30, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36,37, 37, 37, 37, 37, 37, 37, 37, 38, 38, 38, 38, 38, 38, 39, 40, 41, 42, 43]



random_improvement_age = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]


#makes age affect stats and makes players retire
def age_matters():
  global point_guard
  global shooting_guard
  global small_forward
  global power_forward
  global center
  global point_guard_offense
  global shooting_guard_offense
  global small_forward_offense
  global power_forward_offense
  global center_offense
  global point_guard_defense
  global shooting_guard_defense
  global small_forward_defense
  global power_forward_defense
  global center_defense
  global point_guard_age
  global shooting_guard_age
  global small_forward_age
  global power_forward_age
  global center_age
  global age_to_retire
  global point_guard_contract
  global shooting_guard_contract
  global small_forward_contract
  global power_forward_contract
  global center_contract
  pg_retirement_age = random.choice(age_to_retire)
  sg_retirement_age = random.choice(age_to_retire)
  sf_retirement_age = random.choice(age_to_retire)
  pf_retirement_age = random.choice(age_to_retire)
  c_retirement_age = random.choice(age_to_retire)
  #replacing retired players
  if point_guard_age >= pg_retirement_age:
    print(point_guard + " has retired.")
    print()
    point_guard = random.choice(first_name) + " " + random.choice(last_name)
    point_guard_offense = random.randint(0, 10) + (.1 * random.randint(0, 10))
    point_guard_defense = random.randint(0, 10) + (.1 * random.randint(0, 10))
    point_guard_contract = random.randint(1, 3)
    point_guard_age = random.randint(19,35)
  if shooting_guard_age >= sg_retirement_age:
    print(shooting_guard + " has retired.")
    print()
    shooting_guard = random.choice(first_name) + " " + random.choice(last_name)
    shooting_guard_offense = random.randint(0, 10) + (.1 * random.randint(0, 10))
    shooting_guard_defense = random.randint(0, 10) + (.1 * random.randint(0, 10))
    shooting_guard_contract = random.randint(1, 3)
    small_forward_age = random.randint(19,35)
  if small_forward_age >= sf_retirement_age:
    print(small_forward + " has retired.")
    print()
    small_forward = random.choice(first_name) + " " + random.choice(last_name)
    small_forward_offense = random.randint(0, 10) + (.1 * random.randint(0, 10))
    small_forward_defense = random.randint(0, 10) + (.1 * random.randint(0, 10))
    small_forward_contract = random.randint(1, 3)
    small_forward_age = random.randint(19,35)
  if power_forward_age >= pf_retirement_age:
    print(power_forward + " has retired.")
    print()
    power_forward = random.choice(first_name) + " " + random.choice(last_name)
    power_forward_offense = random.randint(0, 10) + (.1 * random.randint(0, 10))
    power_forward_defense = random.randint(0, 10) + (.1 * random.randint(0, 10))
    power_forward_contract = random.randint(1, 3)
    power_forward_age = random.randint(19,35)
  if center_age >= c_retirement_age:
    print(center + " has retired.")
    print()
    center = random.choice(first_name) + " " + random.choice(last_name)
    center_offense = random.randint(0, 10) + (.1 * random.randint(0, 10))
    center_defense = random.randint(0, 10) + (.1 * random.randint(0, 10))
    center_contract = random.randint(1, 3)
    center_age = random.randint(19,35)
  improvement_with_age_pg = random.choice(random_improvement_age)
  improvement_with_age_sg = random.choice(random_improvement_age)
  improvement_with_age_sf = random.choice(random_improvement_age)
  improvement_with_age_pf = random.choice(random_improvement_age)
  improvement_with_age_c = random.choice(random_improvement_age)
  age_to_improve = random.randint(23,28)
  age_to_lose_it = random.randint(30,36)
  if point_guard_age <= age_to_improve:
   point_guard_offense += improvement_with_age_pg
   point_guard_defense += improvement_with_age_pg
  elif point_guard_age >= age_to_lose_it:
   point_guard_offense -= improvement_with_age_pg
   point_guard_defense -= improvement_with_age_pg
  if shooting_guard_age <= age_to_improve:
   shooting_guard_offense += improvement_with_age_sg
   shooting_guard_defense += improvement_with_age_sg
  elif shooting_guard_age >= age_to_lose_it:
   shooting_guard_offense -= improvement_with_age_sg
   shooting_guard_defense -= improvement_with_age_sg
  if small_forward_age <= age_to_improve:
   small_forward_offense += improvement_with_age_sf
   small_forward_defense += improvement_with_age_sf
  elif small_forward_age >= age_to_lose_it:
   small_forward_offense -= improvement_with_age_sf
   small_forward_defense -= improvement_with_age_sf
  if power_forward_age <= age_to_improve:
   power_forward_offense += improvement_with_age_pf
   power_forward_defense += improvement_with_age_pf
  elif power_forward_age >= age_to_lose_it:
   power_forward_offense -= improvement_with_age_pf
   power_forward_defense -= improvement_with_age_pf
  if center_age <= age_to_improve:
   center_offense += improvement_with_age_c
   center_defense += improvement_with_age_c
  elif center_age >= age_to_lose_it:
   center_offense -= improvement_with_age_c
   center_defense -= improvement_with_age_c




def get_team_ovr():
  global point_guard_offense
  global shooting_guard_offense
  global small_forward_offense
  global power_forward_offense
  global center_offense
  global point_guard_defense
  global shooting_guard_defense
  global small_forward_defense
  global power_forward_defense
  global center_defense
  global team_offense_ovr
  global team_defense_ovr
  point_guard_offense = round(point_guard_offense, 1)
  shooting_guard_offense = round(shooting_guard_offense, 1)
  small_forward_offense = round(small_forward_offense, 1)
  power_forward_offense = round(power_forward_offense, 1)
  center_offense = round(center_offense, 1)
  point_guard_defense = round(point_guard_defense, 1)
  shooting_guard_defense = round(shooting_guard_defense, 1)
  small_forward_defense = round(small_forward_defense, 1)
  power_forward_defense = round(power_forward_defense, 1)
  center_defense = round(power_forward_defense, 1)
  if team_name == "MAX HAX":
    team_offense_ovr = 10.0
    team_defense_ovr = 10.0
  if team_name == "Nano's Windians Nans":
    team_offense_ovr = 20.0
    team_defense_ovr = 20.0
  else:
    team_offense = point_guard_offense + shooting_guard_offense + small_forward_offense + power_forward_offense + center_offense
    team_offense_ovr = team_offense / 5
    team_defense = point_guard_defense + shooting_guard_defense + small_forward_defense + power_forward_defense + center_defense
    team_offense_ovr = team_offense / 5
    team_defense_ovr = team_defense / 5
  team_offense_ovr = round(team_offense_ovr, 1)
  team_defense_ovr = round(team_defense_ovr, 1)
  return team_offense_ovr
  return team_defense_ovr


#Gets team name
def get_team_name():
  global team_name
  global team_adj
  global team_noun
  global team_loc
  team_name = input("Welcome, coach! What's the name of your team? ")
  if team_name == "" or team_name == " ":
    team_name = random.choice(team_adj) + random.choice(team_noun)
  print()
  my_team_loc = input("Where are the " + team_name + " from? ")
  if my_team_loc == "" or my_team_loc == " ":
    my_team_loc = random.choice(team_loc)
  print()
  team_name = my_team_loc + " " + team_name
  return team_name

#start of game
def start_game():
  global point_guard
  global shooting_guard
  global small_forward
  global power_forward
  global center
  global team_offense_ovr
  global team_defense_ovr
  global draft_picks
  global money
  global point_guard_contract
  global shooting_guard_contract
  global small_forward_contract
  global power_forward_contract
  global center_contract
  global team_wins
  global team_losses
  global coach_wins
  global coach_losses
  global coach_chips
  global point_guard_age
  global shooting_guard_age
  global small_forward_age
  global power_forward_age
  global center_age
  global coach_seasons
  global point_guard_rookie
  global shooting_guard_rookie
  global small_forward_rookie
  global power_forward_rookie
  global center_rookie
  get_team_name()
  global team_name
  print("Take a look at the " + team_name)
  get_team_ovr()
  print()
  print_team()
  continue_game = input("Press Enter to Continue ")
  print()
  if draft_picks == 1:
    print("Time for the draft! You have " + str(draft_picks) + " pick")
  else:
    print("Time for the draft! You have " + str(draft_picks) + " picks")
  print()
  while draft_picks > 0:
    draft()
  print()
  print("You have no remaining picks.")
  print()
  continue_game = input("Press Enter to Continue ")
  print()
  free_agency()
  print()
  get_team_ovr()
  print("Check out the new " + team_name + "!")
  print()
  get_team_ovr()
  print_team()
  print()
  continue_game = input("Press Enter to Continue ")
  print()
  get_strategy()
  print_team()
  print()
  continue_game = input("Press Enter to Continue ")
  print()
  print("The season is about to begin")
  print()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  propose_trade()
  continue_game = input("Press Enter to Continue ")
  print()
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  playoff_req = random.randint(8,10)
  if team_wins >= playoff_req:
   print(green(("Congratulations, the " + team_name + " made the playoffs!")))
   print()
   continue_game = input("Press Enter to Continue ")
   print()
   playoffs()
  else:
   print(red("The " + team_name + " have missed the playoffs. Better luck next year"))
   print()
  input("Press Enter to Continue ")
  print()
  get_roty()
  input("Press Enter to Continue ")
  print()
  get_mvp()
  input("Press Enter to Continue ")
  print()
  coach_wins += team_wins
  coach_losses += team_losses
  coach_seasons += 1
  retire()
  draft_picks += 3
  money += random.randint(4,8)
  point_guard_contract -= 1
  shooting_guard_contract -= 1
  small_forward_contract -= 1
  power_forward_contract -= 1
  center_contract -= 1
  team_wins = 0
  team_losses = 0
  point_guard_age += 1
  shooting_guard_age += 1
  small_forward_age += 1
  power_forward_age += 1
  center_age += 1
  new_season()
    







def new_season():
  global point_guard
  global shooting_guard
  global small_forward
  global power_forward
  global center
  global point_guard_offense
  global shooting_guard_offense
  global small_forward_offense
  global power_forward_offense
  global center_offense
  global point_guard_defense
  global shooting_guard_defense
  global small_forward_defense
  global power_forward_defense
  global center_defense
  global team_offense_ovr
  global team_defense_ovr
  global draft_picks
  global money
  global point_guard_contract
  global shooting_guard_contract
  global small_forward_contract
  global power_forward_contract
  global center_contract
  global team_wins
  global team_losses
  global coach_wins
  global coach_losses
  global point_guard_age
  global shooting_guard_age
  global small_forward_age
  global power_forward_age
  global center_age
  global coach_seasons
  global point_guard_rookie
  global shooting_guard_rookie
  global small_forward_rookie
  global power_forward_rookie
  global center_rookie
  print()
  print_coach_stats()
  print()
  point_guard_rookie = False
  shooting_guard_rookie = False
  small_forward_rookie = False
  power_forward_rookie = False
  center_rookie = False
  age_matters()
  #Replaces players with expired contracts
  ready_for_again = input("Press enter to start a new season ")
  print()
  renew_length_pg = random.randint(1,3)
  renew_cost_pg = random.randint(2,18)
  renew_length_sg = random.randint(1,3)
  renew_cost_sg = random.randint(2,18)
  renew_length_sf = random.randint(1,3)
  renew_cost_sf = random.randint(2,18)
  renew_length_pf = random.randint(1,3)
  renew_cost_pf = random.randint(2,18)
  renew_length_c = random.randint(1,3)
  renew_cost_c = random.randint(2,18)
  print("A new season begins!")
  print()
  continue_game = input("Press Enter to Continue ")
  print()
  print("You have $" + str(money) + " remaining")
  print()
  get_team_ovr()
  print_team()
  print()
  continue_game = input("Press Enter to Continue ")
  print()
  if point_guard_contract == 0:
    resign_q = input(point_guard + "'s contract has expired. Would you like to renew it for " + str(renew_length_pg) + " years for $" + str(renew_cost_pg) + " (Yes, No) ").lower()
    print()
    if resign_q == "Yes".lower() and money >= renew_cost_pg:
      point_guard_contract = renew_length_pg 
      money -= renew_cost_pg
    else:
      point_guard = random.choice(first_name) + " " + random.choice(last_name)
      point_guard_offense = random.randint(0, 8) + (.1 * random.randint(0, 19))
      point_guard_defense = random.randint(0, 8) + (.1 * random.randint(0, 19))
      point_guard_contract = random.randint(1, 3)
  if shooting_guard_contract == 0:
    resign_q = input(shooting_guard + "'s contract has expired. Would you like to renew it for " + str(renew_length_sg) + " years for $" + str(renew_cost_sg) + " (Yes, No) ").lower()
    print()
    if resign_q == "Yes".lower() and money >= renew_cost_sg:
      shooting_guard_contract = renew_length_sg 
      money -= renew_cost_sg
    else:
      shooting_guard = random.choice(first_name) + " " + random.choice(last_name)
      shooting_guard_offense = random.randint(0, 8) + (.1 * random.randint(0, 19))
      shooting_guard_defense = random.randint(0, 8) + (.1 * random.randint(0, 19))
      shooting_guard_contract = random.randint(1, 3)
  if small_forward_contract == 0:
    resign_q = input(small_forward + "'s contract has expired. Would you like to renew it for " + str(renew_length_sf) + " years for $" + str(renew_cost_sf) + " (Yes, No) ").lower()
    print()
    if resign_q == "Yes".lower() and money >= renew_cost_sf:
      small_forward_contract = renew_length_sf 
      money -= renew_cost_sf
    else:
      small_forward = random.choice(first_name) + " " + random.choice(last_name)
      small_forward_offense = random.randint(0, 8) + (.1 * random.randint(0, 19))
      small_forward_defense = random.randint(0, 8) + (.1 * random.randint(0, 19))
      small_forward_contract = random.randint(1, 3)
  if power_forward_contract == 0:
    resign_q = input(power_forward + "'s contract has expired. Would you like to renew it for " + str(renew_length_pf) + " years for $" + str(renew_cost_pf) + " (Yes, No) ").lower()
    print()
    if resign_q == "Yes".lower() and money >= renew_cost_pf:
      power_forward_contract = renew_length_pf 
      money -= renew_cost_pf
    else:
      power_forward = random.choice(first_name) + " " + random.choice(last_name)
      power_forward_offense = random.randint(0, 8) + (.1 * random.randint(0, 19))
      power_forward_defense = random.randint(0, 8) + (.1 * random.randint(0, 19))
      power_forward_contract = random.randint(1, 3)
  if center_contract == 0:
    resign_q = input(center + "'s contract has expired. Would you like to renew it for " + str(renew_length_c) + " years for $" + str(renew_cost_c) + " (Yes, No) ").lower()
    print()
    if resign_q == "Yes".lower and money >= renew_cost_c:
      center_contract = renew_length_c
      money -= renew_cost_c
    else:
      center = random.choice(first_name) + " " + random.choice(last_name)
      center_offense = random.randint(0, 8) + (.1 * random.randint(0, 19))
      center_defense = random.randint(0, 8) + (.1 * random.randint(0, 19))
      center_contract = random.randint(1, 3)
  print()
  global team_name
  print("Take a look at the " + team_name)
  get_team_ovr()
  print()
  get_team_ovr()
  print_team()
  print()
  continue_game = input("Press Enter to Continue ")
  print()
  if draft_picks == 1:
    print("Time for the draft! You have " + str(draft_picks) + " pick")
  else:
    print("Time for the draft! You have " + str(draft_picks) + " picks")
  print()
  while draft_picks > 0:
    draft()
  print("You have no remaining picks.")
  print()
  continue_game = input("Press Enter to Continue ")
  print()
  free_agency()
  print()
  get_strategy()
  print("Check out the new " + team_name + "!")
  print_team()
  print()
  continue_game = input("Press Enter to Continue ")
  print()
  print("The season is about to begin")
  print()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  propose_trade()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  playoff_req = random.randint(8,10)
  if team_wins >= playoff_req:
   print(green("Congratulations, the " + team_name + " made the playoffs!"))
   print()
   continue_game = input("Press Enter to Continue ")
   print()
   playoffs()
  else:
   print(red("The " + team_name + " have missed the playoffs. Better luck next year"))
   print()
  continue_game = input("Press Enter to Continue ")
  print()
  get_roty()
  continue_game = input("Press Enter to Continue ")
  print()
  get_mvp()
  continue_game = input("Press Enter to Continue ")
  print()
  retire()
  print()
  coach_seasons += 1
  coach_wins += team_wins
  coach_losses += team_losses
  draft_picks += 3
  money += random.randint(4,8)
  point_guard_contract -= 1
  shooting_guard_contract -= 1
  small_forward_contract -= 1
  power_forward_contract -= 1
  center_contract -= 1
  point_guard_age += 1
  shooting_guard_age += 1
  small_forward_age += 1
  power_forward_age += 1
  center_age += 1
  team_wins = 0
  team_losses = 0
  new_season()





def hall_of_fame():
  coach_chips
  coach_wins
  coach_losses
  coach_mvps
  coach_seasons
  coach_rotys
  if coach_wins + (10 * coach_chips) - coach_losses + (5 *coach_mvps) + (3 * coach_rotys) >= 65:
    print()
    print(yellow("You've cemented your legacy and have been accepted into the hall of fame. Congratulations, coach!"))
  else:
    print()
    print("You weren't accepted into the hall of fame, but that doesn't mean you had a bad career.")
    print()



retire_statements = ["Is it time to drop the clipboard for good", "Is it time to cut your losses", "Do you want to end on a high note", "Will you coach again next year, or will you give up", "Is it time to pass on the torch", "Will you end your coaching story"]




def retire():
  global retire_statements
  is_this_the_end = input(random.choice(retire_statements) + " and retire? (Yes, No) ").lower()
  print()
  if is_this_the_end == "Yes".lower() or is_this_the_end == "Yes".lower():
    print("You've had your fun, but all good things must come to an end.")
    print()
    print_coach_stats()
    print()
    continue_or_not = input("Press Enter to Continue ")
    print()
    hall_of_fame()
    print()
    print("Thanks for playing!")
    continue_or_not = input("Press Enter to Exit ")
    sys.exit()






def playoffs():
  global team_name
  global team_won_playoffs
  playoff_opponent_1 = random.randint(1,5)
  new_play_playoff_game()
  global team_won_playoffs
  global coach_chips
  if team_won_playoffs == True:
    print()
    print(green("The " + team_name + " are in the championship!"))
    print()
    champ_bound = input("Press Enter to Continue ")
    print()
    new_play_playoff_game()
    print()
    wanna_continue = input("Press Enter to Continue ")
    print()
    if team_won_playoffs == True:
      print()
      print_trophy()
      print()
      print()
      print(yellow("The " + team_name + " are world champions! Let's do it again!"))
      coach_chips += 1
      print()
      print()
    else:
      print()
      print(red("The " + team_name + " have been eliminated. So close but yet so far!"))
      print()
  else:
    print()
    print(red("The " + team_name + " have been eliminated. Better luck next year."))
    print()




def draft():
  global first_name
  global last_name
  global team_name
  global point_guard
  global shooting_guard
  global small_forward
  global power_forward
  global center
  global point_guard_offense
  global shooting_guard_offense
  global small_forward_offense
  global power_forward_offense
  global center_offense
  global point_guard_defense
  global shooting_guard_defense
  global small_forward_defense
  global power_forward_defense
  global center_defense
  global position
  global draft_picks
  global point_guard_contract
  global shooting_guard_contract
  global small_forward_contract
  global power_forward_contract
  global center_contract
  global point_guard_age
  global shooting_guard_age
  global small_forward_age
  global power_forward_age
  global center_age
  global point_guard_rookie
  global shooting_guard_rookie
  global small_forward_rookie
  global power_forward_rookie
  global center_rookie
  draft_age_1 = random.randint(19, 24)
  draft_age_2 = random.randint(19, 24)
  draft_age_3 = random.randint(19, 24)
  print("You're on the clock! Here are all the available players:")
  choice_1 = random.choice(first_name) + " " + random.choice(last_name)
  choice_2 = random.choice(first_name) + " " + random.choice(last_name)
  choice_3 = random.choice(first_name) + " " + random.choice(last_name)
  choice_1_pos = random.choice(position)
  choice_2_pos = random.choice(position)
  choice_3_pos = random.choice(position)
  choice_1_offense = random.randint(0, 10) + (.1 * random.randint(0, 10))
  choice_1_defense = random.randint(0, 10) + (.1 * random.randint(0, 10))
  choice_2_offense = random.randint(2, 9) + (.1 * random.randint(0, 10))
  choice_2_defense = random.randint(2, 9) + (.1 * random.randint(0, 10))
  choice_3_offense = random.randint(3, 8) + (.1 * random.randint(0, 10))
  choice_3_defense = random.randint(3, 8) + (.1 * random.randint(0, 10))
  choice_1_offense = round(choice_1_offense,1)
  choice_2_offense = round(choice_2_offense,1)
  choice_3_offense = round(choice_3_offense,1)
  choice_1_defense = round(choice_1_defense,1)
  choice_2_defense = round(choice_2_defense,1)
  choice_3_defense = round(choice_3_defense,1)
  print(choice_1_pos + " - " + choice_1 + " - " + str(choice_1_offense) + " OFF - " + str(choice_1_defense) + " DEF - " + str(draft_age_1) + " AGE")
  print(choice_2_pos + " - " + choice_2 + " - "  +  str(choice_2_offense) + " OFF - " + str(choice_2_defense) + " DEF - " + str(draft_age_2) + " AGE")
  print(choice_3_pos + " - " + choice_3 + " - "  +  str(choice_3_offense) + " OFF - " + str(choice_3_defense) + " DEF - " + str(draft_age_1) + " AGE")
  print()
  pick = input("Who would you like to draft? ").lower()
  print()
  if pick == choice_1.lower():
    print()
    print("Welcome to the " + team_name + ", " + choice_1 + "!")
    print()
#Substitutes draft pick into team for choice 1
    if choice_1_pos == "PG":
      point_guard = choice_1
      point_guard_offense = choice_1_offense
      point_guard_defense = choice_1_defense
      point_guard_contract = 3
      point_guard_age = draft_age_1
      point_guard_rookie = True
    elif choice_1_pos == "SG":
      shooting_guard = choice_1
      shooting_guard_offense = choice_1_offense
      shooting_guard_defense = choice_1_defense
      shooting_guard_contract = 3
      shooting_guard_age = draft_age_1
      shooting_guard_rookie = True
    elif choice_1_pos == "SF":
      small_forward = choice_1
      small_forward_offense = choice_1_offense
      small_forward_defense = choice_1_defense
      small_forward_contract = 3
      small_forward_age = draft_age_1
      small_forward_rookie = True
    elif choice_1_pos == "PF":
      power_forward = choice_1
      power_forward_offense = choice_1_offense
      power_forward_defense = choice_1_defense
      power_forward_contract = 3
      power_forward_age = draft_age_1
      power_forward_rookie = True
    elif choice_1_pos == "C":
      center = choice_1
      center_offense = choice_1_offense
      center_defense = choice_1_defense
      center_contract = 3  
      center_age = draft_age_1
      center_rookie = True
    get_team_ovr()
    print_team() 
  if pick == choice_2.lower():
     print()
     print("Welcome to the " + team_name + ", " + choice_2 + "!")
     print()
#Substitutes draft pick into team for choice 2
     if choice_2_pos == "PG":
       point_guard = choice_2
       point_guard_offense = choice_2_offense
       point_guard_defense = choice_2_defense
       point_guard_contract = 3
       point_guard_age = draft_age_2
       point_guard_rookie = True
     elif choice_2_pos == "SG":
       shooting_guard = choice_2
       shooting_guard_offense = choice_2_offense
       shooting_guard_defense = choice_2_defense
       shooting_guard_contract = 3
       shooting_guard_age = draft_age_2
       shooting_guard_rookie = True
     elif choice_2_pos == "SF":
       small_forward = choice_2
       small_forward_offense = choice_2_offense
       small_forward_defense = choice_2_defense
       small_forward_contract = 3
       small_forward_age = draft_age_2
       small_forward_rookie = True
     elif choice_2_pos == "PF":
       power_forward = choice_2
       power_forward_offense = choice_2_offense
       power_forward_defense = choice_2_defense
       power_forward_contract = 3
       power_forward_age = draft_age_2
       power_forward_rookie = True
     elif choice_2_pos == "C":
       center = choice_2
       center_offense = choice_2_offense
       center_defense = choice_2_defense
       center_contract = 3
       center_age = draft_age_2
       center_rookie = True
     get_team_ovr()
     print_team()
  if pick == choice_3.lower():
     print()
     print("Welcome to the " + team_name + ", " + choice_3 + "!")
     print()
#Substitutes draft pick into team for choice 3
     if choice_3_pos == "PG":
       point_guard = choice_3
       point_guard_offense = choice_3_offense
       point_guard_defense = choice_3_defense
       point_guard_contract = 3
       point_guard_age = draft_age_3
       point_guard_rookie = True
     elif choice_3_pos == "SG":
       shooting_guard = choice_3
       shooting_guard_offense = choice_3_offense
       shooting_guard_defense = choice_3_defense
       shooting_guard_contract = 3
       shooting_guard_age = draft_age_3
       shooting_guard_rookie = True
     elif choice_3_pos == "SF":
       small_forward = choice_3
       small_forward_offense = choice_3_offense
       small_forward_defense = choice_3_defense
       small_forward_contract = 3
       small_forward_age = draft_age_3
       small_forward_rookie = True
     elif choice_3_pos == "PF":
       power_forward = choice_3
       power_forward_offense = choice_3_offense
       power_forward_defense = choice_3_defense
       power_forward_contract = 3
       power_forward_age = draft_age_3
       power_forward_rookie = True
     elif choice_3_pos == "C":
       center = choice_3
       center_offense = choice_3_offense
       center_defense = choice_3_defense
       center_contract = 3
       center_age = draft_age_3
       point_guard_rookie = True
     get_team_ovr()
     print()
     print_team()
     continuuuu = input("Press Enter to Continue ")
  draft_picks -= 1
  return point_guard
  return shooting_guard
  return small_forward
  return power_forward
  return center
  return point_guard_offense
  return shooting_guard_offense
  return small_forward_offense
  return power_forward_offense
  return center_offense
  return point_guard_defense
  return shooting_guard_defense
  return small_forward_defense
  return power_forward_defense
  return center_defense
  return draft_picks
  return point_guard_contract
  return shooting_guard_contract
  return small_forward_contract
  return power_forward_contract
  return center_contract
  return point_guard_age
  return shooting_guard_age
  return small_forward_age
  return power_forward_age
  return center_age






def print_coach_stats():
  global coach_wins
  global coach_losses
  global coach_chips
  global coach_mvps
  global coach_seasons
  global coach_rotys
  print("In " + str(coach_seasons) + " seasons, your career record is " + str(coach_wins) + "-" + str(coach_losses) + ". You've won " + str(coach_chips) + " championships. You've coached " + str(coach_mvps) + " MVPs and " + str(coach_rotys) + " ROTYs.")
  print()





def print_trophy():
  print(yellow("    ___________"))
  print(yellow("   '._==_==_=_.'"))
  print(yellow("   .-\:      /-."))
  print(yellow("  | (|:.     |) |"))
  print(yellow("   '-|:.     |-'"))
  print(yellow("     \::.    /"))
  print(yellow("      '::. .'"))
  print(yellow("        ) ("))
  print(yellow("      _.' '._"))
  print(yellow("      `'''''`"))






def print_dunk_1():
  print("          ________")
  print("  o      |   __   |")
  print("   \_ O  |  |__|  |")
  print(" ____/ \ |___WW___|")
  print(" __/   /     ||")
  print("             ||")
  print("             ||")
  print("_____________||________________")





def print_block():
  print("  o- - - \              |")
  print("       /  \o          __|")
  print("     o/   /|          vv`\ ")
  print("    /|   / |              |")
  print("   / |    / \_            |")
  print("    / \   \               |")
  print("   /   \                  |")




def print_deep_3():
  print("            o   ")
  print("       o        ")
  print("               o  ")
  print("/|  o           ")
  print("\|--            o  ")
  print("  WW             ")
  print("                 \ \  ")
  print("              /   \O")
  print("             O_/   |")
  print("             |    /|")
  print("             |\  | |")
  print("_____________|_|________")



highlight_string = ["was named a top 10 play of the week!", "has everyone talking!", "was spectacular!", "was a game changer!", "was on the cover of 'BBall Weekly'!", "was named a top 10 play of the week!", "has everyone talking!", "was spectacular!", "was a game changer!", "was on the cover of 'BBall Weekly'!", "was the play of the season!"]


def get_highlights():
  global point_guard
  global shooting_guard
  global small_forward
  global power_forward
  global center
  global point_guard_offense
  global shooting_guard_offense
  global small_forward_offense
  global power_forward_offense
  global center_offense
  global point_guard_defense
  global shooting_guard_defense
  global small_forward_defense
  global power_forward_defense
  global center_defense
  pg_o_highlight = random.randint(0,22) + point_guard_offense
  sg_o_highlight = random.randint(0,22) + shooting_guard_offense
  sf_o_highlight = random.randint(0,22) + small_forward_offense
  pf_o_highlight = random.randint(0,22) + power_forward_offense
  c_o_highlight = random.randint(0,22) + center_offense
  pg_d_highlight = random.randint(0,22) + point_guard_defense
  sg_d_highlight = random.randint(0,22) + shooting_guard_defense
  sf_d_highlight = random.randint(0,22) + small_forward_defense
  pf_d_highlight = random.randint(0,22) + power_forward_defense
  c_d_highlight = random.randint(0,22) + center_defense
  pg_o_h = False
  pg_d_h = False
  sg_o_h = False
  sg_d_h = False
  sf_o_h = False
  sf_d_h = False
  pf_o_h = False
  pf_d_h = False
  c_o_h = False
  c_d_h = False
  if pg_o_highlight >= 30:
    pg_o_h = True
  if sg_o_highlight >= 28:
    sg_o_h = True
  if sf_o_highlight >= 29:
    sf_o_h = True
  if pf_o_highlight >= 29:
    pf_o_h = True
  if c_o_highlight >= 29:
    c_o_h = True
  if pg_d_highlight >= 31:
    pg_d_h = True
  if sg_d_highlight >= 31:
    sg_d_h = True
  if sf_d_highlight >= 29:
    sf_d_h = True
  if pf_d_highlight >= 29:
    pf_d_h = True
  if c_d_highlight >= 28:
    c_d_h = True
  if pg_o_h == True:
    print_deep_3()
    print()
    print(point_guard + "'s deep 3 " + random.choice(highlight_string))
    print()
  elif sg_o_h == True:
    print_deep_3()
    print()
    print(shooting_guard + "'s deep 3 " + random.choice(highlight_string))
    print()
  elif sf_o_h == True:
    print_dunk_1()
    print()
    print(small_forward + "'s slam dunk "+ random.choice(highlight_string))
    print()
  elif pf_o_h == True:
    print_dunk_1()
    print()
    print(power_forward + "'s slam dunk " + random.choice(highlight_string))
    print()
  elif c_o_h == True:
    print_dunk_1()
    print()
    print(center + "'s slam dunk " + random.choice(highlight_string))
    print()
  elif pg_d_h == True:
    print_block()
    print()
    print(point_guard + "'s huge block "  + random.choice(highlight_string))
    print()
  elif sg_d_h == True:
    print_block()
    print()
    print(shooting_guard + "'s huge block "  + random.choice(highlight_string))
    print()
  elif sf_d_h == True:
    print_block()
    print()
    print(small_forward + "'s huge block "  + random.choice(highlight_string))
    print()
  elif pf_d_h == True:
    print_block()
    print()
    print(power_forward + "'s huge block " + random.choice(highlight_string))
    print()
  elif c_d_h == True:
    print_block()
    print()
    print(center + "'s huge block "  + random.choice(highlight_string))
    print()



def propose_trade():
  global first_name
  global last_name
  global team_name
  global team_loc
  global team_adj
  global team_noun
  global point_guard
  global shooting_guard
  global small_forward
  global power_forward
  global center
  global point_guard_offense
  global shooting_guard_offense
  global small_forward_offense
  global power_forward_offense
  global center_offense
  global point_guard_defense
  global shooting_guard_defense
  global small_forward_defense
  global power_forward_defense
  global center_defense
  global position
  global draft_picks
  global point_guard_contract
  global shooting_guard_contract
  global small_forward_contract
  global power_forward_contract
  global center_contract
  global point_guard_age
  global shooting_guard_age
  global small_forward_age
  global power_forward_age
  global center_age
  new_player_contract = random.randint(1,3)
  new_player_name = random.choice(first_name) + " " + random.choice(last_name)
  new_player_off = random.randint(3,10) + (.1 * (random.randint(0,10)))
  new_player_def = random.randint(3,10) + (.1 * (random.randint(0,10)))
  trade_partner = random.choice(team_loc) + " " + random.choice(team_adj) + random.choice(team_noun)
  new_player_age = random.randint(19,35)
  if new_player_off + new_player_def <= 11:
    draft_picks_req = 1
  else:
    draft_picks_req = 2
  print("The trade deadline is approaching.")
  print()
  conntinew = input("Press Enter to Continue ")
  print()
  trade_ornah = input("Would you like to propose a trade? If you do, you will lose your bonus from practice (Yes, No) ").lower()
  print()
  if trade_ornah == "Yes".lower() or trade_ornah == "Y".lower():
    print_team()
    whos_going = input("What position are you willing to trade? (PG, SG, SF, PF, C) ").lower()
    print()
    if whos_going == "PG".lower():
      print("PG - " + new_player_name + " - " + str(new_player_off) + " OFF - " + str(new_player_def) + " DEF - " + str(new_player_contract) + " YRS - " + str(new_player_age) + " AGE")
      print()
      print("The " + trade_partner + " are willing to trade point guard " + new_player_name + " for " + point_guard + " and " + str(draft_picks_req) + " picks in next year's draft.")
      print()
      trade_happening = input("Do you accept? (Yes, No) ").lower()
      print()
      if trade_happening == "Yes".lower() or trade_happening == "Y".lower():
        draft_picks -= draft_picks_req
        point_guard = new_player_name
        point_guard_offense = new_player_off
        point_guard_defense = new_player_def
        point_guard_contract = new_player_contract
        point_guard_age = new_player_age
    if whos_going == "SG".lower():
      print("SG - " + new_player_name + " - " + str(new_player_off) + " OFF - " + str(new_player_def) + " DEF - " + str(new_player_contract) + " YRS - " + str(new_player_age) + " AGE")
      print()
      trade_happening = input("The " + trade_partner + " are willing to trade shooting guard " + new_player_name + " for " + shooting_guard + " and " + str(draft_picks_req) + " picks in next year's draft. Do you accept? (Yes, No) ").lower()
      print()
      if trade_happening == "Yes".lower() or trade_happening == "Yes".lower():
        draft_picks -= draft_picks_req
        shooting_guard = new_player_name
        shooting_guard_offense = new_player_off
        shooting_guard_defense = new_player_def
        shooting_guard_contract = new_player_contract
        shooting_guard_age = new_player_age
    if whos_going == "SF".lower():
      print("SF - " + new_player_name + " - " + str(new_player_off) + " OFF - " + str(new_player_def) + " DEF - " + str(new_player_contract) + " YRS - " + str(new_player_age) + " AGE")
      print()
      trade_happening = input("The " + trade_partner + " are willing to trade small forward " + new_player_name + " for " + small_forward + " and " + str(draft_picks_req) + " picks in next year's draft. Do you accept? (Yes, No) ").lower()
      print()
      if trade_happening == "Yes".lower() or trade_happening == "Y".lower():
        draft_picks -= draft_picks_req
        small_forward = new_player_name
        small_forward_offense = new_player_off
        small_forward_defense = new_player_def
        small_forward_contract = new_player_contract
        small_forward_age = new_player_age
    if whos_going == "PF".lower():
      print("PF - " + new_player_name + " - " + str(new_player_off) + " OFF - " + str(new_player_def) + " DEF - " + str(new_player_contract) + " YRS - " + str(new_player_age) + " AGE")
      print()
      trade_happening = input("The " + trade_partner + " are willing to trade power forward " + new_player_name + " for " + power_forward + " and " + str(draft_picks_req) + " picks in next year's draft. Do you accept? (Yes, No) ").lower()
      print()
      if trade_happening == "Yes".lower() or trade_happening == "Y".lower():
        draft_picks -= draft_picks_req
        power_forward = new_player_name
        power_forward_offense = new_player_off
        power_forward_defense = new_player_def
        power_forward_contract = new_player_contract
        power_forward_age = new_player_age
    if whos_going == "C".lower():
      print("C - " + new_player_name + " - " + str(new_player_off) + " OFF - " + str(new_player_def) + " DEF - " + str(new_player_contract) + " YRS - " + str(new_player_age) + " AGE")
      print()
      trade_happening = input("The " + trade_partner + " are willing to trade point guard " + new_player_name + " for " + center + " and " + str(draft_picks_req) + " picks in next year's draft. Do you accept? (Yes, No) ").lower()
      print()
      if trade_happening == "Yes".lower() or trade_happening == "Yes".lower():
        draft_picks -= draft_picks_req
        center = new_player_name
        center_offense = new_player_off
        center_defense = new_player_def
        center_contract = new_player_contract
        center_age = new_player_age
    get_team_ovr()
  print("The midseason lineup for the " + team_name)
  print()
  print_team()




def free_agency():
  global first_name
  global last_name
  global position
  global point_guard
  global shooting_guard
  global small_forward
  global power_forward
  global center
  global point_guard_offense
  global shooting_guard_offense
  global small_forward_offense
  global power_forward_offense
  global center_offense
  global point_guard_defense
  global shooting_guard_defense
  global small_forward_defense
  global power_forward_defense
  global center_defense
  global point_guard_contract
  global shooting_guard_contract
  global small_forward_contract
  global power_forward_contract
  global center_contract
  global money
  global point_guard_age
  global shooting_guard_age
  global small_forward_age
  global power_forward_age
  global center_age
  new_money = money
  print("These are the available free agents. You have $" + str(money) + " remaining")
  print()
  choice_1 = random.choice(first_name) + " " + random.choice(last_name)
  choice_2 = random.choice(first_name) + " " + random.choice(last_name)
  choice_3 = random.choice(first_name) + " " + random.choice(last_name)
  choice_1_pos = random.choice(position)
  choice_2_pos = random.choice(position)
  choice_3_pos = random.choice(position)
  choice_1_offense = random.randint(0, 10) + (.1 * random.randint(0, 10))
  choice_1_defense = random.randint(0, 10) + (.1 * random.randint(0, 10))
  choice_2_offense = random.randint(4, 10) + (.1 * random.randint(0, 10))
  choice_2_defense = random.randint(4, 10) + (.1 * random.randint(0, 10))
  choice_3_offense = random.randint(6, 10) + (.1 * random.randint(0, 10))
  choice_3_defense = random.randint(6, 10) + (.1 * random.randint(0, 10))
  choice_1_offense = round(choice_1_offense, 1)
  choice_2_offense = round(choice_2_offense, 1)
  choice_3_offense = round(choice_3_offense, 1)
  choice_1_defense = round(choice_1_defense, 1)
  choice_2_defense = round(choice_2_defense, 1)
  choice_3_defense = round(choice_3_defense, 1)
  choice_1_contract = random.randint(1, 3)
  choice_2_contract = random.randint(1, 3)
  choice_3_contract = random.randint(1, 3)
  choice_1_cost = random.randint(1, 8)
  choice_2_cost = random.randint(6, 12)
  choice_3_cost = random.randint(9, 20)
  choice_1_age = random.randint(21, 38)
  choice_2_age = random.randint(21, 38)
  choice_3_age = random.randint(21, 38)
  print(choice_1_pos + " - " + choice_1 + " - " + str(choice_1_offense) + " OFF - " + str(choice_1_defense) + " DEF - " + str(choice_1_contract) + " YRS - " + str(choice_1_age) + " AGE - " + " $" + str(choice_1_cost))
  print(choice_2_pos + " - " + choice_2 + " - " + str(choice_2_offense) + " OFF - " + str(choice_2_defense) + " DEF - " + str(choice_2_contract) + " YRS - " + str(choice_2_age) + " AGE - " + " $" + str(choice_2_cost))
  print(choice_3_pos + " - " + str(choice_3) + " - " + str(choice_3_offense) + " OFF - " + str(choice_3_defense) + " DEF - " + str(choice_3_contract) + " YRS - " + str(choice_1_age) + " AGE - $" + str(choice_3_cost))
  print()
  pick = input("Who would you like to sign? ").lower()
  if pick == choice_1.lower() and money >= choice_1_cost:
    print()
    print("Welcome to the " + team_name + ", " + choice_1 + "!")
    print()
    print_team()
    continuuuu = input("Press Enter to Continue ")
#Substitutes free agent into team for choice 1
    if choice_1_pos == "PG":
      point_guard = choice_1
      point_guard_offense = choice_1_offense
      point_guard_defense = choice_1_defense
      point_guard_contract = choice_1_contract
      point_guard_age = choice_1_age
    elif choice_1_pos == "SG":
      shooting_guard = choice_1
      shooting_guard_offense = choice_1_offense
      shooting_guard_defense = choice_1_defense
      shooting_guard_contract = choice_1_contract
      shooting_guard_age = choice_1_age
    elif choice_1_pos == "SF":
      small_forward = choice_1
      small_forward_offense = choice_1_offense
      small_forward_defense = choice_1_defense
      small_forward_contract = choice_1_contract
      small_forward_age = choice_1_age
    elif choice_1_pos == "PF":
      power_forward = choice_1
      power_forward_offense = choice_1_offense
      power_forward_defense = choice_1_defense
      power_forward_contract = choice_1_contract
      power_forward_age = choice_1_age
    elif choice_1_pos == "C":
      center = choice_1
      center_offense = choice_1_offense
      center_defense = choice_1_defense
      center_contract = choice_1_contract  
      center_age = choice_1_age
  if pick == choice_2.lower() and money >= choice_2_cost:
     print()
     print("Welcome to the " + team_name + ", " + choice_2 + "!")
     print()
     print_team()
     continuuuu = input("Press Enter to Continue ")
     new_money -= choice_2_cost
     money = new_money
#Substitutes free agent into team for choice 2
     if choice_2_pos == "PG":
       point_guard = choice_2
       point_guard_offense = choice_2_offense
       point_guard_defense = choice_2_defense
       point_guard_contract = choice_2_contract
       point_guard_age = choice_2_age
     elif choice_2_pos == "SG":
       shooting_guard = choice_2
       shooting_guard_offense = choice_2_offense
       shooting_guard_defense = choice_2_defense
       shooting_guard_contract = choice_2_contract
       shooting_guard_age = choice_2_age
     elif choice_2_pos == "SF":
       small_forward = choice_2
       small_forward_offense = choice_2_offense
       small_forward_defense = choice_2_defense
       small_forward_contract = choice_2_contract
       small_forward_age = choice_2_age
     elif choice_2_pos == "PF":
       power_forward = choice_2
       power_forward_offense = choice_2_offense
       power_forward_defense = choice_2_defense
       power_forward_contract = choice_2_contract
       power_forward_age = choice_2_age
     elif choice_2_pos == "C":
       center = choice_2
       center_offense = choice_2_offense
       center_defense = choice_2_defense
       center_contract = choice_2_contract
       center_age = choice_2_age
  if pick == choice_3.lower() and money >= choice_3_cost:
     print()
     print("Welcome to the " + team_name + ", " + choice_3 + "!")
     print()
     print_team()
     continuuuu = input("Press Enter to Continue ")
     new_money -= choice_2_cost
     money = new_money
#Substitutes free agent into team for choice 3
     if choice_3_pos == "PG":
       point_guard = choice_3
       point_guard_offense = choice_3_offense
       point_guard_defense = choice_3_defense
       point_guard_contract = choice_3_contract
       point_guard_age = choice_3_age
     elif choice_3_pos == "SG":
       shooting_guard = choice_3
       shooting_guard_offense = choice_3_offense
       shooting_guard_defense = choice_3_defense
       shooting_guard_contract = choice_3_contract
       shooting_guard_age = choice_3_age
     elif choice_3_pos == "SF":
       small_forward = choice_3
       small_forward_offense = choice_3_offense
       small_forward_defense = choice_3_defense
       small_forward_contract = choice_3_contract
       small_forward_age = choice_3_age
     elif choice_3_pos == "PF":
       power_forward = choice_3
       power_forward_offense = choice_3_offense
       power_forward_defense = choice_3_defense
       power_forward_contract = choice_3_contract
       power_forward_age = choice_3_age
     elif choice_3_pos == "C":
       center = choice_3
       center_offense = choice_3_offense
       center_defense = choice_3_defense
       center_contract = choice_3_contract
       center_age = choice_3_age
  return point_guard
  return shooting_guard
  return small_forward
  return power_forward
  return center
  return point_guard_offense
  return shooting_guard_offense
  return small_forward_offense
  return power_forward_offense
  return center_offense
  return point_guard_defense
  return shooting_guard_defense
  return small_forward_defense
  return power_forward_defense
  return center_defense
  return point_guard_contract
  return shooting_guard_contract
  return small_forward_contract
  return power_forward_contract
  return center_contract
  return money 


  

def print_record():
  global team_name
  global team_wins
  global team_losses
  print("The " + team_name + " are " + str(team_wins) + "-" + str(team_losses))



def get_strategy():
  global team_offense_ovr
  global team_defense_ovr
  global random_improvement_age
  practice_success = random.choice(random_improvement_age)
  whattayawant = input("Would you like to run practices with a focus on offense or defense? (OFF, DEF) ").lower()
  print()
  if whattayawant == "offense".lower() or whattayawant == "Off".lower() or whattayawant == "O".lower():
    team_offense_ovr += practice_success
  else:
    team_defense_ovr += practice_success
  if practice_success <= .3:
    print("The practices didn't go so well")
    print()
  elif practice_success >= .3 and practice_success <= 1.1:
    print("The practices went as expected")
    print()
  else:
    print("The practices were very successful")
    print()
  team_offense_ovr = round(team_offense_ovr, 1)
  team_defense_ovr = round(team_defense_ovr, 1)
  return team_offense_ovr
  return team_defense_ovr



width = 800





def start_game_tutorial():
  global point_guard
  global shooting_guard
  global small_forward
  global power_forward
  global center
  global team_offense_ovr
  global team_defense_ovr
  global draft_picks
  global money
  global point_guard_contract
  global shooting_guard_contract
  global small_forward_contract
  global power_forward_contract
  global center_contract
  global team_wins
  global team_losses
  global coach_wins
  global coach_losses
  global coach_chips
  global point_guard_age
  global shooting_guard_age
  global small_forward_age
  global power_forward_age
  global center_age
  global coach_seasons
  global point_guard_rookie
  global shooting_guard_rookie
  global small_forward_rookie
  global power_forward_rookie
  global center_rookie
  global width
  line_1 = textwrap.wrap("This game is simple and entirely text-based. Your goal is to build the best possible team you can by drafting, signing and trading for players with high stats.")
  for line in line_1:
    print(textwrap.fill(line, width))
  print()
  continuuuu = input("Press Enter to Continue ")
  print()
  print("You will start with a roster of randomly generated players. Each player will have 4 stats that you need to pay attention to:")
  print()
  print("OFF represents offense, the higher rating the better.")
  print()
  print("DEF represents defense, the higher rating the better.")
  print()
  line_2 = textwrap.wrap("YRS represents years remaining of a player's contract. When YRS = 0, you will have to choose to either resign that player or replace him with another randomly generated player.")
  for line in line_2:
    print(textwrap.fill(line, width))
  print()
  line_3 = textwrap.wrap("AGE represents the player's age. A young player will improve every offseason, while an older player may regress. Older players also have a higher chance of retiring.")
  for line in line_3:
    print(textwrap.fill(line, width))
  print()
  continuuuu = input("Press Enter to Continue ")
  print()
  line_9 = textwrap.wrap("First, choose your team name and location. If you leave them blank, a random name and location will be assigned to your team.")
  for line in line_9:
    print(textwrap.fill(line, width))
  print()
  continuuuu = input("Press Enter to Continue ")
  print()
  get_team_name()
  global team_name
  print("Take a look at the " + team_name)
  get_team_ovr()
  print()
  print_team()
  continue_game = input("Press Enter to Continue ")
  print()
  line_4 = textwrap.wrap("You will have multiple chances to improve your team. First, you will be able to draft rookies at the draft. When drafting a player, the rookie will immediately replace the player on your roster who shares his position. Rookies always have a contract length of 3 years. To draft a player, you must enter the player's name exactly. If you don't want to draft anyone, press enter.")
  for line in line_4:
    print(textwrap.fill(line, width))
  print()
  continuuuu = input("Press Enter to Continue ")
  print()
  if draft_picks == 1:
    print("Time for the draft! You have " + str(draft_picks) + " pick")
  else:
    print("Time for the draft! You have " + str(draft_picks) + " picks")
  print()
  while draft_picks > 0:
    draft()
  print()
  print("You have no remaining picks.")
  print()
  continue_game = input("Press Enter to Continue ")
  print()
  line_5 = textwrap.wrap("Next, you will be able to sign a free agent. When signing a player, the free agent will immediately replace the player on your roster who shares his position. To sign a player, you must enter the player's name exactly. Signing a player will cost a given amount of money. You begin with $10 and earn an extra $4 - $8 every offseason. If you don't want to sign anyone, press enter.")
  for line in line_5:
    print(textwrap.fill(line, width))
  print()
  continuuuu = input("Press Enter to Continue ")
  print()
  free_agency()
  print()
  get_team_ovr()
  print("Check out the new " + team_name + "!")
  print()
  get_team_ovr()
  print_team()
  print()
  continue_game = input("Press Enter to Continue ")
  print()
  line_8 = textwrap.wrap("Before the season starts, you will be able to boost either your team's offense or defense by a random number through practice. To choose between offense or defense, enter 'OFF' or 'DEF'.")
  for line in line_8:
    print(textwrap.fill(line, width))
  print()
  continuuuu = input("Press Enter to Continue ")
  print()
  get_strategy()
  print_team()
  print()
  continue_game = input("Press Enter to Continue ")
  print()
  line_8 = textwrap.wrap("Every season is 16 games long. You will have a chance at making the playoffs with 8 wins, and will be guaranteed a playoff spot with 10 wins.")
  for line in line_8:
    print(textwrap.fill(line, width))
  print()
  continuuuu = input("Press Enter to Continue ")
  print()
  print("The season is about to begin")
  print()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  line_6 = textwrap.wrap("Finally, you will have one chance to trade one of your players at midseason. If you propose a trade, you will lose your team's boost from practice. To choose which player you're willing to trade, enter the player's position abbreviation (PG, SG, SF, PF, C). You will be offered another player with matching position in exchange for your player and 1 or 2 picks in next year's draft. When asked if you accept the trade, enter 'Yes' to accept it.")
  for line in line_6:
    print(textwrap.fill(line, width))
  print()
  continuuuu = input("Press Enter to Continue ")
  print()
  propose_trade()
  continue_game = input("Press Enter to Continue ")
  print()
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  new_play_game()
  print_record()
  print()
  get_highlights()
  continue_game = input("Press Enter to Continue ")
  print()
  playoff_req = random.randint(8,10)
  if team_wins >= playoff_req:
   print(green(("Congratulations, the " + team_name + " made the playoffs!")))
   print()
   continue_game = input("Press Enter to Continue ")
   print()
   playoffs()
  else:
   print(red("The " + team_name + " have missed the playoffs. Better luck next year"))
   print()
  line_7 = textwrap.wrap("After every season you will be faced with another draft and another round of free agency. You will get an additional $4 - $8 to spend on free agents or renewing contracts and each player on your roster will get 1 year older and lose a year on his current contract. The best player will be awarded MVP and the best rookie will be named Rookie of the Year.")
  for line in line_7:
    print(textwrap.fill(line, width))
  print()
  input("Press Enter to Continue ")
  print()
  get_roty()
  input("Press Enter to Continue ")
  print()
  get_mvp()
  input("Press Enter to Continue ")
  print()
  coach_wins += team_wins
  coach_losses += team_losses
  coach_seasons += 1
  retire()
  draft_picks += 3
  money += random.randint(4,8)
  point_guard_contract -= 1
  shooting_guard_contract -= 1
  small_forward_contract -= 1
  power_forward_contract -= 1
  center_contract -= 1
  team_wins = 0
  team_losses = 0
  point_guard_age += 1
  shooting_guard_age += 1
  small_forward_age += 1
  power_forward_age += 1
  center_age += 1
  new_season()





def begin_program():
  global width
  print_dunk_1()
  print()
  print("Welcome to My GM Basketball!")
  print()
  continuuuu = input("Press Enter to Continue ")
  print()
  tutu_ornah = input("Would you like a tutorial for you first season? (Yes, No) ").lower()
  print()
  if tutu_ornah == "Yes".lower() or tutu_ornah == "Y".lower():
    print()
    start_game_tutorial()
  else:
    print()
    start_game()



team_loc = ["Scranton", "Chicago", "Kingston", "New York", "Tokyo", "Bangkok", "London", "Shanghai", "Dubai", "Singapore", "Hong Kong", "Barcelona", "Melbourne", "Beijing", "Denver", "Boston", "Los Angeles", "Las Vegas", "Berlin", "Rio De Janeiro", "Manchester", "Toronto", "Sydney", "New Orleans", "Kansas City", "Milwaukee", "Charlotte", "Houston", "Atlanta", "Miami", "Orlando", "Cleveland", "Baltimore", "Washington, D.C.", "Minneapolis", "Detroit", "Pheonix", "Indianapolis", "Pittsburgh", "Seattle", "St. Louis", "Dallas", "Philadelphia", "San Francisco", "Newark", "Mexico City", "Cairo", "Buenos Aires", "Lima", "Jacksonville", "Gainesville", "Oklahoma City", "Nashville", "San Antonio", "Louisville", "Memphis", "Charlotte", "Austin", "Tucson", "Columbus", "Granville", "Evanston", "Ocean City", "Providenciales", "San Jose", "Portland", "Salt Lake City", "Stowe", "Brooklyn", "Fort Lauderdale", "Utah", "Vancouver", "Florida", "New England", "East Coast", "West Coast", "Mid Atlantic", "Pacific", "Northeast", "Northwest", "Hawaii", "Honolulu", "Southeast", "Southwest"]
team_adj = ["Red ", "Blue ", "Green ", "Fiery ", "Big ", "Quick ", "Great ", "Yellow ", "Orange ", "Pink ", "Purple ", "Frozen ", "Checkered ", "Striped ", "Dotted ", "Scary ", "Sea ", "Scarlet ", "Screaming ", "Wild ", "Haunted ", "Lethal ", "Mean ", "Mud ", "Raging ", "Deadly ", "Flipping ", "Risky ", "Mad ", "Elite ", "Bloody ", "Robust ", "Mighty ", "Fighting ", "Agile ", "Dead-Eye ", "Dangerous ", "United ", "Magic ", "Hot ", "Baby ", "Daring ", "Shattered ", "Gold ", "Silver ", "Violet ", "Platinum ", "Unbent ", "Invincible ", "Athletic ", "Iron ", "Metal ", "Twisted ", "Crazy ", "Striking ", "Sonic ", "Ice ", "Fire ", "Windy ", "Blazing ", "Smoking ", "Rebel ", "Zombie ", "Patriotic ", "Aero ", "Starry ", "Free ", "Dead ", "Long ", "Gray ", "" , "" , "" , "" , "" , "", "", "", "", "", "", "", "", "Diamond ", "Wood ", "Chrome ", "Lead ", "Mighty ", "Flying ", "River ", "Ocean ", "Desert ", "Sky ", "Armored ", "Unrelenting ", "Fearless ", "Global ", "Genius ", "Butter ", "Electic ", "Hard ", "Rock Solid ", "Wonder ", "Tin ", "Island " "Flash "]
team_noun = ["Devils", "Demons", "Rangers", "Cats", "Rodents", "Knights", "Royals", "Cannons", "Lightning", "Fury", "Talons", "Tigers", "Sharks", "Swordfish", "Trout", "Fire", "Dogs", "Fangs", "Harpoons", "Hooks", "Guns", "Grizzlies", "Snow", "Sky", "Whales", "Whalers", "Dreams", "Captains", "Rampage", "Dinos", "Scorpions", "Spiders", "Turkeys", "Army", "Bones", "Zombies", "Crew", "Force", "Brutes", "Butchers", "Storm", "Bombs", "Gunners", "Hammerheads", "Angels", "Barbarians", "Squad", "Outlaws", "Rebels", "Reapers", "Nightmares", "Kingpins", "Pythons", "Serpents", "Beasts", "Robots", "Cows", "Bullies", "Bullseyes", "Arrows", "Slam", "Magic", "Lava", "Bulls", "Bears", "Thunder", "Helmets","Swords", "Shields", "T-Rexes", "Pelicans", "Seagulls", "Penguins", "Puffins", "Huskies", "Bulldogs", "Miners", "Pandas", "Dragons", "Jackets", "Steel", "Pirates", "Racers", "Reptiles", "Lunatics", "Chasers", "Gangsters", "Cardinals", "Patriots", "Rhinos", "Punches", "Kicks", "Uppercuts", "Piledrivers", "Cyborgs", "Stars", "Fruit", "Tenors", "Assassins", "Titans", "Missiles", "Colts", "Stallions", "Birds", "Eagles", "Divers", "Dynasty", "Comets", "Ducks", "Hawks", "Falcons", "Warriors", "Minnows", "Globes", "Brians", "Bobcats", "Claws", "Hammers", "Biscuits", "Motors", "Eels", "Thunder", "Flamingos", "Gang", "Terror", "Leaves", "Outlaws", "Predators", "Wings", "Boots", "Bees", "Hive", "Minds"]


def new_play_game():
  global team_name
  global team_offense_ovr
  global team_defense_ovr
  global opponent_1
  global opponent_1_off
  global opponent_1_def
  global opponent_2
  global opponent_2_off
  global opponent_2_def
  global opponent_3
  global opponent_3_off
  global opponent_3_def
  global opponent_4
  global opponent_4_off
  global opponent_4_def
  global opponent_5
  global opponent_5_off
  global opponent_5_def
  global team_wins
  global team_losses
  global team_adj
  global team_noun
  global team_loc
  opponent_1_off = random.randint(3,9) + (.1 * (random.randint(0,20)))
  opponent_1_def = random.randint(3,9) + (.1 * (random.randint(0,20)))
  x_factor = (.1 * random.randint(10,35))
  team_offense_performance = team_offense_ovr * x_factor
  team_defense_performance = team_defense_ovr * x_factor
  opponent_off_performance = opponent_1_off * x_factor
  opponent_def_performance = opponent_1_def * x_factor
  opponent_1 = random.choice(team_loc) + " " + random.choice(team_adj) + random.choice(team_noun)
  print(team_name + " - " + str(team_offense_ovr) + " OFF - " + str(team_defense_ovr) + " DEF vs")
  print(opponent_1 + " - " + str(opponent_1_off) + " OFF - " + str(opponent_1_def) + " DEF")
  team_score = random.randint(90,105) + int(team_offense_performance) - int(opponent_def_performance)
  opponent_score = random.randint(90,105) + int(opponent_off_performance) - int(team_defense_performance)
  if team_score > opponent_score:
   see_results = input("Press Enter to Play Game ")
   print(green("The " + team_name + " win " + str(team_score) + " - " + str(opponent_score)))
   team_wins += 1
  elif team_score < opponent_score:
   see_results = input("Press Enter to Play Game ")
   print(red("The " + opponent_1 + " win " + str(opponent_score) + " - " + str(team_score)))
   team_losses += 1
  else:
    see_results = input("Press Enter to Play Game ")
    print(str(team_score) + " - " + str(opponent_score))
    print("The game went into overtime!")
    team_score += random.randint(4,14)
    opponent_score += random.randint(4,14)
    if team_score > opponent_score:
      see_results = input("Press Enter to Play Overtime")
      print(green("The " + team_name + " win " + str(team_score) + " - " + str(opponent_score)))
      team_wins += 1
    elif team_score < opponent_score:
      see_results = input("Press Enter to Play Overtime")
      print(red("The " + opponent_1 + " win " + str(opponent_score) + " - " + str(team_score)))
      team_losses += 1
    else:
      print("The game went into overtime!")
      team_score += random.randint(4,14)
      opponent_score += random.randint(4,14)
      if team_score > opponent_score:
        see_results = input("Press Enter to Play Double Overtime")
        print(green("The " + team_name + " win " + str(team_score) + " - " + str(opponent_score)))
        team_wins += 1
      elif team_score < opponent_score:
        see_results = input("Press Enter to Play Double Overtime")
        print(red("The " + opponent_1 + " win " + str(opponent_score) + " - " + str(team_score)))
        team_losses += 1
      else:
        print("You tied")






def new_play_playoff_game():
  global team_name
  global team_offense_ovr
  global team_defense_ovr
  global opponent_1
  global opponent_1_off
  global opponent_1_def
  global opponent_2
  global opponent_2_off
  global opponent_2_def
  global opponent_3
  global opponent_3_off
  global opponent_3_def
  global opponent_4
  global opponent_4_off
  global opponent_4_def
  global opponent_5
  global opponent_5_off
  global opponent_5_def
  global team_wins
  global team_losses
  global team_adj
  global team_noun
  global team_won_playoffs
  global team_loc
  opponent_1_off = random.randint(6,9) + (.1 * (random.randint(0,10)))
  opponent_1_def = random.randint(6,9) + (.1 * (random.randint(0,10)))
  x_factor = (.1 * random.randint(10,30))
  team_offense_performance = team_offense_ovr * x_factor
  team_defense_performance = team_defense_ovr * x_factor
  opponent_off_performance = opponent_1_off * x_factor
  opponent_def_performance = opponent_1_def * x_factor
  opponent_1 = random.choice(team_loc) + " " + random.choice(team_adj) + random.choice(team_noun)
  print(team_name + " - " + str(team_offense_ovr) + " OFF - " + str(team_defense_ovr) + " DEF vs")
  print(opponent_1 + " - " + str(opponent_1_off) + " OFF - " + str(opponent_1_def) + " DEF")
  team_score = random.randint(92,103) + int(team_offense_performance) - int(opponent_def_performance)
  opponent_score = random.randint(92,103) + int(opponent_off_performance) - int(team_defense_performance)
  if team_score > opponent_score:
   see_results = input("Press Enter to Play Game ")
   print(green("The " + team_name + " win " + str(team_score) + " - " + str(opponent_score)))
   team_wins += 1
   team_won_playoffs = True
  elif team_score < opponent_score:
   see_results = input("Press Enter to Play Game ")
   print(red("The " + opponent_1 + " win " + str(opponent_score) + " - " + str(team_score)))
   team_losses += 1
   team_won_playoffs = False
  else:
    see_results = input("Press Enter to Play Game ")
    print(str(team_score) + " - " + str(opponent_score))
    print("The game went into overtime!")
    team_score += random.randint(4,14)
    opponent_score += random.randint(4,14)
    if team_score > opponent_score:
      see_results = input("Press Enter to Play Overtime")
      print(green("The " + team_name + " win " + str(team_score) + " - " + str(opponent_score)))
      team_wins += 1
    elif team_score < opponent_score:
      see_results = input("Press Enter to Play Overtime")
      print(red("The " + opponent_1 + " win " + str(opponent_score) + " - " + str(team_score)))
      team_losses += 1
    else:
      print("The game went into double overtime!")
      team_score += random.randint(4,14)
      opponent_score += random.randint(4,14)
      if team_score > opponent_score:
        see_results = input("Press Enter to Play Double Overtime")
        print(green("The " + team_name + " win " + str(team_score) + " - " + str(opponent_score)))
        team_wins += 1
      elif team_score < opponent_score:
        see_results = input("Press Enter to Play Double Overtime")
        print(red("The " + opponent_1 + " win " + str(opponent_score) + " - " + str(team_score)))
        team_losses += 1
      else:
        print("You tied")




def get_mvp():
  global point_guard
  global shooting_guard
  global small_forward
  global power_forward
  global center
  global point_guard_offense
  global shooting_guard_offense
  global small_forward_offense
  global power_forward_offense
  global center_offense
  global point_guard_defense
  global shooting_guard_defense
  global small_forward_defense
  global power_forward_defense
  global center_defense
  global team_wins
  global team_name
  global first_name
  global last_name
  global team_adj
  global team_noun
  global coach_mvps
  mvp_name = random.choice(first_name) + " " + random.choice(last_name)
  fake_team_name = random.choice(team_loc) + " " + random.choice(team_adj) + random.choice(team_noun)
  mvp_wins_req = random.randint(5,9)
  mvp_player_req = (20 + (.1 * random.randint(0,100)))
  if team_wins >= mvp_wins_req:
    if point_guard_offense + point_guard_defense + team_wins >= mvp_player_req:
      print(point_guard + " of the " + team_name + " has been named MVP! You should be proud")
      coach_mvps += 1
    elif shooting_guard_offense + shooting_guard_defense + team_wins >= mvp_player_req:
      print(shooting_guard + " of the " + team_name + " has been named MVP! You should be proud")
      coach_mvps += 1
    elif small_forward_offense + small_forward_defense + team_wins >= mvp_player_req:
      print(small_forward + " of the " + team_name + " has been named MVP! You should be proud")
      coach_mvps += 1
    elif power_forward_offense + power_forward_defense + team_wins >= mvp_player_req:
      print(power_forward + " of the " + team_name + " has been named MVP! You should be proud")
      coach_mvps += 1
    elif center_offense + center_defense + team_wins >= mvp_player_req:
      print(center + " of the " + team_name + " has been named MVP! You should be proud")
      coach_mvps += 1
    else:
      print(mvp_name + " of the " + fake_team_name + " has been named MVP")
    print()
  else:
    print(mvp_name + " of the " + fake_team_name + " has been named MVP")
    print()



point_guard_rookie = False
shooting_guard_rookie = False
small_forward_rookie = False
power_forward_rookie = False
center_rookie = False


coach_rotys = 0

def get_roty():
  global point_guard
  global shooting_guard
  global small_forward
  global power_forward
  global center
  global point_guard_offense
  global shooting_guard_offense
  global small_forward_offense
  global power_forward_offense
  global center_offense
  global point_guard_defense
  global shooting_guard_defense
  global small_forward_defense
  global power_forward_defense
  global center_defense
  global team_wins
  global team_name
  global first_name
  global last_name
  global team_adj
  global team_noun
  global coach_rotys
  global point_guard_rookie
  global shooting_guard_rookie
  global small_forward_rookie
  global power_forward_rookie
  global center_rookie
  mvp_name = random.choice(first_name) + " " + random.choice(last_name)
  fake_team_name = random.choice(team_loc) + " " + random.choice(team_adj) + random.choice(team_noun)
  mvp_wins_req = random.randint(1,5)
  mvp_player_req = (13.5 + (.1 * random.randint(0,100)))
  if team_wins >= mvp_wins_req:
    if point_guard_offense + point_guard_defense + team_wins >= mvp_player_req and point_guard_rookie == True:
      print(point_guard + " of the " + team_name + " has been named Rookie of the Year! You should be proud")
      coach_rotys += 1
      print()
    elif shooting_guard_offense + shooting_guard_defense + team_wins >= mvp_player_req and point_guard_rookie == True:
      print(shooting_guard + " of the " + team_name + " has been named Rookie of the Year! You should be proud")
      coach_rotys += 1
      print()
    elif small_forward_offense + small_forward_defense + team_wins >= mvp_player_req and point_guard_rookie == True:
      print(small_forward + " of the " + team_name + " has been named Rookie of the Year! You should be proud")
      coach_rotys += 1
      print()
    elif power_forward_offense + power_forward_defense + team_wins >= mvp_player_req and point_guard_rookie == True:
      print(power_forward + " of the " + team_name + " has been named Rookie of the Year! You should be proud")
      coach_rotys += 1
      print()
    elif center_offense + center_defense + team_wins >= mvp_player_req and point_guard_rookie == True:
      print(center + " of the " + team_name + " has been named Rookie of the Year! You should be proud")
      coach_rotys += 1
      print()
    else:
      print(mvp_name + " of the " + fake_team_name + " has been named Rookie of the Year")
    print()
  else:
    print(mvp_name + " of the " + fake_team_name + " has been named Rookie of the Year")
    print()







begin_program()