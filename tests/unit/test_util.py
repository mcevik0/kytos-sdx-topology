"""
SDX Topology util Unit test
"""
import numpy as np
import pandas as pd
from napps.kytos.sdx_topology import utils  # pylint: disable=E0401

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def test_get_timestamp():
    '''test get_timestamp'''
    timestamp = '2022-02-18 14:41:10'
    assert utils.get_timestamp(timestamp) == '2022-02-18T14:41:10Z'


def test_diff_pd(df_data):
    """Identify differences between two pandas DataFrames"""
    current_dict = [v for (k, v) in df_data[0].items()]
    current_df = pd.json_normalize(current_dict)
    initial_dict = [v for (k, v) in df_data[1].items()]
    initial_df = pd.json_normalize(initial_dict)

    assert (current_df.columns == initial_df.columns).all(), \
        "DataFrame column names are different"
    if any(current_df.dtypes != initial_df.dtypes):
        # Data Types are different, trying to convert
        initial_df = initial_df.astype(current_df.dtypes)
    if current_df.equals(initial_df):
        assert True
    else:
        diff_mask = (current_df != initial_df) & \
                ~(current_df.isnull() & initial_df.isnull())
        ne_stacked = diff_mask.stack()
        changed = ne_stacked[ne_stacked]
        changed.index.names = ['id', 'col']
        difference_locations = np.where(diff_mask)
        changed_from = current_df.values[difference_locations]
        changed_to = initial_df.values[difference_locations]
        assert changed_from[0] != changed_to[0]


def test_load_spec():
    '''test load_spec'''
    content = utils.load_spec().content()
    assert content['servers'][0]['url'] == '/api/kytos/sdx_topology'
