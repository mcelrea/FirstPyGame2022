# Programming Notes

## Principles of Programming

Ideas and concepts to help you succeed in programming

- Always keep your program in a working state ***AT ALL TIMES***
- Attempt to code small additions. Don't implement too much detail or functionality
- Each idea/addition should be implemented in its own function definition
- Name functions and variables meaningfully
- If something breaks......***STOP***. Seek help, or begin to debug
- It is okay not to know how to do something! Look it up.
    - [PyGame Help](http://www.pygame.org/docs/ref/draw.html)
    - [Python Help](https://www.w3schools.com/python/)

## Create Task Requirements

- **A Purpose** - why did you write this application
- **A List** - a list and how it reduced complexity or how you could not write the app without out
- **A Function**
  - *Sequence* - code that runs over several lined in order
  - *Selection* - if statements
  - *Iteration* - looping
  - *Parameter* - input to the function
    - This input must change the result of the function

### Parameter

What is a parameter.

```python
def function(x, y):
   #code
```
x and y in the above function definition are parameters

### For looping through a list

Assume the following list

```python
bullets = []
#                x , y, size
bullets.append((100,100,5))
bullets.append((400,300,5))
bullets.append((340,560,5))
#assume more bullets
```

How do we loop through this bullet list?

```python
for currentBullet in bullets:
    # code to process each bullet goes here
    # each bullet will be stored in variable currentBullet
```

In general, it look like

```python
for temporaryVariable in listName:
    # code to process each item as stored in temporaryVariable
```

Things we may for-loop throug a list for:

- draw all the things in the list
- check every thing in the list for collisions
- Choose something from the list based upon some criteria
  - choose a hard question for a quiz game
  - take a look at all player one's bullets
- See if something is true about the list
  - In Wordle, check the word against every letter to see if its correct

