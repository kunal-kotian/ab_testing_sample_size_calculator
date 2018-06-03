import math
import scipy.stats as st
import numpy as np

import matplotlib.pyplot as plt

def get_input():
    """Returns a dict that stores parameter values based on input taken from the user."""
    prompt_param = """
    Select a parameter for which you'll provide a range of values.
    Sample sizes will be computed across a range of the selected parameter's values.
    Pick one of:
    1 = significance level (alpha), 2 = power (1 - beta), 3 = effect size (delta)
    """
    print('Enter the type of test. Pick one of:')
    test_of = int(input('1 = Comparison of means, 2 = Comparison of proportions\n'))

    params = ['alpha', 'power', 'delta']
    # param_vals format - key = parameter name, value = parameter value(s) in a list
    # e.g. {'alpha': [0.05], 'power': [0.5, 0.6, 0.7], 'delta': [5.7]}
    param_vals = {}
    # identify the variable for which we need a range of values based on user input
    variable_param = int(input(prompt_param)) - 1

    for param_ind in range(len(params)):
        if param_ind != variable_param:
            param_name = params[param_ind]
            prompt = 'Enter a single value for {}:  '.format(param_name)
            param_vals[param_name] = [float(input(prompt))]

    variable_param_name = params[variable_param]
    print('Specify a range of values for {} below...'.format(variable_param_name))
    variable_param_min = float(input('Enter the minimum value of interest for {} : '.format(variable_param_name)))
    variable_param_max = float(input('Enter the maximum value of interest for {}: '.format(variable_param_name)))
    variable_param_vals = np.linspace(start=variable_param_min, stop=variable_param_max, num=1000)
    param_vals[variable_param_name] = list(variable_param_vals)

    # Ask for other required inputs
    print('"k" is the no. of samples in condition 1 / no. of samples in condition 2, n1 = k*n2')
    param_vals['k'] = [float(input('Enter a value for k: '))]
    one_sided = input('Are you interested in a one-sided test? Enter Y/N:  ')
    if one_sided.lower() == 'y':
        param_vals['is_one_sided'] = [True]
    elif one_sided.lower() == 'n':
        param_vals['is_one_sided'] = [False]
    else:
        raise ValueError('You can enter only "Y" or "N".  Please start over.')

    # we need one more input for the test of proportions
    if test_of == 2:
        print('Enter the probability that a unit in condition 1 performs the action of interest:')
        prop_1 = float(input())
        param_vals['prop_1'] = [prop_1]
    else:
        param_vals['prop_1'] = [None]

    # finally, add test_of to param_vals also for reference later
    param_vals['test_of'] = ['means' if test_of == 1 else 'proportions']

    return param_vals


def get_sample_size(test_of, alpha, power, delta, k, is_one_sided, prop_1):
    """For a two-sample test of proportions, returns a tuple (n1, n2) 
    of the minimum sample sizes required under conditions 1 and 2.
    test_of: one of 'means' or 'proportions'
    alpha: significance level
    power: minimum required power of the test
    delta: minimum difference to be detected between the null and alternate parameter values
    k: no. of samples in condition 1 / no. of samples in condition 2, n1 = k*n2
        k = 1 when both conditions need to have equal no. of samples
    is_one_sided: boolean indicator of whether a test is one-sided or two-sided
    prop_1: proportion under null hypothesis, or for A/B testing:
        probability that a unit in condition 1 performs the action of interest
    """
    if test_of == 'proportions':
        prop_2 = prop_1 - delta
        # z_rejection is the quantile for the rejection region
        # z_rejection = z_alpha for a one-sided test, otherwise z_alpha/2
        z_rejection = st.norm.ppf(alpha) if is_one_sided else st.norm.ppf(alpha / 2)
        z_power = st.norm.ppf(power)   # same as z for (1 - beta)
        n_2 = (((z_rejection - z_power)**2) * ((((prop_1 * (1 - prop_1)) / k) + (prop_2 * (1 - prop_2)))**2)) / delta**2
        n_1 = k * n_2
        min_sample_size = (math.ceil(n_1), math.ceil(n_2))

    elif test_of == 'means':
        # TO DO - calculate no. of samples in the case of test of means
        pass

    return min_sample_size


def format_inputs_dict(x_var, param_vals):
    """Return updated param_vals dict such that every parameter has a list of values with the same length n; 
    x_var will have a range of different values, while the other params have the same values repeated.
    x_var: The x-axis variable - the parameter that will have a range of values
    param_vals: dict containing all required inputs (format specified elsewhere in this script)
    """
    for param in param_vals:
        if param != x_var:
            param_vals[param] = param_vals[param] * len(param_vals[x_var])
    return param_vals

#  ------------------------------------------------------------------------

# Main code:

param_vals = get_input()

# identify the parameter that goes on the x-axis of the sample size plot
x_var = str([var for var in ['alpha', 'power', 'delta'] if len(param_vals[var]) > 1][0])

param_vals = format_inputs_dict(x_var, param_vals)   # reformat param_vals
min_sample_sizes = []

for i in range(len(param_vals[x_var])):
    inputs = {var:param_vals[var][i] for var in param_vals}
    n_1, n_2 = get_sample_size(**inputs)
    min_sample_sizes.append((n_1, n_2))

n_1_all = [e[0] for e in min_sample_sizes]
n_2_all = [e[1] for e in min_sample_sizes]

# create the plot
plt.plot(param_vals[x_var], n_1_all, label='Condition 1')
plt.plot(param_vals[x_var], n_2_all, label='Condition 2')
plt.xlabel(x_var)
plt.ylabel('Minimum number of samples')
plt.legend(loc='upper left')
plt.show()


