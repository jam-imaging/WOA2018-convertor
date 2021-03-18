def plot_layer_by_number(df,column):
    
    from plotly import graph_objs as go
    from plotly.subplots import make_subplots
    import plotly
    import os
    

    trace1     = go.Scattergl(
        x      = df['LON'],
        y      = df['LAT'],
        name   = 'Grid Lat Lon',
        mode   = 'markers',
        line   = dict(color='#000000'), 
        marker = dict(size=4, color=df[curr_depth_layer],colorbar=dict(title='Temp',titleside='top'))
    )
        
    data = [trace1]
    fig  = go.Figure(data=data)

    fig['layout'].update(
        title         = 'Position Map',
        paper_bgcolor = '#414c50',
        plot_bgcolor  = '#414c50',
        font          =  dict(color='#f0f0f0'),
        yaxis         =  dict(scaleanchor="x", scaleratio=1),
        legend        =  dict(yanchor="top",y=0.99,xanchor="left",x=0.01,bgcolor='#000000')
    )

    fig.show() 

    return None

def plot_compare_data(df_s1,df_s2):    
    from plotly import graph_objs as go
    from plotly.subplots import make_subplots
    import plotly
    import os
    
    trace1     = go.Scattergl(
        x      = df_s1['LON'],
        y      = df_s1['0'],
        name   = 'CSV',
        mode   = 'markers',
        line   = dict(color='#000000'), 
        marker = dict(size=4)
    )
    
    trace2     = go.Scattergl(
        x      = df_s2['LON'],
        y      = df_s2['0'],
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
