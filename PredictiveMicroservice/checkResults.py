from darts import metrics

def checkMetrics(series, pred, number_days_to_predict):
    index_to_split = len(series) - number_days_to_predict
    mse = round(metrics.mse(series[index_to_split:], pred), 3)
    ope = round(metrics.ope(series[index_to_split:], pred), 3)
    coe = round(metrics.coefficient_of_variation(series[index_to_split:], pred), 3)
    return mse, ope, coe