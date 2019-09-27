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
            ## Modeling Process - Takeaways
            --------------------------------------------------------------
                
            * ### Cleaning:  
            ![](assets/DF.png)
            This dataset is the NBA data information is from Kaggle.
            This NBA dataset was taken from Kaggle.  
            &emsp;
     
            * ### Goal/Baseline:
            The goal is to predict the expected salary for given variables such as position, age, height, weight and US Colleges.
            To prepare for the predictive model, the data was split randomely. 
            A Mean Baseline was used for the baseline model with the `Mean Absolute Error`
            and `R^2 score`.

            ```
            target = 'Salary'
            y = df[target]
            y_pred = [y.mean()] * len(y)
            print('Mean Baseline:')
            print('Mean Absolute Error', mean_absolute_error(y, y_pred))
            print('R^2 score', r2_score(y, y_pred))
            ```
            `MAE: 3,993,180.17` and `R^2: 0.0`
             
            &emsp;
            * ### RandomForestRegressor:
            To improve the model's prediction R^2 score', a RandomForest model, `RandomForestRegressor`, was chosen.
            After prepping the data with `SimpleImputer` and `OrdinalEncoder` the final model was tested
            on the validation set.
            ```
            pipeline = make_pipeline(
            ce.OrdinalEncoder(),
            SimpleImputer(strategy='median'),
            RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
            )

            # Fit on train , score on val 
            pipeline.fit(X_train, y_train)
            y_pred = pipeline.predict(X_validate)
            print('Mean Absolute Error', mean_absolute_error(y_validate, y_pred))
            print('R^2 score', r2_score(y_validate, y_pred))
            
            ```
            `RandomForestRegressor R^2`: __0.87__
            
            The score was heavily improved, and the dataset was chosen to fit the full train and validation data in order to finally predict the test data.
            ```
            pipeline = make_pipeline(
            ce.OrdinalEncoder(),
            SimpleImputer(strategy='median'),
            RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
            )

            # Fit on train , score on val 
            pipeline.fit(X_train, y_train)
            y_pred = pipeline.predict(X_test)
            print('Mean Absolute Error', mean_absolute_error(y_test, y_pred))
            print('R^2 score', r2_score(y_test, y_pred))
            ```
            `RandomForestRegressor R^2`: __0.8713__
            Further analysis of the predictions can be shown in the [Insights](http://127.0.0.1:8050/insights) page.   
            &emsp;
            * ### Takeaways

            It is important to observe the dataset to figure out how to properly clean the data before performing feature engineering. Also, to validate a classifier model we use the accuracy score and to validate a regression model we use the R^2 value.
            
            1. Before doing any data science on a dataset, we must throroughly try to understand the features and labels(if they exists) within the dataset. This means researching the techincal definitions,
            looking at features datatypes, and asking questions about what results/insights we would like to distill out of the data.
            
            2. Start with a simple model to baseline what is possible and then begin to improve the model and/or hyperparameters. Incremental improvements are the best way to get to the desired outcome.
            
            3. A clean and well-documented jupyter notebook helps keep the workflow understandable, shareable, and streamlines problem solving. This saves time in the long run.
            
            """
            
        ),

    ],
)

layout = dbc.Row([column1])