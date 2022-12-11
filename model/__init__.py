from app import app

linreg_intercept_ = -11633.494594179414
linreg_coef_ = [259.45318189,323.0510586,23833.87003847,-109.04110867]

def calc_insurance(age, bmi, smoking,sex):
    y = ((age*linreg_coef_[0]) + (bmi*linreg_coef_[1]) + (smoking*linreg_coef_[2]) + (sex*linreg_coef_[3]) - linreg_intercept_)
    data = {"prem":'{:,d}'.format(int(y))}
    return data