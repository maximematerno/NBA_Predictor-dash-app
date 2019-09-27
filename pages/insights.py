import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """        
            #### What determines the salary rate of the NBA Players?
            According to the top 5 features in the graph below, more than 50% of salary variance depends on Age and College.           
            """,
        className='mb-4'),
        (
            html.Img(src='assets/Top5Features.png', style= {'width': '40%', 'display': 'inline-block'}, alt="Responsive image", className='mb-4')          
        ),
        dcc.Markdown(
            """        
            To help interpret and determine the significance of the features included in the model, permutation importances were used.
            Notice that the most important feature is age followed by college. An aspiring professsional basketball should keep in mind age and college when trying to increase their salary.          
            """,
        className='mb-4'),
        (
            html.Img(src='assets/PermutationImportance.png', style= {'width': '40%', 'display': 'inline-block'}, alt="Responsive image", className='mb-4')          
        ),
        dcc.Markdown(
            """        
            Partial Dependence Plots show exactly when a feature weight has high concentrations. We can see that between 24 at 30 years old the NBA players get paid a higher salary.        
            """,
        className='mb-4'),
        (
            html.Img(src='assets/PartialDependPlot.png', style= {'width': '40%', 'display': 'inline-block'}, alt="Responsive image", className='mb-4')          
        ),
        dcc.Markdown(
            """        
            We can see on the Partial Dependence Plot that between more you are heavier more you will get pay.           
            """,
        className='mb-4'),
        (
            html.Img(src='assets/PartialDependWeight.png', style= {'width': '40%', 'display': 'inline-block'}, alt="Responsive image", className='mb-4')          
        ),
        dcc.Markdown(
            """
            In conclusion, a Random Forest model was used to predict NBA salary given the following features; age, college, weight, height, and position. From the feature importance and partial dependancy graphs
            one can see that age and college are the top 2 features in determining salary. In the Shaply plot one can observe each feature's weighted value in the prediction.
            """,   
        className='mb-4'),
        (
            html.Img(src="assets/Shaply.PNG", style= {'width': '75%', 'display': 'inline-block'}, alt="Responsive image")
        )      
    ],
)

layout = dbc.Row([column1])