# Typewarz.io

![Image of homepage](images/home.png)

A minimalistic typing test website using Django and Vanilla JS that tracks user keystrokes to provide accuracy and WPM measurements. Also has an integrated User database that provides previous test data and allows for users to make their own accounts.

## The Goal?
Type all the words in the shortest time possible!

## Made using:
* HTML
* CSS
* JavaScript
* Python
* Django

## A personalized account:

![Image of login](images/login.png)

An account that stores a user's max word per minute, max accuracy, min time and the last 5 test results.

![Image of account](images/account.png)

## The test page

![Image of test page](images/test.png)

50 words that are generated randomly and a timer is displayed. The timer begins with the first key stroke. 

The color scheme:
* gray - to be typed
* white - correct
* red - incorrect

## The results page 

![Image of results page](images/results.png)

The results page displays the user's words per minute, their total time and accuracy as a percentage.

Users have the option to redo the test and save their results.

## How are the words generated?
50 words are generated randomly from a list of words that have been stored in our database. Although the words are random, the approximate difficulty of each set of words remains the same, as the number of words of each length stays consistent across each randomly generated set.

## How are the keystrokes tracked
A variable is used to store and mimic the user's keystrokes. Every keydown event is recorded and then compared to the expected event which is then used to check for correctness and accordingly colored.

The timer begins with the first keystroke. As the seconds pass, the minutes and hours are calculated and displayed.

## How are the results calculated?
The accuracy is calculated by dividing the correct typed by the total words.
The WPM is calculated using the formula: ((50 * accuracy)/total time (in seconds)) * 60.

## What is Django?
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It???s free and open source.
