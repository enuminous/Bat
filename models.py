import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import RobustScaler

class LogisticModel:
    def __init__(self, random_state=23, C=1.0):
        self.scaler = RobustScaler()
        self.model = LogisticRegression(max_iter=5000, random_state=random_state, C=C)
        self.constant_ = None

    def fit(self, X, y):
        y=np.asarray(y,dtype=int)
        if len(np.unique(y))<2:
            self.constant_=float(y.mean()) if len(y) else 0.0
            return self
        self.scaler.fit(X)
        self.model.fit(self.scaler.transform(X),y)
        return self

    def predict_proba(self, X):
        if self.constant_ is not None:
            return np.full(len(X),self.constant_)
        return self.model.predict_proba(self.scaler.transform(X))[:,1]
