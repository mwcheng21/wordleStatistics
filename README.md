# Wordle Statistics

Like everyone else, I was talking about [wordle](https://www.powerlanguage.co.uk/wordle/), and the best starting words. It was pointed out that the most common letters might be different among 5-letter words vs the entire english language. Thus... this small project to see the distributions of letters among 5-letter words.

I took valid words accepted by  and plotted the occurances of each letter, was well as the most common letters within each position (1-5)

We see that common starter words such as ADEIU are actually quite bad. Not only are there more common consonants such as r, s, and t, but the position of the letters is not that common in eliminating answers. Instead, the best words are things like REAIS, SOARE, ROATE, or RAISE, which have 3 vowels and the common letters R, S, E. 

NOTE: This is not a wordle solver, there are plenty of those on the internet.

# Graphs

![](total.png)
![](englishTotal.png)
![](1.png)
![](2.png)
![](3.png)
![](4.png)
![](5.png)

# Findings

* The most common letters in english (in order of high to low frequency) are: e, a, i, r, o, t, n. However for 5 letter words it is different: e, s, a, o, r, i, l, t
* The most common 5-letter starting letter is S, and by a substantial amount.
* Vowels are the most common 2nd letter, followed by r