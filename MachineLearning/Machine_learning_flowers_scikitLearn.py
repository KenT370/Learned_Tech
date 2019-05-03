
# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from numpy import array
from sklearn.model_selection import KFold
from numpy.random import seed
from numpy.random import rand
 #Load Dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length','sepal-width','petal-length','petal-width','class']
dataset = pandas.read_csv(url,names = names)

# Descriptions
print(dataset.describe())
# Class Distributions
print(dataset.groupby('class').size())
#Univariate Plots (box and whisker) done because
# the input variables are numeric
dataset.plot(kind = 'box',subplots=True,layout=(2,2),sharex=False,sharey=False)
plt.show()
#histogram
dataset.hist()
plt.show()
#Multivariate plots(loks at interactions btw variables)
#ex.scatterplot btw variables
scatter_matrix(dataset)
plt.show()

#split out validation dataset, large portion will be used
#to train models and small portion will be used to see if it got it right
array = dataset.values
x = array[:,0:4] 
y = array[:,4]
validation_size = 0.20
seed = 7
x_train,x_validation,y_train,y_validation = model_selection.train_test_split(x,y,test_size = validation_size,random_state = seed)
#Test Options and evaluation metric
seed = 7 #pseudorandom # generator
scoring = 'accuracy'
### Not included in original tutorial
### but using K-Fold cross validation to split data
kfold = KFold(3,True,1)
for train, test in kfold.split(array):
    pass

# Spot Check Algorithms
models = []
models.append(('LR',LogisticRegression()))
models.append(('LDA',LinearDiscriminantAnalysis()))
models.append(('KNN',KNeighborsClassifier()))
models.append(('CART',DecisionTreeClassifier()))
models.append(('NB',GaussianNB()))
models.append(('SVM',SVC()))

# Evaluate each model in turn
results = []
names = []
for name,model in models:
   kfold = model_selection.KFold(n_splits=10,random_state=seed)
   cv_results = model_selection.cross_val_score(model,x_train,y_train,cv=kfold,scoring = scoring)
   results.append(cv_results)
   names.append(name)
   msg = '%s:  %f (%f)' % (name,cv_results.mean(),cv_results.std())
   print(msg)
   
# Compare Algorithms
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show   
# The SVM model was the most accurate
# Make predictions on validation dataset
svm = SVC()
svm.fit(x_train,y_train)
predictions = svm.predict(x_validation) #using x val data the algorithm predicts the class of flower
print(accuracy_score(y_validation,predictions)) #compares the predicted data vs the actual data
print(confusion_matrix(y_validation,predictions)) #prints confusions matrix which indicates the erros made
print(classification_report(y_validation,predictions)) #breaks down each class by precision, recall, f1-score, and support

   
   
   
   
   
   
   
   
   
   