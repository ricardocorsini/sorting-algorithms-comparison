import plotly.graph_objects as go
import pandas as pd

def bar_chart(df, name, n):

    x_axis = ['Bubble Sort', 'Heap Sort', 'Insertion Sort', 'Quick Sort', 'Merge Sort', 'Radix Sort', 'Selection Sort']

    fig = go.Figure()

    fig.add_trace(go.Bar(x=x_axis,
                         y= df.iloc[0].tolist(),
                         name='Random',
                         marker_color='#59C9A5'
                        ))
    
    fig.add_trace(go.Bar(x=x_axis,
                         y= df.iloc[1].tolist(),
                         name='Partially (50%)',
                         marker_color='#D81E5B'
                        ))
    
    fig.add_trace(go.Bar(x=x_axis,
                         y= df.iloc[2].tolist(),
                         name='Descending',
                         marker_color='#23395B'
                        ))
    
    fig.update_layout(
        title=f'Experimento com Array de tamanho {n}',
        title_font_size=30,
        xaxis_tickfont_size=24,
        yaxis=dict(
            title='Tempo de processamento (ms)',
            titlefont_size=28,
            tickfont_size=24,
        ),
        legend=dict(
            x=0,
            y=1.0,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)',
            font=dict(
                size=18
            )
        ),
        barmode='group',
        bargap=0.15, 
        bargroupgap=0.1 
    )

    fileName = './charts/' + name + '.html'

    fig.write_html(fileName)


