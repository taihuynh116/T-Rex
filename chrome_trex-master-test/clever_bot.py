import numpy as np
import time

import capturing_objects


URL = "http://www.trex-game.skipser.com/"

clever_params = {'b2': np.array([[ 0.27304736]]), 'W2': np.array([[ 0.91572382, -0.29862268,  0.30955728]]), 'W1': np.array([[-0.02062025,  0.00016742,  0.00381535],
       [ 0.00226537,  0.01325698,  0.02389935],
       [ 0.02300561,  0.01351209,  0.00588823]]), 'b1': np.array([[-0.73119972],
       [-0.05157346],
       [-0.00290758]])}
cle_2_gen23 = {'W1': np.array([[-0.00985001, -0.0029748 , -0.00174466],
       [-0.02531742,  0.01277125,  0.00501999],
       [ 0.00976886, -0.00177337,  0.00834544]]), 'W2': np.array([[ 2.84559397,  1.17383076, -2.60060588]]), 
   		'b1': np.array([[0.5343408 ],
       [0.10894481],
       [0.22580921]]), 'b2': np.array([[-0.04068509]])}

#capturing_objects.chrome_setup(URL)
#time.sleep(3)
capturing_objects.play_game(cle_2_gen23)