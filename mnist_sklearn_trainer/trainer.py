import os
from datetime import datetime
from subprocess import check_call

import mnist
from sklearn.externals import joblib
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

BUCKET_ID = 'television-markup'

X_train = mnist.train_images().reshape(-1, 28 ** 2) / 255
y_train = mnist.train_labels()

knn_clf = KNeighborsClassifier()

param_grid = [
    {
        'weights': ['uniform', 'distance'],
        'n_neighbors': [2, 3, 4, 5]
    }
]

grid_search = GridSearchCV(knn_clf, param_grid, n_jobs=-1, cv=5, verbose=True)
grid_search.fit(X_train, y_train)

model = 'model.joblib'
joblib.dump(knn_clf, model)

model_path = os.path.join('gs://', BUCKET_ID, datetime.now().strftime('knn_clf_%Y%m%d_%H%M%S'), model)
check_call(['gsutil', 'cp', model, model_path])
