import joblib

def ensemble_model(fp_x_test):
    alpha = 0.15
    beta = 0.05
    gamma = 0.3
    delta = 0.5

    xgb_model = joblib.load("./models/xgb_model.pkl")
    logistic_model = joblib.load("./models/logistic_model.pkl")
    knn_model = joblib.load("./models/knn_model.pkl")
    random_forest_model = joblib.load("./models/random_forest_model.pkl")

    y_pred_xgb = xgb_model.predict_proba(fp_x_test)
    y_pred_logistic = logistic_model.predict_proba(fp_x_test)
    y_pred_knn = knn_model.predict_proba(fp_x_test)
    y_pred_random_forest = random_forest_model.predict_proba(fp_x_test)

    y_pred_ensemble = []
    for i in range(len(y_pred_xgb)):
        xgb_score = y_pred_xgb[i][1] * alpha
        logistic_score = y_pred_logistic[i][1] * beta
        knn_score = y_pred_knn[i][1] * gamma
        random_forest_score = y_pred_random_forest[i][1] * delta
        total_score = xgb_score + logistic_score + knn_score + random_forest_score

        if total_score >= 0.4:
            y_pred_ensemble.append(1)
        else:
            y_pred_ensemble.append(0)

    return y_pred_ensemble

