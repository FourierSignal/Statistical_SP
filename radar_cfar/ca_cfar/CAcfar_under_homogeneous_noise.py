import numpy as np
import matplotlib.pyplot as plt

import random
from numpy.random import randn



cells_in_beam = 40
window_length = 8

def estimate_noise_around_CUT(range_det_strength,cell_under_test):
    num_guard_cells = 2
    M = int(window_length/2)
    num_train_cells = window_length - num_guard_cells
    lag_start = cell_under_test-M
    lag_end = cell_under_test-num_guard_cells
    
    lead_start = cell_under_test+num_guard_cells
    lead_end = cell_under_test+M

    print(lag_start,lag_end)
    print(lead_start,lead_end)
    
    if lag_start < 0 and lag_end < 0 :
        lag_start = 0
        lag_end = 0
    elif lag_start < 0 and lag_end >= 0 :
        lag_start = 0
        #lag_end = 0
        
        
    if lead_start > cells_in_beam and lead_end > cells_in_beam :
        lead_start = cells_in_beam
        lead_end = cells_in_beam        
    elif lead_start <= cells_in_beam and lead_end > cells_in_beam:
        #lead_start = cells_in_beam
        lead_end = cells_in_beam  
        
    print(lag_start,lag_end)
    print(lead_start,lead_end)   
    
    lag_length = lag_end-lag_start
    lead_length = lead_end - lead_start
    print("lengths=",lag_length ,lead_length)
    actual_window_length = lag_length + lead_length
    print("actual_window_length=",actual_window_length)
    
    #lag_sum = np.sum(range_det_strength[cell_under_test-M : cell_under_test-num_guard_cells])
    #lead_sum = np.sum(range_det_strength[cell_under_test+num_guard_cells : cell_under_test+M])
    
    lag_sum = np.sum(range_det_strength[lag_start : lag_end])
    lead_sum = np.sum(range_det_strength[lead_start : lead_end])

    
    #avg_noise_power = (lag_sum+lead_sum)/window_length
    avg_noise_power = (lag_sum+lead_sum)/actual_window_length
    print("-----------------")
    print("CUT=",cell_under_test)

    
    print(range_det_strength[lag_start : lag_end])
    print(range_det_strength[lead_start : lead_end])
    print(lead_sum,lag_sum,avg_noise_power)
    return avg_noise_power
     
     
def calc_scale_factor(rate_fa):
    alpha = window_length*(rate_fa**(-1/window_length) - 1) # threshold scaling factor
    return alpha

def cfar_threshold(avg_noise_power,rate_fa):
    alpha = calc_scale_factor(rate_fa)
    print("scale_factor=",alpha)
    threshold = alpha * avg_noise_power
    return threshold
     
def range_cfar(range_detection_strength_vetor,rate_fa):
    detection_index = []
    for cell_under_test in range(range_detection_strength_vetor.size):
        avg_noise_power = estimate_noise_around_CUT(range_detection_strength_vetor,cell_under_test)
        threshold = cfar_threshold(avg_noise_power,rate_fa)
        print("CUT=",cell_under_test,"avg_noise_power",avg_noise_power,"threshold=",threshold)
        print("CUT_strength=",range_detection_strength_vetor[cell_under_test])  
        if range_detection_strength_vetor[cell_under_test] > threshold :
            detection_index.append(cell_under_test)
            print("Target")
        else:
            print("noise")
            
             
    #detection_index = np.array(detection_index, dtype=int)
          
    return detection_index
  
  
cells_in_beam = 40

signal_vector_len = 5

signal_strength_vector = np.zeros(cells_in_beam)

signal_addition_indices = []


# this should follow exponential distribution infact
mean_norm = 200
sd_norm = 1
iid_noise = []
for i in range(cells_in_beam):
    #iid_noise.append(randint(0, 10000))
    #iid_noise.append(mean_norm + sd_norm * randn())
    n = np.random.standard_exponential()
    iid_noise.append(n)
    
signal_strength_vector = signal_strength_vector + iid_noise

signal = []
for i in range(signal_vector_len):
    signal.append(randint(100000, 100200))

    
signal_addition_index = 0    
for signal_val in signal:
    #n = randint(0,20)
    n = 8
    if n > 0 and signal_addition_index + n < len(iid_noise):
        signal_addition_index += n
        #print(signal_addition_index)
        signal_strength_vector[signal_addition_index] =+ signal_val
        signal_addition_indices.append(signal_addition_index)
        
    
print(signal_addition_indices)
    
    
    
plt.figure(figsize=(40,10))
cell_no = range(signal_strength_vector.size)
plt.stem(cell_no[:140],iid_noise[:140])
plt.show()


rate_fa = 1/(10^6)
detection_indices = range_cfar(signal_strength_vector,rate_fa)
print(detection_indices)
print(signal_addition_indices)
  
  
  
