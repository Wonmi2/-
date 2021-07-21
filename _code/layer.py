import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
from common.layers import *
from common.gradient import numerical_gradient
from collections import OrderedDict


class TwoLayerNet:

    def __init__(self, input_size, hidden_size, output_size, weight_init_std = 0.01):
#         print('TwoLayerNet.__init__()')
        # 가중치 초기화
        self.params = {} # dict={key:value}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size) 
        self.params['b2'] = np.zeros(output_size)

        # 계층 생성
        self.layers = OrderedDict() # 순번 지키는 dict
        self.layers['Affine1'] = Affine(self.params['W1'], self.params['b1'])
        self.layers['Relu1'] = Relu()
        self.layers['Affine2'] = Affine(self.params['W2'], self.params['b2'])

        self.lastLayer = SoftmaxWithLoss()
        
    def predict(self, x):
#         print('TwoLayerNet.predict()')
        for layer in self.layers.values():
#             print(x.shape)
            x = layer.forward(x)
#         print("확률x=",x.shape)
        return x
        
    # x : 입력 데이터, t : 정답 레이블
    def loss(self, x, t):
#         print('TwoLayerNet.loss()')
        y = self.predict(x)
        return self.lastLayer.forward(y, t)
    
    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        if t.ndim != 1 : t = np.argmax(t, axis=1)
        
        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy
        
    # x : 입력 데이터, t : 정답 레이블
    def numerical_gradient(self, x, t):
        loss_W = lambda W: self.loss(x, t)
        
        grads = {}
        grads['W1'] = numerical_gradient(loss_W, self.params['W1'])
        grads['b1'] = numerical_gradient(loss_W, self.params['b1'])
        grads['W2'] = numerical_gradient(loss_W, self.params['W2'])
        grads['b2'] = numerical_gradient(loss_W, self.params['b2'])
        
        return grads
        
    def gradient(self, x, t):
#         print('TwoLayerNet.gradient()')
        # forward
        loss = self.loss(x, t)
#         print('loss=',loss)

        # backward
        dout = 1
        dout = self.lastLayer.backward(dout)
#         print('dout.shape=',dout.shape)
#         print('   t[0]=' , t[0])
#         print('dout[0]=' , dout[0])
        
        layers = list(self.layers.values())
        layers.reverse() # 역방향
        for layer in layers:
#             print("dout.shape=",dout.shape )
            dout = layer.backward(dout)
#         print("dout.shape=",dout.shape )
            
        # 결과 저장
        grads = {}
        grads['W1'], grads['b1'] = self.layers['Affine1'].dW, self.layers['Affine1'].db
        grads['W2'], grads['b2'] = self.layers['Affine2'].dW, self.layers['Affine2'].db

        return grads
