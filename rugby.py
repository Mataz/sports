# Scrape the last 10 results of the Aviva Premiership Rugby on flashscore.com

from selenium import webdriver

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\chromedriver.exe')
driver.implicitly_wait(15)
driver.get('https://www.flashscore.com/rugby-union/england/aviva-premiership-rugby/')

event_date = driver.find_elements_by_css_selector('td.cell_ad.time')
dates = [x.text for x in event_date][:10]
print(dates)        # test

home_team = driver.find_elements_by_css_selector('td.cell_ab.team-home')
home_teams = [x.text for x in home_team][:10]
print(home_teams)   # test

away_team = driver.find_elements_by_css_selector('td.cell_ac.team-away')
away_teams = [x.text for x in away_team][:10]
print(away_teams)   # test

event_score = driver.find_elements_by_css_selector('td.cell_sa.score.bold')
scores = [x.text for x in event_score][:10]
print(scores)       # test

print('Latest scores for the Aviva Premiership Rugby')
for date, home_team, away_team, score in zip(dates, home_teams, away_teams, scores):
    print(str(date) + ' | ' + str(home_team) + ' - ' + str(away_team) + ' | ' + str(score) + '\n')





