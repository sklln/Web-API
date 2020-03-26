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

dt_classifier = DecisionTreeClassifierModel('model_resources/covid_feats_2.csv', 'model_resources/covid_labels_2.csv')

def get_prediction_from_single_vector(x_vec=None):
    x_vec_processed = convert_to_features_tensor(x_vec)
    y_pred = dt_classifier.dt.predict([x_vec_processed])
    predicted_label = dt_classifier.labels.columns[y_pred.argmax()]
    return predicted_label


def convert_to_features_tensor(item):
    feat_vec = []
    # feat_vec.append(item.aches_pains)
    # feat_vec.append(item.cough)
    # feat_vec.append(item.diarrhea)
    # feat_vec.append(item.fatigue)
    # feat_vec.append(item.fever_chills)
    # feat_vec.append(item.headache)
    # feat_vec.append(item.running_nose)
    # feat_vec.append(item.breathless)
    # feat_vec.append(item.sneezing)
    # feat_vec.append(item.sore_throat)
    feat_vec.append(item.aches_pains)
    feat_vec.append(item.breathlessness)
    feat_vec.append(item.cough)
    feat_vec.append(item.diarrhea)
    feat_vec.append(item.fatigue)
    feat_vec.append(item.fever)
    feat_vec.append(item.headache)
    feat_vec.append(item.runny_nose)
    feat_vec.append(item.sneezing)
    feat_vec.append(item.sore_throat)
    return feat_vec