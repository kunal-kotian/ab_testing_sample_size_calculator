import dash
import numpy as np
from sample_size_calculator import *
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go


app = dash.Dash()
app.config['suppress_callback_exceptions'] = True
app.scripts.config.serve_locally = True
app.css.config.serve_locally = True
dcc._css_dist[0]['relative_package_path'].append('styles.css')

app.layout = html.Div([
    html.Div(
        dcc.Tabs(
            tabs=[{'label': 'Comparison of Means', 'value': 1},
                  {'label': 'Comparison of Proportions', 'value': 2}
                  ],
            value=1,
            id='tabs',
            vertical=True,
            style={
                'height': '100vh',
                'borderRight': 'thin lightgrey solid',
                'textAlign': 'left'
            }
        ),
        style={'width': '20%', 'float': 'left'}
    ),
    html.Div(
        html.Div(id='tab-output'),
        style={'width': '80%', 'float': 'left'}
    )
], style={
    'fontFamily': 'Sans-Serif',
    'margin-left': 'auto',
    'margin-right': 'auto',
})


@app.callback(Output('tab-output', 'children'), [Input('tabs', 'value')])
def display_choice(tab):
    if tab == 1:
        return html.Div([dcc.Tabs(
            tabs=[
                {'label': 'Alpha Range', 'value': 1},
                {'label': 'Power Range', 'value': 2},
                {'label': 'Effect Size Range', 'value': 3}
            ],
            value=1,
            id='top_tab',
            vertical=False), html.Div([html.Div(id='mean_input_window',
                                      style={'width': '15%',
                                             'float': 'left',
                                             'padding-right': '5px',
                                             'padding-top': '10px',
                                             'padding-bottom': '10px',
                                             'padding-left': '10px',
                                             'border-style': 'solid',
                                             'border-width': '1px',
                                             'margin-top': '10px'}),
                                       dcc.Graph(id="graph_report",
                                                 style={'width': '80%', 'float': 'right',
                                                        'margin-top': '10px'})])],
            style={'width': '657.95px',
                   'fontFamily': 'Sans-Serif',
                   'margin-left': '0',
                   'margin-right': '0',
                   'padding-left': '6.90625px',
                   'padding-right': '6.90625px'
                   })
    else:
        return html.Div([dcc.Tabs(
            tabs=[
                {'label': 'Alpha Range', 'value': 4},
                {'label': 'Power Range', 'value': 5},
                {'label': 'Effect Size Range', 'value': 6}
            ],
            value=4,
            id='top_tab',
            vertical=False), html.Div([html.Div(id='proportion_input_window',
                                      style={'width': '15%',
                                             'float': 'left',
                                             'padding-right': '5px',
                                             'padding-top': '10px',
                                             'padding-bottom': '10px',
                                             'padding-left': '10px',
                                             'border-style': 'solid',
                                             'border-width': '1px',
                                             'margin-top': '10px'}),
                                       dcc.Graph(id="graph_report",
                                                 style={'width': '80%', 'float': 'right',
                                                        'margin-top': '10px'})])],
            style={'width': '657.95px',
                   'fontFamily': 'Sans-Serif',
                   'margin-left': '0',
                   'margin-right': '0',
                   'padding-left': '6.90625px',
                   'padding-right': '6.90625px'
                   })


@app.callback(Output('mean_input_window', 'children'),
              [Input('top_tab', 'value')])
def display_content(value):
    if value == 1:
        return html.Div(
            [html.Div([html.Div(html.Label('Min Alpha:')),
             dcc.Input(id='variable_param_min', value=0.05,
                       type='text', style={'width': 80}),
             html.Div(html.Label('Max Alpha:'),
                      style={'margin-top': 5}),
             dcc.Input(id='variable_param_max', value=0.10,
                       type='text', style={'width': 80}),
             html.Div(html.Label('Power:'),
                      style={'margin-top': 5}),
             dcc.Input(id='var3', value=0.8,
                       type='text', style={'width': 80}),
             html.Div(html.Label('Effect Size:'),
                      style={'margin-top': 5}),
             html.Div(dcc.Input(id='var4', value=0.5,
                      type='text', style={'width': 80})),
             html.Div(['k:',
                       html.Span(
                           '"k" is the no. of samples in condition 1 / no. of samples in condition 2',
                           className='tooltiptext')],
                      style={'margin-top': 5},
                      className='tooltip'),
             html.Div(dcc.Input(id='k', value=2,
                                type='text', style={'width': 80})),
             dcc.Input(id='prob', value=0.5, type='text',
                       style={'width': 80, 'display': 'none'}),
             html.Div(html.Label('Type:'),
                      style={'margin-top': 5}),
             dcc.RadioItems(id='tails',
                            options=[{'label': 'One-tailed',
                                      'value': True},
                                     {'label': 'Two-tailed',
                                      'value': False}],
                            value=True,
                            labelStyle={'display': 'inline-block',
                                        'font-size': '13px'}),
             html.Div(html.Button('Submit', id='button',
                                  style={'margin-top': 15,
                                         'text-align': 'center',
                                         'font-size': '17px'}),
                      style={'padding-left': '10px',
                             'padding-right': '5px'})]),
             html.Div(id='text_warning',
                      style={'margin-top': 15})])
    elif value == 2:
        return html.Div(
            [html.Div([html.Div(html.Label('Min Power:')),
             dcc.Input(id='variable_param_min', value=0.80,
                       type='text', style={'width': 80}),
             html.Div(html.Label('Max Power:'),
                      style={'margin-top': 5}),
             dcc.Input(id='variable_param_max',
                       value=0.90, type='text', style={'width': 80}),
             html.Div(html.Label('Alpha:'), style={'margin-top': 5}),
             dcc.Input(id='var3', value=0.05, type='text',
                       style={'width': 80}),
             html.Div(html.Label('Effect Size:'),
                      style={'margin-top': 5}),
             html.Div(dcc.Input(id='var4', value=0.5, type='text',
                                style={'width': 80})),
             html.Div(['k:',
                      html.Span(
                          '"k" is the no. of samples in condition 1 / no. of samples in condition 2',
                          className='tooltiptext')], style={'margin-top': 5},
                      className='tooltip'),
             html.Div(dcc.Input(id='k', value=2, type='text',
                                style={'width': 80})),
             dcc.Input(id='prob', value=0.5, type='text',
                       style={'width': 80, 'display': 'none'}),
             html.Div(html.Label('Type:'), style={'margin-top': 5}),
             dcc.RadioItems(id='tails',
                            options=[{'label': 'One-tailed', 'value': True},
                                     {'label': 'Two-tailed', 'value': False}],
                            value=True,
                            labelStyle={'display': 'inline-block',
                                        'font-size': '13px'}),
             html.Div(html.Button('Submit', id='button',
                                  style={'margin-top': 15,
                                         'text-align': 'center',
                                         'font-size': '17px'}),
                      style={'padding-left': '10px',
                             'padding-right': '5px'})]),
             html.Div(id='text_warning', style={'margin-top': 15})])
    elif value == 3:
        return html.Div(
            [html.Div([html.Div(html.Label('Min Effect Size:',
                      style={'font-size': '13px'})),
             dcc.Input(id='variable_param_min', value=0.05, type='text',
                       style={'width': 80}),
             html.Div(html.Label('Max Effect Size:',
                      style={'font-size': '13px'}),
                      style={'margin-top': 5}),
             dcc.Input(id='variable_param_max', value=0.10, type='text',
                       style={'width': 80}),
             html.Div(html.Label('Alpha:'), style={'margin-top': 5}),
             dcc.Input(id='var3', value=0.05, type='text',
                       style={'width': 80}),
             html.Div(html.Label('Power:'), style={'margin-top': 5}),
             html.Div(dcc.Input(id='var4', value=0.8, type='text',
                      style={'width': 80})),
             html.Div(['k:',
                       html.Span(
                           '"k" is the no. of samples in condition 1 / no. of samples in condition 2',
                           className='tooltiptext')], style={'margin-top': 5},
                      className='tooltip'),
             html.Div(dcc.Input(id='k', value=2, type='text',
                      style={'width': 80})),
             dcc.Input(id='prob', value=0.5, type='text',
                       style={'width': 80, 'display': 'none'}),
             html.Div(html.Label('Type:'), style={'margin-top': 5}),
             dcc.RadioItems(id='tails', options=[{'label': 'One-tailed',
                                                  'value': True},
                                                 {'label': 'Two-tailed',
                                                  'value': False}],
             value=True,
             labelStyle={'display': 'inline-block', 'font-size': '13px'}),
             html.Div(html.Button('Submit', id='button',
                                  style={'margin-top': 15,
                                         'text-align': 'center',
                                         'font-size': '17px'}),
                      style={'padding-left': '10px',
                             'padding-right': '5px'})]),
                html.Div(id='text_warning', style={'margin-top': 15})])


@app.callback(Output('proportion_input_window', 'children'), [Input('top_tab', 'value')])
def display_content(value):
    if value == 4:
        return html.Div(
            [html.Div([html.Div(html.Label('Min Alpha:')),
             dcc.Input(id='variable_param_min', value=0.05,
                       type='text', style={'width': 80}),
             html.Div(html.Label('Max Alpha:'), style={'margin-top': 5}),
             dcc.Input(id='variable_param_max', value=0.10, type='text',
                       style={'width': 80}),
             html.Div(html.Label('Power:'), style={'margin-top': 5}),
             dcc.Input(id='var3', value=0.8, type='text', style={'width': 80}),

             html.Div(html.Label('Effect Size:'), style={'margin-top': 5}),
             html.Div(dcc.Input(id='var4', value=0.5, type='text',
                                style={'width': 80})),
             html.Div(['k:',
                       html.Span(
                           '"k" is the no. of samples in condition 1 / no. of samples in condition 2',
                           className='tooltiptext')], style={'margin-top': 5},
             className='tooltip'),
             html.Div(dcc.Input(id='k', value=2, type='text',
                      style={'width': 80})),
             html.Div(['Probability:',
                       html.Span(
                           'The probability that a unit in condition 1 performs the action of interest',
                           className='tooltiptext', style={'right': '93px'})],
                      style={'margin-top': 5}, className='tooltip'),
             dcc.Input(id='prob', value=0.5, type='text', style={'width': 80}),
             html.Div(html.Label('Type:'), style={'margin-top': 5}),
             dcc.RadioItems(id='tails',
                            options=[{'label': 'One-tailed', 'value': True},
                                     {'label': 'Two-tailed', 'value': False}],
                            value=True, labelStyle={'display': 'inline-block',
                                                    'font-size': '13px'}),
             html.Div(html.Button('Submit', id='button',
                      style={'margin-top': 15, 'text-align': 'center',
                             'font-size': '17px'}),
                      style={'padding-left': '10px',
                             'padding-right': '5px'})]),
             html.Div(id='text_warning', style={'margin-top': 15})])
    elif value == 5:
        return html.Div(
            [html.Div([html.Div(html.Label('Min Power:')),
             dcc.Input(id='variable_param_min', value=0.80, type='text',
                       style={'width': 80}),
             html.Div(html.Label('Max Power:'), style={'margin-top': 5}),
             dcc.Input(id='variable_param_max', value=0.90, type='text',
                       style={'width': 80}),
             html.Div(html.Label('Alpha:'), style={'margin-top': 5}),
             dcc.Input(id='var3', value=0.05, type='text',
                       style={'width': 80}),
             html.Div(html.Label('Effect Size:'), style={'margin-top': 5}),
             html.Div(dcc.Input(id='var4', value=0.5, type='text',
                      style={'width': 80})),

             html.Div(['k:',
                       html.Span(
                           '"k" is the no. of samples in condition 1 / no. of samples in condition 2',
                           className='tooltiptext')], style={'margin-top': 5},
             className='tooltip'),
             html.Div(dcc.Input(id='k', value=2, type='text',
                                style={'width': 80})),
             html.Div(['Probability:',
                       html.Span(
                           'The probability that a unit in condition 1 performs the action of interest',
                           className='tooltiptext', style={'right': '93px'})],
             style={'margin-top': 5},
             className='tooltip'),
             dcc.Input(id='prob', value=0.5, type='text', style={'width': 80}),
             html.Div(html.Label('Type:'), style={'margin-top': 5}),
             dcc.RadioItems(id='tails',
                            options=[{'label': 'One-tailed', 'value': True},
                                     {'label': 'Two-tailed', 'value': False}],
                            value=True,
                            labelStyle={'display': 'inline-block',
                                        'font-size': '13px'}),
             html.Div(html.Button('Submit', id='button',
                                  style={'margin-top': 15,
                                         'text-align': 'center',
                                         'font-size': '17px'}),
                      style={'padding-left': '10px',
                             'padding-right': '5px'})]),
             html.Div(id='text_warning', style={'margin-top': 15})])
    elif value == 6:
        return html.Div(
            [html.Div([html.Div(html.Label('Min Effect Size:',
             style={'font-size': '13px'})),
                dcc.Input(id='variable_param_min', value=0.05,
                          type='text', style={'width': 80}),
                html.Div(html.Label('Max Effect Size:',
                         style={'font-size': '13px'}),
                         style={'margin-top': 5}),
                dcc.Input(id='variable_param_max', value=0.10, type='text',
                          style={'width': 80}),
                html.Div(html.Label('Alpha:'), style={'margin-top': 5}),
                dcc.Input(id='var3', value=0.05, type='text',
                          style={'width': 80}),
                html.Div(html.Label('Power:'), style={'margin-top': 5}),
                html.Div(dcc.Input(id='var4', value=0.8, type='text',
                                   style={'width': 80})),
                html.Div(['k:',
                          html.Span(
                              '"k" is the no. of samples in condition 1 / no. of samples in condition 2',
                              className='tooltiptext')],
                         style={'margin-top': 5},
                         className='tooltip'),
                html.Div(dcc.Input(id='k', value=2, type='text',
                                   style={'width': 80})),

                html.Div(['Probability:',
                          html.Span(
                              'The probability that a unit in condition 1 performs the action of interest',
                              className='tooltiptext',
                              style={'right': '93px'})],
                         style={'margin-top': 5},
                         className='tooltip'),
                dcc.Input(id='prob', value=0.5, type='text',
                          style={'width': 80}),

                html.Div(html.Label('Type:'), style={'margin-top': 5}),
                dcc.RadioItems(id='tails',
                               options=[{'label': 'One-tailed',
                                         'value': True},
                                        {'label': 'Two-tailed',
                                         'value': False}],
                               value=True,
                               labelStyle={'display': 'inline-block',
                                           'font-size': '13px'}),
                html.Div(html.Button('Submit', id='button',
                                     style={'margin-top': 15,
                                            'text-align': 'center',
                                            'font-size': '17px'}),
                         style={'padding-left': '10px',
                                'padding-right': '5px'})]),
             html.Div(id='text_warning', style={'margin-top': 15})])


def render_plot_data(param_vals):
    x_var = str([var for var in ['alpha', 'power', 'delta'] if
                len(param_vals[var]) > 1][0])
    param_vals = format_inputs_dict(x_var, param_vals)

    min_sample_sizes = []
    num_vars = len(param_vals[x_var])
    for i in range(num_vars):
        inputs = {var: param_vals[var][i] for var in param_vals}
        n_1, n_2 = get_sample_size(**inputs)
        min_sample_sizes.append((n_1, n_2))

    n_1_all = [e[0] for e in min_sample_sizes]
    n_2_all = [e[1] for e in min_sample_sizes]

    trace1 = go.Scatter(x=param_vals[x_var],
                        y=n_1_all, name='Condition 1')
    trace2 = go.Scatter(x=param_vals[x_var],
                        y=n_2_all, name='Condition 2')
    data = [trace1, trace2]
    layout = go.Layout(title='Test of {}'.format(param_vals['test_of'][0]),
                       xaxis={'title': x_var},
                       yaxis={'title': 'Minimum number of samples'},
                       margin={'l': 80, 'b': 60, 't': 50, 'r': 40},
                       hovermode='closest',
                       showlegend=False)
    fig = go.Figure(data=data, layout=layout)
    return fig


def generate_param_vals(tab, variable_param_min, variable_param_max,
                        var3, var4, k, tails, prob):
    variable_param_vals = np.linspace(start=float(variable_param_min),
                                      stop=float(variable_param_max), num=100)
    if tab == 1:
        param_vals = {'alpha': variable_param_vals.tolist(),
                      'power': [float(var3)],
                      'delta': [float(var4)],
                      'k': [float(k)],
                      'is_one_sided': [tails],
                      'prop_1': [None],
                      'test_of': ['means']}
    elif tab == 2:
        param_vals = {'power': variable_param_vals.tolist(),
                      'alpha': [float(var3)],
                      'delta': [float(var4)],
                      'k': [float(k)],
                      'is_one_sided': [tails],
                      'prop_1': [None],
                      'test_of': ['means']}
    elif tab == 3:
        param_vals = {'delta': variable_param_vals.tolist(),
                      'alpha': [float(var3)],
                      'power': [float(var4)],
                      'k': [float(k)],
                      'is_one_sided': [tails],
                      'prop_1': [None],
                      'test_of': ['means']}
    elif tab == 4:
        param_vals = {'alpha': variable_param_vals.tolist(),
                      'power': [float(var3)],
                      'delta': [float(var4)],
                      'k': [float(k)],
                      'is_one_sided': [tails],
                      'prop_1': [float(prob)],
                      'test_of': ['proportions']}
    elif tab == 5:
        param_vals = {'power': variable_param_vals.tolist(),
                      'alpha': [float(var3)],
                      'delta': [float(var4)],
                      'k': [float(k)],
                      'is_one_sided': [tails],
                      'prop_1': [float(prob)],
                      'test_of': ['proportions']}
    elif tab == 6:
        param_vals = {'delta': variable_param_vals.tolist(),
                      'alpha': [float(var3)],
                      'power': [float(var4)],
                      'k': [float(k)],
                      'is_one_sided': [tails],
                      'prop_1': [float(prob)],
                      'test_of': ['proportions']}
    return param_vals


@app.callback(Output('graph_report', 'figure'), [Input('button', 'n_clicks')],
              [State('top_tab', 'value'), State('variable_param_min', 'value'),
               State('variable_param_max', 'value'), State('var3', 'value'),
               State('var4', 'value'), State('k', 'value'),
               State('tails', 'value'), State('prob', 'value')])
def display_plot(n_clicks, tab, variable_param_min, variable_param_max,
                 var3, var4, k, tails, prob):
    param_vals = generate_param_vals(tab, variable_param_min, variable_param_max,
                                     var3, var4, k, tails, prob)
    try:
        fig = render_plot_data(param_vals)
    except:
        fig = {'data': []}
    return fig

@app.callback(Output('text_warning', 'children'), [Input('button', 'n_clicks')],
              [State('top_tab', 'value'), State('variable_param_min', 'value'),
               State('variable_param_max', 'value'), State('var3', 'value'),
               State('var4', 'value'), State('k', 'value'),
               State('tails', 'value'), State('prob', 'value')])
def display_plot(n_clicks, tab, variable_param_min, variable_param_max,
                 var3, var4, k, tails, prob):
    param_vals = generate_param_vals(tab, variable_param_min, variable_param_max,
                                     var3, var4, k, tails, prob)
    error_mesg = ''
    try:
        render_plot_data(param_vals)
    except:
        error_mesg = 'Invalid input parameter(s)!'
    return error_mesg


if __name__ == '__main__':
    app.run_server(debug=True)
