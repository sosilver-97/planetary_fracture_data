import pandas as pd

# raw data for Mars surfaces starts here

# mars hexagons (link):

mars_hexagons_raw = {'n_or_v_value' : [2,3,4,5,6,7,8,9,10,11,''],
                 'n' : [1043,8017,661,10,'','','','','','',''],
                 'v' : ['',67,611,1947,1779,505,116,30,8,5,''],
                 }

mars_hexagons = pd.DataFrame(mars_hexagons_raw)

# gordii dorsum (link):

gordii_dorsum_raw = {'n_or_v_value' : [2,3,4,5,6,7,8,''],
                 'n' : [249,140,23,'','','','',''],
                 'v' : [1,27,73,65,22,5,1,''],
                 }

gordii_dorsum = pd.DataFrame(gordii_dorsum_raw)


#gale crater (link):

gale_crater_raw = {'n_or_v_value' : [2,3,4,5,6,7,8,''],
                 'n' : [95,14,25,4,'','','',''],
                 'v' : ['',15,55,6,1,'','',''],
                 }

gale_crater = pd.DataFrame(gordii_dorsum_raw)


#angustus labyrinthus (link) :

angustus_labyrinthus_raw = {'n_or_v_value' : [2,3,4,5,6,7,8,''],
                 'n' : [51,22,2,1,'','','',''],
                 'v' : ['',9,15,5,4,'','',''],
                 }

angustus_labyrinthus = pd.DataFrame(angustus_labyrinthus_raw)


#mars lacustrine sediments (link):

mars_lacustrine_sediments_raw = {'n_or_v_value' : [2,3,4,5,6,7,8,''],
                 'n' : [57,62,13,1,'','','',''],
                 'v' : ['',12,29,19,8,1,'',''],
                 }

mars_lacustrine_sediments = pd.DataFrame(mars_lacustrine_sediments_raw)

#exhumed ridges (link):

exhumed_ridges_raw = {'n_or_v_value' : [2,3,4,5,6,7,8,''],
                 'n' : [162,82,24,'','','','',''],
                 'v' : [1,12,54,36,11,2,2,''],
                 }

exhumed_ridges = pd.DataFrame(exhumed_ridges_raw)

#frozen soil w sublimation (link):

frozen_soil_raw = {'n_or_v_value' : [2,3,4,5,6,7,8,''],
                 'n' : [122,45,22,'','','','',''],
                 'v' : ['',9,49,24,5,1,'',''],
                 }

frozen_soil = pd.DataFrame(frozen_soil_raw)


#northern plains polygons (link):

northern_planes_raw = {'n_or_v_value' : [2,3,4,5,6,7,8,''],
                 'n' : [120,157,38,'','','','',''],
                 'v' : ['',7,58,55,27,8,2,''],
                 }

northern_planes = pd.DataFrame(northern_planes_raw)



#utopia planitia (link) :

utopia_planetia_raw = {'n_or_v_value' : [2,3,4,5,6,7,8,''],
                 'n' : [16,41,3,'','','','',''],
                 'v' : ['',1,7,8,6,2,'',''],
                 }

utopia_planetia = pd.DataFrame(utopia_planetia_raw)


#mawrth vallis smectites (link):

mawrth_vallis_raw = {'n_or_v_value' : [2,3,4,5,6,7,8,''],
                 'n' : [73,232,39,1,'','','',''],
                 'v' : ['',8,33,81,42,7,2,''],
                 }

mawrth_vallis = pd.DataFrame(mawrth_vallis_raw)


 # # #processing Mars data starts here# # #

## for any data frame named above, use average_n_v(df_name) function to return calculated \bar{n} and \bar{v} values!
##

def average_n_v(df):

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

