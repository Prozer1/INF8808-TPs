'''
    Contains the functions to set up the map visualization.

'''

import plotly.graph_objects as go
import plotly.express as px

import hover_template as hover


def add_choro_trace(fig, montreal_data, locations, z_vals, colorscale):
    '''
        Adds the choropleth trace, representing Montreal's neighborhoods.

        Note: The z values and colorscale provided ensure every neighborhood
        will be grey in color. Although the trace is defined using Plotly's
        choropleth features, we are simply defining our base map.

        The opacity of the map background color should be 0.2.

        Args:
            fig: The figure to add the choropleth trace to
            montreal_data: The data used for the trace
            locations: The locations (neighborhoods) to show on the trace
            z_vals: The table to use for the choropleth's z values
            colorscale: The table to use for the choropleth's color scale
        Returns:
            fig: The updated figure with the choropleth trace

    '''
    # TODO : Draw the map base
    # fig = go.Figure(data=go.Choroplethmapbox(geojson=montreal_data, locations=locations, z=z_vals, colorscale=colorscale, marker_opacity=0.2))
    # fig.update_layout(mapbox_style="carto-positron", mapbox_zoom=9.5, mapbox_center = {"lat": 45.50884, "lon": -73.58781})

    # fig.add_trace(
    # go.Choroplethmapbox(
    #     locations=locations,
    #     z=z_vals,
    #     geojson=montreal_data,
    #     colorscale=colorscale,
    #     marker_opacity=0.2,
    #     #hovertemplate=hover.get_hover_template()
    # )
    # )

    fig = px.choropleth_mapbox(geojson=montreal_data, locations=locations, color=z_vals, opacity=0.2)
    fig.update_layout(mapbox_style="carto-positron", mapbox_zoom=9.5, mapbox_center = {"lat": 45.50884, "lon": -73.58781})

    
    return fig


def add_scatter_traces(fig, street_df):
    '''
        Adds the scatter trace, representing Montreal's pedestrian paths.

        The marker size should be 20.

        Args:
            fig: The figure to add the scatter trace to
            street_df: The dataframe containing the information on the
                pedestrian paths to display
        Returns:
            The figure now containing the scatter trace

    '''
    # TODO : Add the scatter markers to the map base
    # fig.add_trace(go.Scattermapbox(lat=street_df['properties.LATITUDE'], lon=street_df['properties.LONGITUDE'], mode='markers', marker=go.scattermapbox.Marker(size=20)))
    
    return fig
