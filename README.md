# ML Horse Prediction

## Team Members

- John O'Sullivan
- Brianne Coffey
- Noel Castillo
- Sebasitan Kurpiel

## About Bet-On-Us

Horse raching, once an event only for the elite and royales of society has become a everyday day occurance. The ancient Greek Olympics had events for both chariot and mounted horse racing. Since the ancient sport was conceived not much has changed but how bets are placed. Using today's machine learning, our team, <b>bet on us</b>, will be using from models from the skilearn library to determine what are the best features and horses to bet on.

## Prerequisites

Atom is a text and source code editor which works well for macOS, Linux, and Microsoft Windows. Atom is free and can be downloaded from the internet. Once Atom is installed make sure Python works. To get Python running on Atom head to preferences, click on install, search for atom-runner and install it. On Windows that’s all that is needed but on Mac there is one more step. Under the Atom menu go to open your config, at the end of your config.csn file add runner: python: “/user/local/bin/python3”.

Anaconda must also be installed in order to run the second SVC model of our project. Anaconda is a freemium open source distribution of Python and can be downloaded from the internet. Once Anaconda is installed, use Jupyter notebook to run the code. 

## Code

To run this code you will need:

* Python 3
* Scikit-learn
* Numpy
* Pandas 
 
## Goal

The goal was to use three different models from the skilearb library in order to find which models woekws best in predicting the winning horse of the race.

## About DataSet

All features will have a value of 0 or 1, the raw dataset can be found here: <a href="https://github.com/dominicplouffe/HorseRacingPrediction/tree/master/data">Github</a>.

<a href="https://docs.google.com/presentation/d/1mBy5keCI7yhRvQnToHzveEUy8CXaDpChe2sufttldMI/edit?usp=sharing">Google Presentation</a>

| # | Row Name | Description |
| --- | --- | --- |
| 1 | Post | If the horse is in the post position 1, 2, 3, 4, or 5 “1” else “0” |
| 2 | Speed | If horse was in the top 2 finish speeds, “1” else “0” |
| 3 | Horse Win % | If horse’s win % is over 50%, “1” else “0” |
| 4 | Horse WPS % | If horse’s WPS % is over 60%, “1” else “0” |
| 5 | Horse ROI | If horse’s lifetime ROI for a $2 bet is over $2, “1” else “0” |
| 6 | Driver Win % | If driver’s win % is over 50%, “1” else “0” |
| 7 | Driver WPS % | If driver’s WPS % is over 60%, “1” else “0” |
| 8 | Driver ROI | If driver’s lifetime ROI for a $2 bet is over $2, “1” else “0” |
| 9 | Trainer Win % | If trainer’s win % is over 50%, “1” else “0” |
| 10 | Trainer WPS % | If trainer’s WPS % is over 60%, “1” else “0” |
| 11 | Trainer ROI | If trainer’s lifetime ROI for a $2 bet is over $2, “1” else “0” |
| 12 | Minimum Races | If horse has races more than 5 races “1” else “0” |
| 13 | Previous Break | If horse has broken strides in the last 2 races, “0” else “1” |
| 14 | Days Since Last Race | If horse has raced over the last 21 days, “1” else “0” |
| 15 | Same Track | If horse is racing on the same track as the previous race, “1” else “0” |
| 16 | Same Driver | If horse’s driver is the same as the previous race, “1” else “0” |
| 17 | Last Race Result | If the horse finished in first in the previous race, “1” else “0” |
| 18 | Last Race WPS | If the horse finished in a WPS position in the last race, “1” else “0” |
| 19 | Last Three Race | If the horse finished in first in the last 3 races, “1” else “0” |
| 20 | Purse | If the purse is the same as the last race, “0” if it is lower “-1”, else “1” |

## Our Models
The three different models used in this project were K-nearest neighbors, decision tree, and Support Vector Classification. 


