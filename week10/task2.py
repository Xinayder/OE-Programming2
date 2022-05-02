import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# %matplotlib inline

class mr:

  # Evaluates the gradient of cost function (J). Hint: You can use this to optimize w
  def grad(self,x,y,w,alpha):
    grad_J = grad_J - alpha * self.computeCost(x,y,w) # Your code
    return grad_J

  # This function calculates the cost (J)
  def computeCost(self,x,y,w):
    J = 0    # J is cost function
    # write your code to calculate J
    m = len(y)
    for i in range(len(y)):
      J = J + (1/(2*m))*np.sum(np.subtract(np.dot(x,np.transpose(w)),y)**2)
    return J
  
  # This function optimizes the weights w_0, w_1, w_2. Batch Gradient Descent method
  def bgdMulti(self, x, y, w, alpha, iters):
    m =  len(y)  # number of training examples
    w = w.copy() # To keep a copy of original weights
    
    J_history = []   # Use a python list to save cost in every iteration

    for i in range(iters):
      # Loop to update weights (w vector)
      # Also save cost at every step
      J = self.computeCost(self,x=x,y=y,w=w)
      J_history.append(J)
      w[i] = w[i]- alpha * np.diff(J)

    return w, J_history
  
  # Estimate the price of a 4 bedrooms, 2.5 bathrooms, 2570 sq. feet area, 2 floors, 2005 yr. built
  # You need to rescale all the values, mu is mean of all X data of each column, sigma is standard deviation of X data. mu , sigma will be vector
  # You need to do feature normalization of all X (see lab notes)
  def predict(self, mu, sigma):
    price =  mu * sigma # predict the price of the house
    
    return price

  def normalization(lista):
    minim = min(lista)
    maxim = max(lista)
    return_arr = []
    for i in lista:
      return_arr.append((i - minim)/(maxim - minim))
    return return_arr

if __name__ == '__main__':
  df = pd.read_csv("prob2data.csv")
  df = df.drop(['id'],1)
  df = df.dropna()
  normalized_df=(df-df.min())/(df.max()-df.min())
  print(normalized_df)
  X = normalized_df[['bedrooms','bathrooms','sqft_living','floors','yr_built']]
  Y = df['price']
  w = np.zeros((len(X)+1,5),dtype=float)
  #result = mr.bgdMulti(mr,X,Y,w,alpha=0.01,iters=50)