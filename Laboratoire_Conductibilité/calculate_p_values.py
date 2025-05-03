import scipy.stats as stats

def calculate_p_value(x, y):
    """
    Calculate the p-value for two datasets x and y using a two-tailed t-test.

    Parameters:
        x (list or array-like): First dataset.
        y (list or array-like): Second dataset.

    Returns:
        float: The p-value of the t-test.
    """
    slope, intercept, r, p, std_err = stats.linregress(x, y)
    return p


current_rayan = [0.00, 0.05, 0.10, 0.15, 0.20, 0.25]
voltage_rayan = [0.00, 1.06, 2.16, 3.12, 4.05, 5.19]
current_radu = [0.00, 0.10, 0.20, 0.30, 0.40]
voltage_radu = [0.00, 1.12, 2.11, 3.08, 4.05]

p_value_rayan = calculate_p_value(voltage_rayan, current_rayan)
p_value_radu = calculate_p_value(voltage_radu, current_radu)
print(f"P-value Rayan: {p_value_rayan}")
print(f"P-value Radu: {p_value_radu}")