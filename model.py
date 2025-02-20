import numpy as np

class AndModel:
    def __init__(self):
        # Parameter
        self.weights = np.random.rand(2)
        self.bias = np.random.rand(1)

    def train(self):
        learning_rate = 0.1
        epochs = 20
        inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
        outputs = np.array([0, 0, 0, 1])        
        for epoch in range(epochs):
            for i in range(len(inputs)):
                total_input = np.dot(inputs[i], self.weights) + self.bias # 총 입력 계산
                prediction = self.step_function(total_input) # 예측 출력 계산
                error = outputs[i] - prediction # 오차 계산

                print(f'inputs[i] : {inputs[i]}')
                print(f'weights : {self.weights}')
                print(f'bias before update: {self.bias}')
                print(f'prediction: {prediction}')
                print(f'error: {error}')
                # 출력

                self.weights += learning_rate * error * inputs[i]
                self.bias += learning_rate * error
                print('====')
                # Weight와 Bias 업데이트

    def step_function(self, x):
        return 1 if x >= 0 else 0
    
    def predict(self, input_data):
        total_input = np.dot(input_data, self.weights) + self.bias
        return self.step_function(total_input)
    