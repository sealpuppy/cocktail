import numpy as np
import os
from data_process import gen_spectrogram
import json


root_dir = '/home/tk/Documents/'
sliced_pool_path = '/home/tk/Documents/sliced_pool/'
mixed_pool_path =  '/home/tk/Documents/mix_pool/'
clean_path = '/home/tk/Documents/clean/'
cleanlabel_path = '/home/tk/Documents/clean_labels/'

full_audio = ['birdstudybook', 'captaincook', 'cloudstudies_02_clayden_12', 
              'constructivebeekeeping',
              'discoursesbiologicalgeological_16_huxley_12', 
              'natureguide', 'pioneersoftheoldsouth', 
              'pioneerworkalps_02_harper_12', 
              'romancecommonplace', 'travelstoriesretold']
              
              
<<<<<<< HEAD
blocks = 6
=======
blocks = 11
>>>>>>> 118773a3c20c82a5394ee0b07195935867009b18

for i in range(blocks):
    for ind, name in enumerate(full_audio):
        
        all_clean_spec = []
        all_clean_label = []

        if (mixed_pool_path + 'feature/' + name) == False:
            os.mkdir(mixed_pool_path + 'feature/' + name)
        
        if (mixed_pool_path + 'feature_label/' + name) == False:
            os.mkdir(mixed_pool_path + 'feature_label/' + name)


        file_name_list = os.listdir(sliced_pool_path + name + '/clean/')
        file_name = np.random.choice(file_name_list, 1000)
        

        for k in file_name:
            spec = gen_spectrogram(sliced_pool_path + name + '/clean/' + k)
            print (k)
            all_clean_spec.append(spec)
            all_clean_label.append(ind)
            print (ind)
            
            
        all_clean_spec = np.array(all_clean_spec)
        all_clean_spec = np.stack(all_clean_spec)

        all_clean_label = np.array(all_clean_label)
        all_clean_label = np.stack(all_clean_label)

            
        print ("name = ", name , ", shape = ", all_clean_spec.shape)
        print ("label = ", name , ", shape = ", all_clean_label.shape)

    
<<<<<<< HEAD
        with open(clean_path + name + '_' + str(i) + '.json', 'w') as jh:
            json.dump(all_clean_spec.tolist(), jh)

        with open(cleanlabel_path + name + '_' + str(i) + '.json', 'w') as jh:
=======
        with open(mixed_pool_path +  'feature/' + name + '/' + name + str(i) + '.json', 'w') as jh:
            json.dump(all_clean_spec.tolist(), jh)

        with open(mixed_pool_path +  'feature_label/' + name + '/' + name + str(i) + '.json', 'w') as jh:
>>>>>>> 118773a3c20c82a5394ee0b07195935867009b18
            json.dump(all_clean_label.tolist(), jh)


