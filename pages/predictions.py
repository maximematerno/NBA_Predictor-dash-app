import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
from app import app
import pandas as pd

pipeline = load('assets/pipeline.joblib')

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions


            """, className='mb-3'
        ),
        dcc.Markdown('#### Age'),
        dcc.Slider(
            id='Age',
            min=19, 
            max=40, 
            step=5, 
            value=41, 
            marks={n: str(n) for n in range(19,41,1)},
            className='mb-5',  
        ),
        dcc.Markdown('#### Position'), 
        dcc.Dropdown(
            id='Position',
            options = [
                {'label': 'PG', 'value': 'PG'}, 
                {'label': 'SF', 'value': 'SF'}, 
                {'label': 'PF', 'value': 'PF'}, 
                {'label': 'SG', 'value': 'SG'}, 
                {'label': 'C', 'value': 'C'}, 
            ],
            value = 'PG',
            className='mb-5',

            ),
            dcc.Markdown('#### Height'), 
        dcc.Dropdown(
            id='Height',
            options = [
                {'label': 5.11, 'value': 5.11}, 
                {'label': 6, 'value': 6}, 
                {'label': 6.1, 'value': 6.1}, 
                {'label': 6.2, 'value': 6.2},
                {'label': 6.3, 'value': 6.3}, 
                {'label': 6.4, 'value': 6.4}, 
                {'label': 6.5, 'value': 6.5},
                {'label': 6.6, 'value': 6.6},
                {'label': 6.7, 'value': 6.7}, 
                {'label': 6.8, 'value': 6.8}, 
                {'label': 6.9, 'value': 6.9},  
                {'label': 7, 'value': 7},
                {'label': 7.1, 'value': 7.1},
                {'label': 7.2, 'value': 7.2},
                {'label': 7.3, 'value': 7.3}, 
            ],
            value = 5.11,
            className='mb-5',

            ),
        dcc.Markdown('#### Weight'),
        dcc.Slider(
            id='Weight',
            min=160, 
            max=300, 
            step=5, 
            value=41, 
            marks={n: str(n) for n in range(160,301,10)},
            className='mb-5',  
        ),
             dcc.Markdown('#### College'), 
        dcc.Dropdown(
            id='College',
            options = [
                {'label': 'Texas', 'value': 'Texas'}, 
                {'label': 'Marquette', 'value': 'Marquette'}, 
                {'label': 'Boston University', 'value': 'Boston University'}, 
                {'label': 'Georgia State', 'value': 'Georgia State'}, 
                {'label': 'LSU', 'value': 'LSU'}, 
                {'label': 'Gonzaga', 'value': 'Gonzaga'}, 
                {'label': 'Louisville', 'value': 'Louisville'}, 
                {'label': 'Oklahoma State', 'value': 'Oklahoma State'}, 
                {'label': 'Ohio State', 'value': 'Ohio State'}, 
                {'label': 'Washington', 'value': 'Washington'}, 
                {'label': 'Kentucky', 'value': 'Kentucky'}, 
                {'label': 'North Carolina', 'value': 'North Carolina'}, 
                {'label': 'Arizona', 'value': 'Arizona'}, 
                {'label': 'Georgia Tech', 'value': 'GGeorgia Tech'}, 
                {'label': 'Cincinnati', 'value': 'Cincinnati'}, 
                {'label': 'Miami (FL)', 'value': 'Miami (FL)'}, 
                {'label': 'Stanford', 'value': 'Stanford'}, 
                {'label': 'Syracuse', 'value': 'Syracuse'}, 
                {'label': 'Saint Louis', 'value': 'Saint Louis'}, 
                {'label': 'Kansas', 'value': 'Kansas'}, 
                {'label': 'Georgetown', 'value': 'Georgetown'}, 
                {'label': 'Texas A&M', 'value': 'Texas A&M'}, 
                {'label': 'UCLA', 'value': 'UCLA'}, 
                {'label': 'UNLV', 'value': 'UNLV'}, 
                {'label': 'Wichita State', 'value': 'Wichita State'}, 
                {'label': "Saint Joseph's", 'value': "Saint Joseph's"}, 
                {'label': 'Notre Dame', 'value': 'Notre Dame'}, 
                {'label': 'Duke', 'value': 'Duke'}, 
                {'label': 'Murray State', 'value': 'Murray State'}, 
                {'label': 'Tennessee State', 'value': 'Tennessee State'}, 
                {'label': 'Bowling Green', 'value': 'Bowling Green'}, 
                {'label': 'Purdue', 'value': 'Purdue'}, 
                {'label': 'Wake Forest', 'value': 'Wake Forest'}, 
                {'label': 'Michigan', 'value': 'Michigan'}, 
                {'label': 'Missouri', 'value': 'Missouri'},
                {'label': 'USC', 'value': 'USC'}, 
                {'label': 'Villanova', 'value': 'Villanova'}, 
                {'label': 'Rider', 'value': 'Rider'}, 
                {'label': 'Utah', 'value': 'Utah'}, 
                {'label': 'Belmont', 'value': 'Belmont'}, 
                {'label': 'Davidson', 'value': 'Davidson'}, 
                {'label': 'Vanderbilt', 'value': 'Vanderbilt'}, 
                {'label': 'Michigan State', 'value': 'Michigan State'}, 
                {'label': 'Florida', 'value': 'Florida'}, 
                {'label': 'Washington State', 'value': 'Washington State'}, 
                {'label': 'Arizona State', 'value': 'Arizona State'}, 
                {'label': 'Oklahoma', 'value': 'Oklahoma'}, 
                {'label': 'Wyoming', 'value': 'Wyoming'}, 
                {'label': "St. John's", 'value': "St. John's"}, 
                {'label': 'Maryland', 'value': 'Maryland'}, 
                {'label': 'Wisconsin', 'value': 'Wisconsin'}, 
                {'label': 'Utah Valley', 'value': 'Utah Valley'}, 
                {'label': 'North Carolina State', 'value': 'North Carolina State'}, 
                {'label': 'UC Santa Barbara', 'value': 'UC Santa Barbara'}, 
                {'label': 'Baylor', 'value': 'Baylor'}, 
                {'label': 'Connecticut', 'value': 'Connecticut'}, 
                {'label': 'Oregon State', 'value': 'Oregon State'}, 
                {'label': 'New Mexico', 'value': 'New Mexico'}, 
                {'label': 'Oregon', 'value': 'Oregon'}, 
                {'label': 'Creighton', 'value': 'Creighton'}, 
                {'label': 'Arkansas', 'value': 'Arkansas'}, 
                {'label': 'Memphis', 'value': 'Memphis'}, 
                {'label': "Saint Mary's", 'value': "Saint Mary's"}, 
                {'label': 'Tennessee', 'value': 'Tennessee'}, 
                {'label': 'Alabama', 'value': 'Alabama'}, 
                {'label': 'Georgia', 'value': 'Georgia'}, 
                {'label': 'Colorado', 'value': 'Colorado'}, 
                {'label': 'Boston College', 'value': 'Boston College'}, 
                {'label': 'Temple', 'value': 'Temple'}, 
                {'label': 'Fresno State', 'value': 'Fresno State'}, 
                {'label': 'IUPUI', 'value': 'IUPUI'},  
                {'label': 'Eastern Washington', 'value': 'Eastern Washington'}, 
                {'label': 'Western Michigan', 'value': 'Western Michigan'}, 
                {'label': 'Virginia', 'value': 'Virginia'}, 
                {'label': 'Northeastern', 'value': 'Northeastern'}, 
                {'label': 'Western Kentucky', 'value': 'Western Kentucky'}, 
                {'label': 'Nevada', 'value': 'Nevada'}, 
                {'label': 'Illinois', 'value': 'Illinois'}, 
                {'label': 'Kansas State', 'value': 'Kansas State'}, 
                {'label': 'Charleston', 'value': 'Charleston'}, 
                {'label': 'Clemson', 'value': 'Clemson'}, 
                {'label': 'Blinn College', 'value': 'Blinn College'}, 
                {'label': 'Providence', 'value': 'Providence'}, 
                {'label': '123456', 'value': '123456'}, 
                {'label': 'Detroit', 'value': 'Detroit'}, 
                {'label': 'Rhode Island', 'value': 'Rhode Island'}, 
                {'label': 'California', 'value': 'California'}, 
                {'label': 'Cleveland State', 'value': 'Cleveland State'}, 
                {'label': 'Iowa State', 'value': 'Iowa State'}, 
                {'label': 'Florida State', 'value': 'Florida State'}, 
                {'label': 'Long Beach State', 'value': 'Long Beach State'}, 
                {'label': 'Penn State', 'value': 'Penn State'}, 
                {'label': 'Indiana', 'value': 'Indiana'}, 
                {'label': 'San Diego State', 'value': 'San Diego State'}, 
                {'label': 'Western Carolina', 'value': 'Western Carolina'}, 
                {'label': 'Houston', 'value': 'Houston'}, 
                {'label': 'Xavier', 'value': 'Xavier'}, 
                {'label': 'Old Dominion', 'value': 'Old Dominion'}, 
                {'label': 'Minnesota', 'value': 'Minnesota'}, 
                {'label': 'Louisiana Tech', 'value': 'Louisiana Tech'},
                {'label': 'Bucknell', 'value': 'Bucknell'}, 
                {'label': 'Pittsburgh', 'value': 'Pittsburgh'}, 
                {'label': 'St. Bonaventure', 'value': 'St. Bonaventure'}, 
                {'label': 'Louisiana-Lafayette', 'value': 'Louisiana-Lafayette'},
                {'label': 'Colorado State', 'value': 'Colorado State'}, 
                {'label': 'Virginia Tech', 'value': 'Virginia Tech'}, 
                {'label': 'DePaul', 'value': 'DePaul'}, 
                {'label': 'Morehead State', 'value': 'Morehead State'},
                {'label': 'Central Michigan', 'value': 'Central Michigan'}, 
                {'label': 'Weber State', 'value': 'Weber State'}, 
                {'label': 'Lehigh', 'value': 'Lehigh'}, 
                {'label': 'Westchester CC', 'value': 'Westchester CC'}, 
                {'label': 'Dayton', 'value': 'Dayton'},
                {'label': 'Butler', 'value': 'Butler'}, 
            ],
            value = 'Texas',

        ),
    ],
    md=7,
)

column2 = dbc.Col(
    [
        html.H2('Expected Salary', className='mb-5'), 
        html.Div(id='prediction-content', className='lead'),
        html.Img(src='assets/athletes-ball-basketball-163267.jpg', className='img-fluid')
    ]
)

layout = dbc.Row([column1, column2])


@app.callback(
    Output('prediction-content', 'children'),
    [Input('Age', 'value'), Input('Position', 'value'),Input('College', 'value'),Input('Height', 'value'),Input('Weight', 'value')],
)
def predict(Age, Position, College, Height, Weight):
    df = pd.DataFrame(
        columns=['Age', 'Position','College', 'Height','Weight'], 
        data=[[Age, Position, College, Height, Weight]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'${y_pred:10,.0f} salary'