import numpy as np
sys.path.append(os.pardir)
from common.layers import Convolution

image = np.arange(16).reshape(1,1,4,4)
weight = np.ones((1,1,2,2))
b = np.zeros((1,))
print(image)
print(weight)
print(b)
conv = Convolution(weight, b)
cout = conv.forward(image)
print(cout)
print(cout.shape)


######## Row Level

import sys, os
sys.path.append(os.pardir)
import numpy as np
pad=0
stride=1
filter_h = 2
filter_w = 2
input_data = np.arange(16).reshape(1,1,4,4)
# print(input_data.shape)
# print(input_data)

N, C, H, W = input_data.shape
out_h = (H + 2*pad - filter_h)//stride + 1
out_w = (W + 2*pad - filter_w)//stride + 1

img = np.pad(input_data, [(0,0), (0,0), (pad, pad), (pad, pad)], 'constant')
# col = np.zeros((N, C, filter_h, filter_w, out_h, out_w))

# print(img.shape)
# print(img)
# print(col.shape)

# for y in range(filter_h):
#     y_max = y + stride*out_h
#     for x in range(filter_w):
#         x_max = x + stride*out_w
#         col[:, :, y, x, :, :] = img[:, :, y:y_max:stride, x:x_max:stride]

# print(col)    # (1,1,2,2,3,3)            

col = np.zeros((N, C, out_h, out_w, filter_h, filter_w))
for y in range(out_h):
    y_max = y + stride*filter_h
    for x in range(out_w):
        x_max = x + stride*filter_w
        col[:, :, y, x, :, :] = img[:, :, y:y_max:stride, x:x_max:stride]

print(col)    # (1,1,3,3,2,2)            
    
# col[:, :, 0, 0, :, :] = img[:, :, 0:3:1, 0:3:1]
# col[:, :, 0, 1, :, :] = img[:, :, 0:3:1, 1:4:1]
# col[:, :, 1, 0, :, :] = img[:, :, 1:4:1, 0:3:1]
# col[:, :, 1, 1, :, :] = img[:, :, 1:4:1, 1:4:1]

# print(col)
# ret = col.transpose(0, 4, 5, 1, 2, 3)
# # print(ret.shape)  # (1, 3, 3, 1, 2, 2)
# # print(ret)
# col = ret.reshape( N*out_h*out_w, -1 )
# print(col.shape)
# print(col)

# W = np.ones((1,1,2,2))
# print(W)
# col_W = W.reshape(1, -1).T
# print(col_W.shape)

# out = np.dot(col, col_W)  # (9,4)(4,1)
# print( out.shape )
# print(out)
# out = out.reshape(N, out_h, out_w, -1).transpose(0, 3, 1, 2)
# print( out.shape )
# print(out)
