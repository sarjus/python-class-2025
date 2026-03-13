
import pandas as pd
import numpy as np
import shap
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

# -------------------------------
# 1. Load Excel Data
# -------------------------------

file_path = r"C:\Users\mesar\PycharmProjects\s6cse\Data for Input Output analysis.xlsx"

data = pd.read_excel(file_path, header=0)
print(data.head(15))

# -------------------------------
# 2. Define Inputs and Output
# -------------------------------
# MODIFY column names to match your Excel file exactly

input_features = [
    'Deck slab thickness',
    'Span/Depth ratio',
    'Boundary condition',
    'Applied Load'
]

output_feature = 'Central deflection'   # Change to 'End slip' if needed

X = data[input_features]
y = data[output_feature]

# -------------------------------
# 3. Train-Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# 4. Train ML Model (Surrogate)
# -------------------------------
# Tree-based models are ideal for SHAP

model = RandomForestRegressor(
    n_estimators=300,
    max_depth=None,
    random_state=42
)

model.fit(X_train, y_train)

# -------------------------------
# 5. Model Performance Check
# -------------------------------
y_pred = model.predict(X_test)

print("R² Score :", r2_score(y_test, y_pred))
print("RMSE     :", np.sqrt(mean_squared_error(y_test, y_pred)))

# -------------------------------
# 6. SHAP Explainer
# -------------------------------
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_train)

# -------------------------------
# 7. SHAP Summary Plot
# -------------------------------
plt.figure()
shap.summary_plot(
    shap_values,
    X_train,
    plot_type="dot",
    show=False
)
plt.tight_layout()
plt.show()

# -------------------------------
# 8. SHAP Bar Plot (Mean Impact)
# -------------------------------
plt.figure()
shap.summary_plot(
    shap_values,
    X_train,
    plot_type="bar",
    show=False
)
plt.tight_layout()
plt.show()

# -------------------------------
# 9. SHAP Dependence Plots
# -------------------------------
for feature in input_features:
    plt.figure()
    shap.dependence_plot(
        feature,
        shap_values,
        X_train,
        show=False
    )
    plt.tight_layout()
    plt.show()

# -------------------------------
# 10. SHAP Percentage Contribution
# -------------------------------
mean_shap = np.abs(shap_values).mean(axis=0)
shap_percent = 100 * mean_shap / mean_shap.sum()

shap_table = pd.DataFrame({
    'Feature': input_features,
    'Mean |SHAP|': mean_shap,
    'Percentage Contribution (%)': shap_percent
}).sort_values(by='Percentage Contribution (%)', ascending=False)

print("\nSHAP Percentage Contribution:")
print(shap_table)

# Optional: Save SHAP table
shap_table.to_excel("SHAP_Percentage_Contribution.xlsx", index=False)
