# Lyrics Extractor
Find the lyrics of a song and writes all the unique words into a csv file.

## Overview
My main aim during the project was to learn web scraping and combining it with the love of music, I have written this script which gives the frequency table of the words in the lyrics.
	
## Description
Using a powerful word scrapper beautiful soup, I have used some basic logics to finally output csv.

## Dependencies
This is the list of dependencies for running this application.
 * **Beautiful Soup**
 * **operator**
 * **seaborn**
 * **Pandas**
 * **Numpy**
 * **Requests**
 
  
## How to use
1. Download or clone this repository.
2. Extract to some location
3. First, run **```lyrics-extractor.py```** from **```lyrics-extractor```** folder.<br>
4. Enter the URL in command prompt. 
5. CSV file will be created. 

## Future Work
1. Using the data extracted above we can do couple of improvments to the data extracted itself such as **lemmatization** ( consider go, goes, going all as one) and removing **stop words**(ignoring words like to, by, i, to, etc.)
2. By using this data set all sorts od intersting challenges can begiven to users after they have listened to a particular songs.
3. Make the process of giving input URL can be reduced to just playing the song on your computer and it will automatically start generating a quiz. 
4. Making an online community to share and challange your friends on the same quiz.
