def plot_layer_by_number(df2, curr_depth_layer, path_html):
    
    from plotly import graph_objs as go
    from plotly.subplots import make_subplots

    trace1     = go.Scattergl(
        x      = df2['LON'],
        y      = df2['LAT'],
        name   = 'Grid Lat Lon',
        mode   = 'markers',
        line   = dict(color='#000000'), 
        marker = dict(size=4, color=df2[curr_depth_layer],colorbar=dict(title='Temp',titleside='top'))
    )
        
    data = [trace1]
    fig  = go.Figure(data=data)

    fig['layout'].update(
        title         = 'Temperature',
        paper_bgcolor = '#414c50',
        plot_bgcolor  = '#414c50',
        font          =  dict(color='#f0f0f0'),
        yaxis         =  dict(scaleanchor="x", scaleratio=1),
        legend        =  dict(yanchor="top",y=0.99,xanchor="left",x=0.01,bgcolor='#000000')
    )

    fig.show()
    fig.write_html(path_html) 

    return None

def plot_compare_data(df_csv,df_asc):    
    from plotly import graph_objs as go
    from plotly.subplots import make_subplots
    
    trace1     = go.Scattergl(
        x      = df_csv['LON'],
        y      = df_csv['0'],
        name   = 'CSV',
        mode   = 'markers',
        line   = dict(color='#000000'), 
        marker = dict(size=4)
    )
    
    trace2     = go.Scattergl(
        x      = df_asc['LON'],
        y      = df_asc['0'],
        name   = 'Ascii',
        mode   = 'markers',
        line   = dict(color='#ff0000'), 
        marker = dict(size=4)
    )
    
    data = [trace1,trace2]
    fig  = go.Figure(data=data)

    fig['layout'].update(
        title         = 'Data Graph',
        paper_bgcolor = '#414c50',
        plot_bgcolor  = '#414c50',
        font          =  dict(color='#f0f0f0'),
        yaxis         =  dict(scaleanchor="x", scaleratio=1),
        legend        =  dict(yanchor="top",y=0.99,xanchor="left",x=0.01,bgcolor='#000000')
    )

    fig.show() 
    return None
