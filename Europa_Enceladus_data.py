import pandas as pd

# raw data for Europa images starts here

## Rhadamanthys Linea (link):

rhad_linea_raw = {'n_or_v_value':[2,3,4,5,6,7,8],
                  'n':[141,6,394,'','','',''],
                  'v':['',196,196,76,12,3,1]}

rhad_linea = pd.DataFrame(rhad_linea_raw)

## Phaidra Linea (link):

phad_linea_raw = {'n_or_v_value':[2,3,4,5,6,7,8],
                  'n':[65,2,158,2,6,'',''],
                  'v':['',85,62,27,9,1,'']}

phad_linea = pd.DataFrame(phad_linea_raw)

### Enceladus images start here ###

# Enceladus (link):

enceladus_raw = {'n_or_v_value':[2,3,4,5,6,7,8],
                  'n':[21,2,52,4,1,'',''],
                  'v':['',14,35,6,1,'','']}

enceladus = pd.DataFrame(enceladus_raw)


def n_v(df):

    def average_n (df):
        n_list = []
        n_list_sum = 0
        n_actual_sum = 0
        value_list_n = []
        value_list_n = df[df['n'] != '']['n_or_v_value'].tolist()
        for value in df['n']:
             if value != '' : n_list.append(value)
        for value in n_list:
            n_list_sum += value
        multiplied_list = [a * b for a, b in zip(n_list, value_list_n)]
        for value in multiplied_list:
             n_actual_sum += value
        n_bar_star = n_actual_sum / n_list_sum
        return n_bar_star

    def average_v (df):
        v_list = []
        v_list_sum = 0
        v_actual_sum = 0
        value_list_v = []
        value_list_v = df[df['v'] != '']['n_or_v_value'].tolist()
        for value in df['v']:
            if value != '' : v_list.append(value)
        for value in v_list:
            v_list_sum += value
        multiplied_list = [a * b for a, b in zip(v_list, value_list_v)]
        for value in multiplied_list:
            v_actual_sum += value
        v_bar_star = v_actual_sum / v_list_sum
        return v_bar_star
    n_bar_star = average_n(df)
    v_bar_star = average_v(df)
    return print('\u0305n\u2217,\u0305v\u2217 =',f'{n_bar_star:2f}',',',f'{v_bar_star:2f}')

n_v(enceladus)