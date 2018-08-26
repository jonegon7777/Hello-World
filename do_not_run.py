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
not all at once or something else). Do let's move on to something more confusing.
So I'm gonna give you a random number (1-6) in do_not_run.my_roll. Print out that
variable.'''

my_roll = [randint(1,6), "So I lied"]

def main():
    print("I said don't run me! and don't open me up in notepad++ either. My complexity will confuse your simple mind.")
    system("pause")

if __name__ == "__main__":
    main()