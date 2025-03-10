from pyVS.pyVoxelStats.pyVoxelStatsLM import pyVoxelStatsLM

model_string = 'Flubet_scan ~ MMSE + Age + C(Gender_code)'
csv_file = '/data/data03/sulantha/VoxelStatsPaper/CSVs/DataCSV.csv'
mask_file = '/home/sulantha/PycharmProjects/pyVoxelStats/VoxelStatsTestData/Masks/cerebellum_mask_rsl_8mm_blur_075_mask2_8mm_test_mask.mnc'
voxel_variables = ['Flubet_scan']
#subset_string = ''
file_type = 'minc'

lm = pyVoxelStatsLM(file_type, model_string, csv_file, mask_file, voxel_variables, weights=1.0)
lm.enable_save_model()
lm.set_no_parallel(True)

lm.set_up_cluster()

#lm.set_up_cluster(profile_name='sgeovn', no_start=True, clust_sleep_time=140)
lm.evaluate()
models = lm.models
res = lm.res

lm.save('/home/sulantha/Desktop/MMSE_Flu2_pyV.mnc', 'tvalues', 'MMSE')

## Pickle analysis if needed to write results later
import pickle
## Saving
pickle.dump(lm, open('VoxelStatsTestData/Pickles/LM.pkl', 'wb'))
## Loading Back
lm2 = pickle.load(open('VoxelStatsTestData/Pickles/LM.pkl', 'rb'))

lm2.save('/home/sulantha/Desktop/MMSE_Flu2_pyV2.mnc', 'tvalues', 'MMSE')