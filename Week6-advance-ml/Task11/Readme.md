# Week 6 — Advanced Machine Learning Techniques

This project covers advanced machine learning techniques, including model building, tuning, and comparison for housing price prediction. It is part of the AI/ML Fellowship at GDGOC COMSATS Attock.

## Task 11 — Advanced ML & Model Comparison

### Objectives

- Build multiple regression and classification models
- Apply regularization techniques
- Implement tree-based and ensemble models
- Perform hyperparameter tuning
- Compare models using evaluation metrics

### Concepts Covered

- Advanced Machine Learning Techniques
- Regularization (L1 - Lasso, L2 - Ridge)
- Decision Trees & Random Forests
- Support Vector Machines (SVM & SVR)
- Ensemble Learning Methods
- Gradient Boosting
- Model Stacking
- Hyperparameter Tuning
- Model Evaluation (RMSE, R², Accuracy, etc.)

### Models Implemented

1. Linear Models
- Linear Regression (Baseline)
- Ridge Regression (L2 Regularization)
- Lasso Regression (L1 Regularization)

2. Tree-Based Models
- Decision Tree Regressor
- Random Forest Regressor

3. Kernel-Based Models
- Support Vector Regression (SVR)
- Support Vector Machine (SVM - Classification)

4. Ensemble Learning
- Gradient Boosting Regressor
- Stacking Regressor (Meta-model)

5. Hyperparameter Tuning
- GridSearchCV
- RandomizedSearchCV
Used for optimizing:
- Random Forest
- Model performance improvement

###  Dataset
- California Housing Dataset (from Scikit-learn)
- Features include income, house age, rooms, population, etc.
- Target: Median house value

### Model Evaluation Metrics
- Regression Metrics:
- RMSE (Root Mean Squared Error) → Lower is better
- R² Score → Higher is better
- Classification Metrics:
  1. Accuracy
  2. Precision
  3. Recall
  4. F1 Score

### Results Summary

 | Model | Performance |
 |-------|-------------|
 | Linear Models |	Baseline performance |
 | Decision Tree |	Improved non-linear learning |
 | Random Forest | Strong performance |
 | SVR | Good but sensitive to scaling |
 | Gradient Boosting | High accuracy |
 | Stacking | Best overall performance |
 | Tuned Random Forest | Further improved results |

### Visualization

- Bar plots for RMSE comparison
- Bar plots for R² comparison
- Clear ranking of models
##  Project Structure
Week6-Advanced-ML/
│
└── house_price_pred.ipynb   # Complete implementation

### Key Learnings
- Ensemble models outperform single models
- Regularization prevents overfitting
- Feature scaling is crucial for SVM
- Hyperparameter tuning significantly improves performance
- Stacking combines strengths of multiple models

### Final Conclusion

- Best Model: Stacking Regressor
- Runner-up: Gradient Boosting
- Most Improved: Tuned Random Forest

These models provide the best balance of low error (RMSE) and high accuracy (R² score) for housing price prediction.
