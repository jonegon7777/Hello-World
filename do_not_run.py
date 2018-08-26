from os import system
from random import randint
# Globals
next_step1 = \
'''Good job so now you see why you need the system("pause"). Or you are reading
this in do_not_run.py file in which case there's your hint.

So now from do_not_run.py import next_step2 and print it out to, you know like,
continue, or whatever. IDK it's your life'''

next_step2 = \
'''Okay so you've proven you understand sequence (commands execute in order and
not all at once or something else). Now let's move on to something more confusing.
Now you're going to call a function. I've already done this actually (see
print() and system() ) but now you're going to run a function with nothing
between those parentheses (you call them arguments btw).
So
from do_not_run import next_step3
then run it with
next_step3()'''

my_roll = randint(1,6)

def main():
    print("I said don't run me! and don't open me up in notepad++ either. My complexity will confuse your simple mind.")
    system("pause")

def next_step3():
    print("Running next_step3...beep, boop")
    system("pause")
    print("All next_step* after this will be functions you run.")
    print("After you're done with one import the next")
    print("They will always run system('pause') after completing")
    system("pause")

if __name__ == "__main__":
    main()