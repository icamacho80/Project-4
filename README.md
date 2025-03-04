# Project-4: US Real EState Market – Housing price prediction​

Project4- Jennifer Ilyayeva, Idrees Andarr., Ingrid Camacho


# Data Model Implementation :
A Python script initializes, trains, and evaluates a model.

The data is cleaned, normalized, and standardized before modeling.

The model utilizes data retrieved from SQL or Spark.

The model demonstrates meaningful predictive power at least 75% classification accuracy or 0.80 R-squared.

# Data Model Optimization:
The model optimization and evaluation process, showing iterative changes made to the model and the resulting changes in model performance, is documented in either a CSV/Excel table or the Python script.

Overall model performance is printed or displayed at the end of the script.

# GitHub Documentation:
GitHub repository is free of unnecessary files and folders and has an appropriate .gitignore in use.

The README is customized as a polished presentation of the project's content.

# Group Presentation:
All group members speak during the presentation.

Content, transitions, and conclusions flow smoothly within any time restrictions.

The content is relevant to the project.

The presentation maintains audience interest.

# Model Performance Metrics:
Model: Gradient Boosting Regressor Parameters:
•	n_estimators = 300
•	learning_rate = 0.1
•	max_depth = 5
•	random_state = 42

# Evaluation Metrics:
•	Mean Squared Error (MSE): 179,675,782,813.27
•	R-squared (R²): 0.7411

# Analysis:
1.	Mean Squared Error (MSE):
o	The Mean Squared Error is quite large, indicating that the predicted values deviate significantly from the actual values. This value depends on the scale of the target variable, so if your target values are in a large range, a higher MSE might be expected.
o	It is essential to put this value into perspective by comparing it to the variance in the actual target values.
2.	R-squared (R²):
o	The R² value of 0.7411 implies that approximately 74.11% of the variance in the target variable can be explained by the model. This is a relatively good fit, showing that the model captures a significant portion of the data's underlying patterns.
o	However, there is still about 25.89% of the variance that is not explained by the model, suggesting room for improvement.

# Conclusion:
•	Strengths: Your Gradient Boosting Regressor model shows a decent performance with an R² of 0.7411, indicating it explains a significant portion of the variance in your data.
•	Weaknesses: The high MSE suggests that there might be issues with overfitting or the presence of outliers. It's crucial to check the distribution of your target variable and consider normalizing or transforming it if needed.
