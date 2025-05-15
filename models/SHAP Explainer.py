import shap
import joblib

explainer = shap.TreeExplainer(model)
joblib.dump(explainer, '../models/shap_explainer.pkl')

# Example usage
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test)