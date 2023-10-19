#### SER494: Exploratory Data Munging and Visualization
#### Exploring Toxicity in League of Legends (title)
#### Nicolas Coles (author)
#### 10/17/2023 (date)

## Basic Questions
**Dataset Author(s):** Nicolas Coles

**Dataset Construction Date:** 10/14/2023

**Dataset Record Count:** 1278

**Dataset Field Meanings:** 
Category: Category of toxicity that a person may exude or talk about.
Title: Title of the reddit post from the r/leagueoflegends subreddit.
Content: Content of each post, the body to the title in essence.
Date: Date posted for each entry.
Upvotes: The number of upvotes, or likes, that each post received, which can be used
        to measure how people may agree or disagree with certain opinions about toxicity in League of Legends.
Comment_Count: The amount of comments that each post has.
URL: The URL of the post.


**Dataset File Hash(es):** N/A

## Interpretable Records
### Record 1
**Raw Data:** 
Category: 'new'
Title: 'Why the hell were EQ and DH gutted'
Content: 'These runes werenâ€™t even that good, and were niche on a few champs, now theyâ€™re literally unusable. 
            DH was my favourite rune, and felt far more rewarding then FS, but now Iâ€™m forced to go FS on kha. 
            Thereâ€™s absolutely no rune diversity now. Assassins have to go first strike, or build bruiser and go conq.
            Revert the domination nerfs pls :)'
Author: 'Mr_Bear_Tamer'
Date: 1697505212 
Upvotes: 1
Comment_Count: 0
URL: https://www.reddit.com/r/leagueoflegends/comments/179ma57/why_the_hell_were_eq_and_dh_gutted/

**Interpretation:** 
On 10/17/2023, Reddit user "Mr_Bear_Tamer" posted a complaint on the Reddit subreddit r/LeagueOfLegends about an aspect
of the game balance in League of Legends. The user believes that the removal of a few runes were unnecessary and then went on
to complain about other runes that are overpowered in their opinion as well. This type of frustration highlists a key problem 
that contributes to the video game community's toxicity, as the frustration may likely be taken out on other players in real matches,
since they believe that the game is not balanced in the aspect of runes.


### Record 2
**Raw Data:**
Category: 'new'
Title: 'What's wrong with late night ranked?'
Content: 'I don't mean like "they're mentally unwell" but rather like the ones who go: this 
        is just my drunk account/I'm high/this is my siblings account or the ones who just flame, afk, 
        both or are just troll. Example of trolling: enemy diving &gt; Yasuo gets in knockup + ult &gt; 
        enemy survives with 5-10% HP &gt; ADC just stands and watches, while in range. Not aa'ing the diving opponent, not using abilities on them, nothing.'
Author: 'Traveling_Solo'
Date: '1697504472' 
Upvotes: 1
Comment_Count: 2
URL: https://www.reddit.com/r/leagueoflegends/comments/179m0y7/whats_wrong_with_late_night_ranked/
**Interpretation:** 
On 10/17/2023, Reddit user "Traveling_Solo" posted a complaint about bad teammates in his games. They claim that late at 
night, League of Legends players tend to play the game and not take it seriously, which means that it ruins their games
because of League of Legends' high dependability on other teammates during matches. 

## Background Domain Knowledge
Online gaming communities have always encountered the big problem of toxicity in their games. People can find many different things to get frustrated about, and frustration can easily transform into hatred and anger,
which is what leads to toxicity in the video game League of Legends. Before a match even starts, players pick the champion that
they will play that match; survey findings suggest that players find certain types of champions as extremely toxic picks;
this means that frustration can begin before a match even starts (https://comicbook.com/gaming/news/league-of-legends-survey-toxic-players/).
"Toxicity in games usually takes the form of abusive or negative language behavior. In effect, this is cyberbullying",
which is why it is such a big problem in an online community (https://smhp.psych.ucla.edu/pdfdocs/gaming.pdf).
The community of this video game suggests that the reason why League of Legends is so toxic is due to its lonely nature,
miscommunication, ranked pressure, and bad teammates can all culminate in an isolated experience that makes the players take
the game too seriously, akin to a popular sport. The game is so complex that winning requires a competent team with good communication.
(https://www.reddit.com/r/leagueoflegends/comments/16yi4va/league_of_legends_is_such_a_lonely_experience/).

## Data Transformation
### Text Cleaning
**Description:** 
Removing punctuation, special characters, and converting text to lowercase for the title and content of each post.

**Soundness Justification:** 
This transformation ensures that textual data and keywords are consistent in order to minimize outliers from user typos. 
It does not introduce errors or outliers because they simply improve the quality and uniformity of the data.

## Category Assignment
**Description:** 
Reddit posts are categorized into pre-defined categories of frustration/toxicity from players, such as "Bad Teammates" or "Champion Design."
**Soundness Justification:** 
This operation categorizes posts according to their content and helps understand the underlying reasons for toxicity and frustration
in League of Legends. The categories are shown in a column that was irrelevant before the transformation, therefore changing the column
does not damage the data. As long as the selected keywords are relevant to the categories, it does not introduce errors or outliers.

## Date Conversion
**Description:** 
Convert the API's date storage method into human-readable dates.
**Soundness Justification:** 
Converting the date timestamps to human-readable dates makes the data more interpretable, it does not alter the semantics of the data
and enhances its presentation, therefore it introduces no outliers or errors.


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

