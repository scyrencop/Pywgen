# Description 


Pywgen is a word list generator in which you can specify a standard character set or a character set that you specify and It can generate all possible combinations and permutations.

This code can be easily adapted for use in brute-force attacks against network services or cryptography.

**DO NOT use this software on other systems without their permission. Only use it on your own system and for educational purposes.**


# Usage 

Use the command-line, after `-char` yoou specify placeholders for fixed character sets :  

- az : lower case alpha characters
- AZ : upper case alpha characters
- 09 : numeric characters

 and after -len specifies the length of the word 

**Example**

`python pywgen.py -char az09 -len 4`

this code will generate a file with lower case alphanumeric characters

![Example](https://cdn1.imggmi.com/uploads/2019/1/1/3697a8b0c2f4b44c381aa09b1956abf6-full.png)



# Todo

- [x] Generate wordlist alphanumeric
- [ ] Generate wordlist with special char
- [ ] Specify the order of the possible combinations
- [ ] Adds support to compress the generation output
- [ ] Encrypt the word to compare it
