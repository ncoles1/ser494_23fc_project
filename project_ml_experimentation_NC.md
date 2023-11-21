#### SER494: Experimentation
#### Experimentating Categorization of Toxic Posts in League of Legends (title)
#### Nicolas Coles (author)
#### 11/20/2023 (date)


## Explainable Records
### Record 1
**Raw Data:**
(These two get combined)
Title: 'so what exactly are the roadblocks preventing riot from having a balanced game after 13 years'
Content: 'dont get me wrong im not an expert on the subject so my opinion probably means squat but ive been playing league for about 8 years so i at least know what some things are or were like the obvious ones are'


Prediction Explanation:** The model predicted this to be Champion Design. While it should be classified as Game Balance, in the original data it is also classified as Champion Design, which means that the model did a good job and that I need to make the dataset better in the future.
However, Champion Design is part of game balance, which means that the prediction is not useless or totally wrong.

### Record 2
**Raw Data:** 
Title: 'why do people in low elo play jayce'
Content: 'im gold 1 atm and whenever i get jayce on my team it just feels like an automatic loss hes supposed to be a lane bully if youre skilled enough but every time i see it they just go even or lose lane by the time 20 minutes rolls around they basically turn into a caster minion for the rest of the game but almost worse since they almost always miss their one skill shot either that or they jump on like a melee minion and die within 2 seconds the champ has one of the worst win rates in the game right now  jayce build with highest winrate  lol runes items and skill orderhttpsugglolchampionsjaycebuildrankgold   just genuinely curious what compels people to pick him edit okay so i guess people think its more fun to cosplay huni than win the game '

Prediction Explanation:** The model predicted Champion Design as the category. This is a correct category, as you can clearly see the user that posted this is complaining that the champion is not beginner friendly, however it can also be classified as bad teammates since he complains that the issue is low elo players playing a complicated character, not the character being bad itself. However, this prediction does shed light on the reason for toxcity on League of Legends, which is the end goal of the model.

## Interesting Features
### Feature A
**Feature:** Title

**Justification:** The title of each post is usually a great indicator of what posters are going to complain about in the game, since it usually summarizes the intent behind the post.
This means that the title is an almost necessary feature for accurate predictions.

### Feature B
**Feature:** Content

**Justification:** The content of each post is usually where users will further explain their frustrations with League of Legends, therefore it is a great indicator of what exactly the user may be frustrated about.

## Experiments 
### Varying A: Title
**Prediction Trend Seen:** By using only the titles instead, the accuracy of the initial model actually went up to 0.683, but all the other models' accuracies went down.

### Varying B: Content
**Prediction Trend Seen:** By using only the content instead, the accuracies changed to an insignificant degree.

### Varying A and B together: Title & Content
**Prediction Trend Seen:** When both features are used together, the accuracy tends to always be better than when using each of them separately.

### Varying A and B inversely: Title & Content (Content is weighed to be more important)
**Prediction Trend Seen:** When putting more weight on the Content, the predictions tend to have a slightly lower accuracy, but not by much.
