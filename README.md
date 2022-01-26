# Wordle Letter Distributions

NOTE: If you want the wordle answers, see [answers (spoilers)](data/searchableAnswers.txt)

NOTE: This is not a wordle solver, there are plenty of those on the internet. This is just some stats for me to check out

# About

Like everyone else, I was talking about [wordle](https://www.powerlanguage.co.uk/wordle/), and the best starting words. It was pointed out that the most common letters might be different among 5-letter words vs the entire english language. Thus... this small project to see the distributions of letters among 5-letter words.

I took valid words accepted by and plotted the occurances of each letter, was well as the most common letters within each position (1-5)

# Findings

We see that common starter words such as ADEIU are actually quite bad. Not only are there more common consonants such as r, s, and t, but the position of the letters is not that common in eliminating answers. Instead, the best words are things like REAIS, SOARE, ROATE, or RAISE, which have 3 vowels and the common letters R, S, E. 

* The most common letters in english (in order of high to low frequency) are: e, a, r, i, o, t, n. However for 5 letter words it is different: s, e, a, o, r, i, l, t
* The most common 5-letter starting letter is S, and by a substantial amount.
* Vowels are the most common 2nd letter, followed by r
* Pending...

# Graphs

![](img/total.png)
![](img/englishTotal.png)
![](img/1.png)
![](img/2.png)
![](img/3.png)
![](img/4.png)
![](img/5.png)
![](img/compTotal.png)

