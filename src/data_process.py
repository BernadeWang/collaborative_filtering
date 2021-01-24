import numpy as np
import pandas as pd


def sim_euclidean_distance(pref:dict, person1, person2):
    person1_series = pd.Series(pref[person1])
    person2_series = pd.Series(pref[person2])

    euclidean_distance = np.sqrt((person1_series - person2_series).pow(2).sum())
    return 1 / (1 + euclidean_distance)


def sim_pearson(pref:dict, person1, person2):
    person1_series = pd.Series(pref[person1])
    person2_series = pd.Series(pref[person2])

    concat_df = pd.concat([person1_series, person2_series], axis=1)
    index_series = concat_df.notna().all('columns')
    concat_df = concat_df.loc[index_series]
    index_len = len(concat_df)

    sum_series = concat_df.sum()
    square_sum_series = concat_df.pow(2).sum()
    inner_prod = concat_df.prod(axis=1).sum()

    numerator = inner_prod - sum_series.prod() / index_len
    denominator = np.sqrt((square_sum_series - sum_series.pow(2) / index_len).prod())
    if denominator == 0:
        return 0
    return numerator / denominator


def match_for_certain_people(pref: dict, person, sim_metric=sim_pearson):
    ranked_match = [sim_metric(pref, person, other) for other in ]
    pass
