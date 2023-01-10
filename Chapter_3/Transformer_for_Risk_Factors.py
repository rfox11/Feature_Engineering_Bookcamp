# custom transformer for RiskFactors

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import MultiLabelBinarizer

class DummifyRiskFactor(BaseEstimator, TransformerMixin):
    def __init__(self) -> None:
        super().__init__()
        self.label_binarizer = None
    
    def parse_risk_factors(self, comma_sep_factors):
        ''' hello, hi -> ['hello', 'hi']'''
        try:
            return [s.strip().lower() for s in comma_sep_factors.split(',')]
        except:
            return []

    def fit(self, X, y=None):
        self.label_binarizer = MultiLabelBinarizer()
        self.label_binarizer.fit(X.apply(self.parse_risk_factors))
        return self
    
    def transform(self, X, y=None):
        return self.label_binarizer.transform(X.apply(self.parse_risk_factors))