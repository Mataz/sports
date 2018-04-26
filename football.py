from selenium import webdriver

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\chromedriver.exe')
driver.implicitly_wait(15)
driver.get('https://www.soccer24.com/europe/champions-league/results/')     # Importan - Have to wait in order to properly scrape

event_round = driver.find_elements_by_class_name('event_round')
rounds = [x.text for x in event_round][:3]

print(rounds)       # test if rounds works

event_date = driver.find_elements_by_css_selector('td.cell_ad.time')
dates = [x.text for x in event_date][:26]

print(dates)        # test if dates works

home_team = driver.find_elements_by_css_selector('td.cell_ab.team-home')
home_teams = [x.text for x in home_team][:26]

print(home_teams)        # test if home_teams works

away_team = driver.find_elements_by_css_selector('td.cell_ac.team-away')
away_teams = [x.text for x in away_team][:26]

print(away_teams)       # test if away_teams works

event_score = driver.find_elements_by_css_selector('td.cell_sa.score.bold')
scores = [x.text for x in event_score][:26]

print(scores)           # test if scores works

for date, home_team, away_team, score in zip(dates, home_teams, away_teams, scores):
    print(str(date) + ' | ' + str(home_team) + ' - ' + str(away_team) + ' | ' + str(score) + '\n')


