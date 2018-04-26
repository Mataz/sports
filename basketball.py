# Scrape the last 10 results for the NBA on soccer24.com

from selenium import webdriver

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\chromedriver.exe')
driver.implicitly_wait(15)                  # Important - Have to wait in order to properly scrape
driver.get('https://www.basketball24.com/usa/nba/results/')

event_date = driver.find_elements_by_css_selector('td.cell_ad.time')
dates = [x.text for x in event_date][:10]

home_team = driver.find_elements_by_css_selector('td.cell_ab.team-home')
home_teams = [x.text for x in home_team][:10]

away_team = driver.find_elements_by_css_selector('td.cell_ac.team-away')
away_teams = [x.text for x in away_team][:10]

event_score = driver.find_elements_by_css_selector('td.cell_sa.score.bold')
scores = [x.text for x in event_score][:10]

print('Last 10 results for the NBA')
for date, home_team, away_team, score in zip(dates, home_teams, away_teams, scores):
    print(str(date) + ' | ' + str(home_team) + ' - ' + str(away_team) + ' | ' + str(score) + '\n')