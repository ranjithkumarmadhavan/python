# import pandas as pd
import random
import time

# teamA = pd.read_csv("teamA.csv")
# teamB = pd.read_csv("teamB.csv")

teamA = "INDIA"
teamA_playing_11 = ["Shubman Gill", "Rohit Sharma", "Cheteshwar Pujara", "Ajinkya Rahane", "Rishabh Pant", "Wriddhiman Saha", "R Ashwin", "Mohammed Siraj", "Navdeep Saini", "Shardul Thakur", "T Natarajan"]
teamB = "AUSTRALIA"
teamB_playing_11 = ["Marcus Harris", "David Warner", "Marnus Labuschagne", "Steve Smith", "Mathew Wade", "Cameron Green", "Tim Paine", "Pat Cummins", "Mitchell Starc", "Nathan Lyon", "Josh Hazlewood"]

# toss
toss = random.randint(0,1)
options = ["bat","bowl"]

choose_to = random.choice(options)

print('#'*3 + "SUPER OVER" + '#'*3)
print('#'*3 + "INDIA vs AUSTRALIA" + '#'*3)

first_batting_team = None
first_batting_playing_11 = None
second_batting_team = None
second_batting_playing_11 = None

if toss == 0:
    print("INDIA won the toss and choose to {0}".format(choose_to))
    if choose_to == "bat":
        first_batting_team = teamA
        first_batting_playing_11 = teamA_playing_11
        second_batting_team = teamB
        second_batting_playing_11 = teamB_playing_11
    else:
        first_batting_team = teamB
        first_batting_playing_11 = teamB_playing_11
        second_batting_team = teamA
        second_batting_playing_11 = teamA_playing_11
else:
    print("AUSTRALIA won the toss and choose to {0}".format(choose_to))
    if choose_to == "bat":
        first_batting_team = teamB
        first_batting_playing_11 = teamB_playing_11
        second_batting_team = teamA
        second_batting_playing_11 = teamA_playing_11
    else:
        first_batting_team = teamA
        first_batting_playing_11 = teamA_playing_11
        second_batting_team = teamB
        second_batting_playing_11 = teamB_playing_11

#first innings
bowler_name = random.choice(second_batting_playing_11[-4:])
print("Bowler - {}".format(bowler_name))
on_field_batsmen = {
    "on_strike" : first_batting_playing_11[0],
    "off_strike" : first_batting_playing_11[1]
}
target = 0
for ball in range(1,7):
    print("{0} to {1}".format(bowler_name, on_field_batsmen['on_strike']))
    current_ball_run = random.randint(0,6)
    target += current_ball_run
    time.sleep(1)
    print("Ball - {0}, runs - {1}".format(ball, current_ball_run))
    if current_ball_run%2 != 0:
        temp = on_field_batsmen['on_strike']
        on_field_batsmen['on_strike'] = on_field_batsmen['off_strike']
        on_field_batsmen['off_strike'] = temp

print("{0} Posted a target of {1}".format(first_batting_team, target))

#chase
bowler_name = random.choice(first_batting_playing_11[-4:])
print("Bowler - {}".format(bowler_name))
on_field_batsmen = {
    "on_strike" : second_batting_playing_11[0],
    "off_strike" : second_batting_playing_11[1]
}
chase = 0
for ball in range(1,7):
    print("{0} to {1}".format(bowler_name, on_field_batsmen['on_strike']))
    current_ball_run = random.randint(0,6)
    chase += current_ball_run
    time.sleep(1)
    print("Ball - {0}, runs - {1}".format(ball, current_ball_run))
    if chase > target:
        break
    if current_ball_run%2 != 0:
        temp = on_field_batsmen['on_strike']
        on_field_batsmen['on_strike'] = on_field_batsmen['off_strike']
        on_field_batsmen['off_strike'] = temp

print("{0} scored {1}".format(second_batting_team, chase))

#result
if target > chase:
    print("{} WON!!".format(first_batting_team))
elif chase > target:
    print("{} WON!!".format(second_batting_team))
else:
    print("SCORE IS LEVEL!!")