import dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

application = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = application.server
application.config.suppress_callback_exceptions = True