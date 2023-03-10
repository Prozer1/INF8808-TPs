'''
    Provides the templates for the tooltips.
'''


def get_heatmap_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains three labels, followed by their corresponding
        value, separated by a colon : neighborhood, year and
        trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''

    return "<br>".join([
        "<span style='font-family: Roboto Slab; font-weight: bold'>Neighborhood</span> : %{y}",
        "<span style='font-family: Roboto Slab; font-weight: bold'>Year</span> : %{x}",
        "<span style='font-family: Roboto; font-weight: bold'>Trees</span> : %{z}",
        "<extra></extra>"
    ])


def get_linechart_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains two labels, followed by their corresponding
        value, separated by a colon : date and trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''

    return "<br>".join([
        "<span style='font-family: Roboto Slab; font-weight: bold'>Date</span> : %{x}",
        "<span style='font-family: Roboto; font-weight: bold'>Trees</span> : %{y}"
    ])

