## -*- coding: utf-8 -*-

import numpy as np

def topic_words(model, feature_names, n_top_words):
    """
    Display n_top_words number of words for a model
    and its corresponding feature_names.
    """
    for num_topic, topic in enumerate(model.components_):
        words = np.argsort(topic)[::-1][:n_top_words]
        print('Topic ' + str(num_topic) + ':')
        print(' '.join([feature_names[i] for i in words]))