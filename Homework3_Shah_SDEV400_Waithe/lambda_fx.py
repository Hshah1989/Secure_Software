Python/AWS Lambda API integration/lambda_function.py /

  
# Name: Hiren Shah
# Date: 9/25/2021
# Class: SDEV 400
# Professor: Waithe

import json
import logging
import boto3


BUCKET = 'sports-data89'
DATA_SETS = {
    'NBA': 'NBA.json',
    'NFL': 'NFL.json',
    'NHL': 'NHL.json'
}


if len(logging.getLogger().handlers) > 0:
    # The Lambda environment pre-configures a handler logging to stderr.
    # If a handler is already configured,
    # `.basicConfig` does not execute. Thus we set the level directly.
    logging.getLogger().setLevel(logging.INFO)
else:
    logging.basicConfig(level=logging.INFO)
# logging.getLogger().setLevel(logging.INFO)



def lambda_handler(event, context):
    """
    Lambda Event Function
    """

    sport = None
    team = None
    message = "Sport is not recognized. Please try either NBA, NHL, or NFL."

    # Uses this code to get URL Vars when running through API Gateway
    if 'params' in event and 'querystring' in event['params']:
        if 'sport' in event['params']['querystring']:
            sport = event['params']['querystring']['sport']
        if 'team' in event['params']['querystring']:
            team = event['params']['querystring']['team']

    # Uses this code to get URL Vars when running through "TEST" button
    # in LAMBDA Console
    if 'sport' in event:
        sport = event['sport']

    if 'team' in event:
        team = event['team']

    if sport is None or team is None:
        message = "sport and team abbreviations are required." +\
                  "Try adding the following to the URL: ?team=WAS&sport=NBA"
    elif sport.upper() in ('NBA', 'NFL', 'NHL'):
        # For looking up the JSON data in S3
        # s3_resource_handle = boto3.resource('s3')

        # KEY is json file associated with the sport (i.e., NBA, NHL, etc.)
        KEY = DATA_SETS[sport.upper()]
        # calls read_s3() function and returns associated info for message
        info = read_s3(KEY, team.upper())

        message = "The team {} for the sport {}. RESULTS: {}".format(team.upper(),
        sport.upper(), info)

    return {
        'statusCode': 200,
        'message': message,
    }



def read_s3(KEY, team):
    """
    Reads S3 files for Sports and Teams info
    """

    try:
        s3 = boto3.resource('s3')
        content_object = s3.Object(BUCKET, KEY)
        file_content = content_object.get()['Body'].read().decode('utf-8')
        json_content = json.loads(file_content)
        info = json_content


        # get all the dates for sport
        dates = []
        for record in info:
            dates.append(record)

        # check if team search for exists for sport
        games = []
        teams = []
        for date in dates:
            for game in info[date]:
                teams.append(game['away_abbr'].upper())
                teams.append(game['home_abbr'].upper())

        teams = set(teams)  # get only unique teams by casting list to set

        if team not in teams:
            info = "Team {} not found. Try one of the following teams: {}".format(team, teams)
        else:
            # get relevant data from each sport date event, including:
            # teams that played, scores, and who won
            team_scores = []
            team_name = ''
            opposing_team = []
            opposing_team_names = []
            opposing_team_scores = []
            game_dates = []
            game_outcomes = []
            count = 0
            for date in dates:
                if count > 4:
                    break
                for game in info[date]:
                    # if team searched for is the away team
                    if team == game['away_abbr'].upper():
                        game_dates.append(game['boxscore'][4:6] +'/'
                        + game['boxscore'][6:8] +'/'
                        + game['boxscore'][:4])
                        team_name = game['away_name']
                        team_scores.append(game['away_score'])
                        opposing_team.append(game['home_abbr'].upper())
                        opposing_team_names.append(game['home_name'])
                        opposing_team_scores.append(game['home_score'])
                        if team == game['winning_abbr'].upper():
                            game_outcomes.append('beat')
                        else:
                            game_outcomes.append('lost to')
                        count += 1

                    # if team searched for is the home team
                    elif team == game['home_abbr'].upper():
                        game_dates.append(game['boxscore'][4:6] +'/'
                        + game['boxscore'][6:8] +'/'
                        + game['boxscore'][:4])
                        team_name = game['home_name']
                        team_scores.append(game['home_score'])
                        opposing_team.append(game['away_abbr'].upper())
                        opposing_team_names.append(game['away_name'])
                        opposing_team_scores.append(game['away_score'])
                        if team == game['winning_abbr'].upper():
                            game_outcomes.append('beat')
                        else:
                            game_outcomes.append('lost to')
                        count += 1

                    # if team searched for did not play on this date
                    else:
                        pass

            # the end user message
            info = f"In the last 5 games, {team_name} ({team}) {game_outcomes[0]} {opposing_team_names[0]} ({opposing_team[0]}) with {team_scores[0]} to {opposing_team_scores[0]} on {game_dates[0]}, {team_name} ({team}) {game_outcomes[1]} {opposing_team_names[1]} ({opposing_team[1]}) with {team_scores[1]} to {opposing_team_scores[1]} on {game_dates[1]}, {team_name} ({team}) {game_outcomes[2]} {opposing_team_names[2]} ({opposing_team[2]}) with {team_scores[2]} to {opposing_team_scores[2]} on {game_dates[2]}, {team_name} ({team}) {game_outcomes[3]} {opposing_team_names[3]} ({opposing_team[3]}) with {team_scores[3]} to {opposing_team_scores[3]} on {game_dates[3]}, and {team_name} ({team}) {game_outcomes[4]} {opposing_team_names[4]} ({opposing_team[4]}) with {team_scores[4]} to {opposing_team_scores[4]} on {game_dates[4]}"

    except IndexError as err:
        info = "Error: ", err

    return info
