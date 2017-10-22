To my beautiful God



ShutToPasswords
a social engineering on Passwords











Clara Lanza

What is ShutToPasswords?
I Analysis passwords leaked on the Internet and found millions of passwords. It’s very bad for users. But exist a worse case! If Intruder mining the password databases he/she can find golden result! How?
Let me to suppose the passwords leaked database as a human's language. Why humans language? Users (human) creators passwords and they choose a password by attention to behaviors(such “shutup” or ‘iloveshe’), environment (“moscow” or “highschool”), region (“muslim”,”buda”) and other human common properties!
 Now we speak about Pass language and it’s dependencies. If you attend Pass language is very young and not improved as well as English, Russian, Chines or Turkish. Each leaked database consist new words and update our language. Such each natural language, we can analysis Pass. If we can decide about w in Pass, we can improve our security. But we know any string by any length may be used as a password, but we know Pass language have a word distribution such others word. We use fuzzy methods to decide about w in pass.
When adversary do Brute-force attack on a cipher-text, we must check parity of E_k(ciphertext)  to find correct plain-text and related key. In this case (Pass language) we can use similar methods. We calculated some probabilities of Pass and will use them to earn degree of membership of an arbitrary string to Pass. Method we have chosen to calculate degree of membership is the letter frequency (by attention to speed of calculus and gain of letter frequency in usual language).

Some people may be used others method, such letter frequency by attention of positions, place of keyboards layout key, by Wikipedia word, local information's such local language, names and… (Hijri calendar is an important element when you attack on ISIS or FSA terrorists passwords, But if you want to attack to NATO terrorists you must attend to Georgian calendar). In below we plot mono, dual and triple letter frequency of passwords. In all figures, x-axis sorted by dictionary ordered on the ASCIIs that was shown in password databases.

For first result of above graphs we understand distribution of Pass words is not uniform, even not nearly to uniform! (as we excepted from a usual language), 
We must to note, we don’t use Markof chains distribution in our tools, owing to in a fixed n for passwords length, there is no significant difference between letter frequency and first characters frequency. But if you want to use Markof  we advise to use letter and first character frequency for n-char passwords.

Future
I’ll try to add multiThread as soon as I can in next release (If I have enough free time). In multiThreaded version, you can shut to passwords faster than current version.
If you want to know about my plan for first alpha version (ShutMyPassword v1.0) I get you this list:
1. MultiThreading by GPU (Graphic card) to import processing speed and earn the shortest time for dictionary generation.
2. Cracking hash or archive, without need to hard space
3. Split output files. It’s avoid to create large file to facilitate themes management.
4. Use quantum true random bit generator to generate a most strong password
However, I will only submit version 1, when I received 1.4BTC (nearly 4800$) in my wallet. 
How to?
	Gui
Inputs
The great box on the main window is a command box for define sets of chars. They will be used in the “input box”.
{setA}→{xyz} : Create 3 sequences of setA elements (chars) by length x and y and z. pay attention numbers in second {} is exactly 1 digit integer.

Example1:
If you enter below formula in input box
{setLower}→{2}+{setDigit}→{2}=4
then, output passwords generate by below properties:
1) Length of each output: 4
2) let a_0, a_1, a_2, a_3 is an output then:
	a_0 in setLower,  a_1 in setLower, a_2 in setDigit, a_3 in setDigit
example2:
If you enter below formula in input box
{setLower}→{13}+{setDigit}→{2}=4
then there is no ouput!

example2:
If you enter below formula in input box
{setLower}→{13}+{setDigit}→{2}=3
then, output passwords come from below properties:
1. Length of each output: 4
2. let a_0, a_1, a_2, a_3 is an output then:
	a_0 in setLower,  a_1 in setDigit, a_2 in setDigit
	or
	a_0 in setLower,  a_1 in setLower, a_2 in setLower

treshold
If I want to describe a good Pass language dictionary, I noted “each word has high chance to seen in real targets, it had seen word on dictionary!”. After this, first question is “ how I have calculated probability of words?”. I use letter frequency to answer it!
We use 3 versions of letter frequency
Using the mono letter frequency of Pass language: 
Pr_1(a_0 a_1 , … , a_n)=f_1(a_0 )*f_1(a_1 )*... f_1(a_n )
Using the double letter frequency of Pass language: 
Pr_2(a_0 a_1 , … , a_n)=f_2(a_0 a_1 )*... f_2(a_{n-1}a_n )
Using the triple letter frequency of Pass language: 
Pr_3(a_0 a_1 , … , a_n)=f_3(a_0 a_1 a_2)... f_3(a_{n-2}a_{n-1} a_n )
(Attention in each scenario, assumed all Pass-words have same length. Do not compare a 5 characteristic word by 8 characteristic! 
example:
password



“password”
5.930120500034659e-13, 
3.050243853094855e-20, 
1.763021569888539e-22
“12345678”
3.0952854678741692e-15, 
2.1491937361427716e-18, 
2.0203736325227483e-18
“football”
1.4903553669304546e-12, 
3.8431442929906875e-21, 
1.0706592803286283e-25
“qwerty”
1.957640790680022e-11, 
4.316585158734176e-17, 
4.1292005132803934e-20
“princess”
4.570080997595735e-12, 
3.5704632274553605e-19, 
9.6072986576993e-23
“passw0rd”
2.6800863149851517e-13,  
6.77816416990106e-24,
1.2578035599550942e-27
“sunshine”
4.67910344744717e-12,  
9.967219458085412e-20,
1.4255306897850103e-24

Note: for all i<j :Pr_i(pw) > Pr_j(pw)
Note: If you don't have enough hard space don't use Pr_1, since 
Pr_1 (a_0 a_1 ... a_n) = Pr_1 (a_sigma(0) a_sigma(1) ... a_igma(n))
for all sigma in S_n.
So output database size is in factorial order. (OH! My GOD!)
Note: for all  i<j: sizeOf(database_1) > sizeOf(database_2)
I believe that 4 letter frequency cannot be a good standard, (it’s may be mistake!)
database generating
In this case, program generate a good dictionary. Chance of seen of all of its word have at least 2**threshold! Use it to unlock yourself old archives that's you forget themes password.
Strong password
In this case, program generate a good dictionary. Chance of seen of all of its word have at most 2**threshold! Use it to provide of yourself security. But if you forget it, you cannot use previous section… in an unusual case, you must use strong passwords database :)
setNew
Before each calling databases generators, use passwordObj.setNew()
Module
Password class
Password structure form is a list of strings, that each element of password in related list elements. If a structure is [‘12’,’ab’,’cd’], then possible passwords set is {‘1ac’,’1ad’,’2ac’,2ad’,’1bc’,’1bd’,’2bd’,’2bc’]
password.structures is a list of common structures.
Password.initDatabase: Create “temp modules” that generator of your favorites password dictionary! Attend that if you use “module.initDatabase()” or “from temp import G” in yourself research for got passwords. Both of them use similar code and make similar dictionary without any of them is better than other!
Temp Module
After each time you called module.initDatabase, “temp.py” have will been changed. 
