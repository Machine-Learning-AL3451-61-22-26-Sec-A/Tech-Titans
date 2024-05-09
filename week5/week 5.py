{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# MACHINE LEARNING LAB - 5 ( naïve Bayesian Classifier )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**5. Write a program to implement the naïve Bayesian classifier for a sample training data set stored as a .CSV file. Compute the accuracy of the classifier, considering few test data sets.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "THe first 5 values of data is :\n",
      "     Outlook Temperature Humidity  Windy PlayTennis\n",
      "0     Sunny         Hot     High  False         No\n",
      "1     Sunny         Hot     High   True         No\n",
      "2  Overcast         Hot     High  False        Yes\n",
      "3     Rainy        Mild     High  False        Yes\n",
      "4     Rainy        Cool   Normal  False        Yes\n"
     ]
    }
   ],
   "source": [
    "# import necessary libarities\n",
    "import pandas as pd\n",
    "from sklearn import tree\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "from sklearn.naive_bayes import GaussianNB\n",
    "\n",
    "# load data from CSV\n",
    "data = pd.read_csv('tennisdata.csv')\n",
    "print(\"THe first 5 values of data is :\\n\",data.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "The First 5 values of train data is\n",
      "     Outlook Temperature Humidity  Windy\n",
      "0     Sunny         Hot     High  False\n",
      "1     Sunny         Hot     High   True\n",
      "2  Overcast         Hot     High  False\n",
      "3     Rainy        Mild     High  False\n",
      "4     Rainy        Cool   Normal  False\n"
     ]
    }
   ],
   "source": [
    "# obtain Train data and Train output\n",
    "X = data.iloc[:,:-1]\n",
    "print(\"\\nThe First 5 values of train data is\\n\",X.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "The first 5 values of Train output is\n",
      " 0     No\n",
      "1     No\n",
      "2    Yes\n",
      "3    Yes\n",
      "4    Yes\n",
      "Name: PlayTennis, dtype: object\n"
     ]
    }
   ],
   "source": [
    "y = data.iloc[:,-1]\n",
    "print(\"\\nThe first 5 values of Train output is\\n\",y.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Now the Train data is :\n",
      "    Outlook  Temperature  Humidity  Windy\n",
      "0        2            1         0      0\n",
      "1        2            1         0      1\n",
      "2        0            1         0      0\n",
      "3        1            2         0      0\n",
      "4        1            0         1      0\n"
     ]
    }
   ],
   "source": [
    "# Convert then in numbers \n",
    "le_outlook = LabelEncoder()\n",
    "X.Outlook = le_outlook.fit_transform(X.Outlook)\n",
    "\n",
    "le_Temperature = LabelEncoder()\n",
    "X.Temperature = le_Temperature.fit_transform(X.Temperature)\n",
    "\n",
    "le_Humidity = LabelEncoder()\n",
    "X.Humidity = le_Humidity.fit_transform(X.Humidity)\n",
    "\n",
    "le_Windy = LabelEncoder()\n",
    "X.Windy = le_Windy.fit_transform(X.Windy)\n",
    "\n",
    "print(\"\\nNow the Train data is :\\n\",X.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Now the Train output is\n",
      " [0 0 1 1 1 0 1 0 1 1 1 1 1 0]\n"
     ]
    }
   ],
   "source": [
    "le_PlayTennis = LabelEncoder()\n",
    "y = le_PlayTennis.fit_transform(y)\n",
    "print(\"\\nNow the Train output is\\n\",y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy is: 0.6666666666666666\n"
     ]
    }
   ],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.20)\n",
    "\n",
    "classifier = GaussianNB()\n",
    "classifier.fit(X_train,y_train)\n",
    "\n",
    "from sklearn.metrics import accuracy_score\n",
    "print(\"Accuracy is:\",accuracy_score(classifier.predict(X_test),y_test))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
