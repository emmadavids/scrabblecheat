I made a programme to help users cheat at scrabble. I coded in Python as a command line programme by myself and my partner helped me convert it to a web application with Flask. HTML and CSS by me. There are better apps that do the exact same thing out there, but I learned a lot doing this project.
Initially I used for loops to go through every possible permutation of a user's input and compared each one to every word in the dictionary, which was woefully inefficient and caused the programme to crash when the user input more than 5 letters. I solved this by creating temporary arrays,
one which stored permutations beginning with a certain letter and one which stores dictionary words beginning with a certain letter and compared the two. It is still not particularly fast and it does not deal with blank tiles but as my first functional web app I am pleased. Dictionary from Mielestronk.