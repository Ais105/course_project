from typing import List
import plotly.graph_objects as go


def paint(headers: List[str], cells: list, width: int, height: int):
    """

    :param headers:
    :param cells:
    :param width:
    :param height:
    :return:
    """

    fig = go.Figure(data=[go.Table(
        header=dict(values=headers,
                    line_color='white',
                    fill_color='rgb(206, 153, 255)',
                    align='center'),
        cells=dict(values=cells,
                   line_color='white',
                   fill_color='rgb(230, 204, 255)',
                   align='center'))
    ])
    fig.update_layout(width=width, height=height)
    fig.show()
