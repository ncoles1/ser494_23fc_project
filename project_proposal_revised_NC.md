#### SER494: Project Proposal
#### Understanding League of Legend's Community Problems
#### Nicolas Coles 
#### 9/11/2023 

Keywords: Human behavior, video games, internet communities, league of legends

Description: Toxic behavior and frustration in competitive video games are prevalent issues that game companies face when creating online multiplayer games. Game communities can easily fall to ruin and abandon, which puts off newcomers from trying the game. This project will analyze from Reddit posts in the r/LeagueOfLegends subreddit in order to find out the biggest reasons why players are toxic towards other players, whether it be through abusive chats, spam pinging, or even intentionally trying to lose the game. 

Intellectual Merit: Most modern companies that manage any type of social network necessarily take steps towards reducing the amount of toxicity and cyberbullying that occurs on their platforms. By analyzing the cause, companies will be able to better tackle this problem which can result in more welcoming and stable communities.

Data Sourcing: The data will be produced by gathering posts from the Reddit subreddit r/LeagueOfLegends. The data extracted will be preprocessed and gathered in a .csv format, posts will be retrieved so that posts mentioning complaints about the game or any type of general toxicity are prioritized when being added to the .csv file. The data will be retrieved, cleaned, and displayed through the use of Python libraries such as pandas and matplotlib. After the data is retrieved, it will then be categorized through a categorization machine learning model that can classify what type of posts complain about what type of general category, such as "Bad Teammates" or "Game Balance".

Background Knowledge: 
1. Absolute Beginner’s Guide to League of Legends (https://mobalytics.gg/blog/absolute-beginners-guide-to-league-of-legends/) Retrieved 9/11/2023
2. Flaming and Gaming – Computer-mediated communication and toxic disinhibition (http://essay.utwente.nl/62350/1/Elliott%2C_T.P._-_s0157090_%28verslag%29.pdf) Retrieved 9/11/2023
3. How League Of Legends Enables Toxicity (https://kotaku.com/how-league-of-legends-enables-toxicity-1693572469) Retrieved 9/11/2023

Related Work: 
1. Toxic Behaviors in Team-Based Competitive Gaming: The Case of League of Legends (https://dl.acm.org/doi/abs/10.1145/3410404.3414243) Retrieved 9/11/2023
2. Effects of individual toxic behavior on team performance in League of Legends (https://www.tandfonline.com/doi/full/10.1080/15213269.2020.1868322) Retrieved 9/11/2023
3. Don’t You Know That You’re Toxic: Normalization of Toxicity in Online Gaming (https://dl.acm.org/doi/abs/10.1145/3411764.3445157?casa_token=rosvbKOf2N4AAAAA:jtzAjb8bX6u0QLeNWCDvYTePJ_U482DXF9eZ7HqAY3BaYn_J9TEYLYLAd-dqo6668NJgojGyrwbfkA) Retrieved 10/29/2023
4. Tackling Toxicity: Identifying and Addressing Toxic Behavior in Online Video Games (https://scholarship.shu.edu/dissertations/2798/) Retrieved 10/29/2023
5. Towards a unified theory of toxic behavior in video games (https://www.emerald.com/insight/content/doi/10.1108/INTR-08-2019-0343/full/html?casa_token=eq6AnWLnOkEAAAAA:it0tBtUVY8GHruuIKH1z_jWQ1L-7ahlFPWPuvLO6Zohfroi22e-8jrej-G7w724R7vdggUavcCANxMu4tfnIHXflymTuMrkMyL8ZV97Zom4zOYhzVKC8) Retrieved 10/30/2023
6. Regulating anti-social behavior on the Internet: The example of League of Legends (https://www.ideals.illinois.edu/items/35528) Retrieved 10/30/2023

**Research Objectives**
**RO1:** To describe trends within categories for toxicity.
**RO2:** To predict the category of toxicity of Reddit posts. 
**RO3:** To defend the model for performing the prediction in RO2.
**RO4:** To evaluate casual relationships implied by the RO2 model.
