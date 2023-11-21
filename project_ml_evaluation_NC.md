#### SER494: Machine Learning Evaluation
#### Classifying Toxicity in League of Legends (title)
#### Nicolas Coles (author)
#### 11/20/2023 (date)

## Evaluation Metrics
### Metric 1
**Name:** Accuracy

**Choice Justification:** Accuracy works best as the baseline metric since it measures the overall correctness of the model's predictions against the training data.

Interpretation:** An accuracy score of 0.8452830188679246 for example means that the model more or less predicted 84% of the test data correctly.

### Metric 2
**Name:** F1-Score

**Choice Justification:** F1-Score takes the average of the precision and recall scores for each category that is being predicted.


## Alternative Models
### Alternative 1: Random Forest
**Construction:** This model uses Scikit-learn's RandomForestClassifier library,
it operates by constructing multiple decision trees during training and then merges their predictions to obtain the most accurate and stable ones.
It is set up in a similar way to the first model, but the parameters for the model training are:
n_estimators=100, random_state=42 where n_estimators is the number of trees in the forest.

**Evaluation:** The Random Forest Classifier showed greater accuracy than the initial model, as it had better performance for both
accuracy (0.845) and F1-Scores.

### Alternative 2: Gradient Boosting
**Construction:** This model used Scikit-learn's GradientBoostingClassifier, which repeatedly selects a function that leads in the direction of a negative gradient so that it can minimize a loss function (Gradient boosting).
Its parameters are also n_estimators=100, random_state=42, where n_estimators is the number of boosting stages to perform. 

**Evaluation:** This model had the best performance overall when looking at the F1-scores and the accuracy of 0.875.

### Alternative 3: Support Vector Machine
**Construction:** This model was trained using a Support Vector Machine with a linear kernel and the same random state as the other models.
SVM works by mapping data in a way so that data points can be categorized. A separator between categories is found, then data is transformed in such a way that the separator looks like a hyperplane.

**Evaluation:** This model had an accuracy of 0.732 and better F1-scores than the initial model, but was not as good as the other two alternatives.

## Visualization
### Category Histogram
**Analysis:** 
The category histogram provides an overview of the distribution of Reddit posts that fall under each category.
The graph shows that bad teammates are the number one reason for toxicity in League of Legends, which is the number one most
complained about issue in the game. This means that matchmaking and skill issues in the game in the game must be prevalent, and thus should be the focus of 
the developers to try and fix, potentially by implementation of a better MMR system and making the barrier of entry into the game easier.

### Comment Count Scatter
**Analysis:** 
The comment count scatter plot shows the distribution of how many comments each post has. Usually, the more controversial or
agreeable that a post is, the more comments it will have, which may be used to weigh the posts in the future in order to better interpret the data.
It can also help understand which aspects of the game are more likely to lead to community engagement and whether it is positive or
negative engagement.

### Upvotes Vs. Comment Count Scatter
**Analysis:** 
The scatter plot of Upvotes Vs. Comment Count shows the relationship between post popularity and community engagement.
Analyzing this data can allow us to determine if posts discussing a specific topic receive more upvotes and comments, thus engagement.
Additionally, it can reveal whether positive or negative sentiments are more likely to gain attention and support from the community.

### Upvotes Vs. Date Scatter
**Analysis:** 
The Upvotes Vs. Date scatter plot helps understand the dynamics of post popularity over time. By visualizing how upvotes 
change over time, we can identify patterns in categories, and tell whether certain categories become more or less popular 
as time progresses, allowing the exploration of the constantly evolving sentiments of the players and community.


## Best Model

**Model:** Gradient Boosting Classifier Model