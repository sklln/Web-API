from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from joblib import dump, load

class DecisionTreeClassifierModel:
    """
    Assumes you've two separate csv files,
    one with your idx'd integer features looks like [0, 1, 0, 2, etc]
    one with your corresponding binary label vectors [1,0,0,0] for four labels
    """
    def __init__(self, feats_path, labels_path):
        try:
            self.feats = pd.read_csv(feats_path)
            self.labels = pd.read_csv(labels_path)
        except Exception as e:
            print('Issue with your reading:', e)

        self.dt = DecisionTreeClassifier()
        self.dt.fit(self.feats, self.labels)

    def save_load_model(self, save_model_path=None, save_model=False,  model=None):
        if save_model:
            dump(model, save_model_path)
        else:
            return load(save_model_path)

    def get_prediction_from_single_vector(self, x_vec=None):
        """
        Gets prediction for single list feature vector
        :param x_label: list with feature vector
        :return: precition label
        """
        y_pred = self.dt.predict([x_vec])
        predicted_label = self.labels.columns[y_pred.argmax()]
        return predicted_label

dt_classifier = DecisionTreeClassifierModel('model_resources/covid_feats.csv', 'model_resources/covid_labels.csv')

def get_prediction_from_single_vector(x_vec=None):
    x_vec_processed = convert_to_features_tensor(x_vec)
    y_pred = dt_classifier.predict([x_vec])
    predicted_label = dt_classifier.labels.columns[y_pred.argmax()]
    return predicted_label

def convert_to_features_tensor(item):
    # feat_vec = []
    # feat_vec.append(item.Age if type(item.Age)==float else float(item.Age))
    # feat_vec.append(calculate_bmi(item))
    # feat_vec.append(1)
    # feat_vec.append(1 if type(item.Gender)=='female' else 2)
    # feat_vec.append(1 if type(item.Smoking) == 'yes' else 0)
    # feat_vec.append(1)
    # feat_vec.append(1)
    # feat_vec.append(1 if type(item.Exercise) == 'yes' else 0)
    # feat_vec.append(1 if type(item.Alcohol) == 'yes' else 0)
    # feat_tensor = torch.tensor(feat_vec, dtype=torch.float)
    return feat_tensor