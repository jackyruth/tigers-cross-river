# Background
This mini-project started as my attempt to connect with my grandparents.
They raised me by themselves from when I was 3 until I was 7, while my actual parents were away doing very valid things.

I immigrated to Canada when I was 8, and have since visited my grandparents every single year.
Except that I haven't visited them in the last 6 years, due to my busy academic studies and covid.

However, I found some time this year to visit them, and I wanted to reconnect with them after so much time away.
Unfortunately, I have forgotten nearly all of my Chinese, so I couldn't communicate what I have been up to.
I tried to show them some pictures, but age hasn't been kind to their eyes.

There is this riddle that my grandpa used to give me when I was a kid.
I remember that it captured my attention, and that I spent many hours working on it before eventually solving it.
Year after year, my grandpa would gave me the same riddle as I inevitably forget the answer (because the answer was quite long and involved).
Eventually, it sort of became our favourite riddle.

Back when I first solved the riddle, I felt very clever and satisfied.
But knowing what I know now, I was doing nothing more than manually running a brute-force algorithm.
I knew I could use the Breadth-first search algorithm to automate this process.

I thought that this was a good way to show the kind of things I've been interested in over the last few years.
And to shows it in a way that my grandparents can see and comprehend.
So without further ado, here is the riddle.

<Pic of me with my grandparents>

# Riddle
The River Crossing Riddle
=========================
There are three tigers and three cubs.
Each tiger is a parent to exactly one of the cubs.

The tigers and cubs are trying to cross a river.
There is a boat next to the shore capable of carrying at most two animals at a time.
All three tigers know how to row the boat, but only one of the cubs knows, the other two cubs can only be passengers.

The tigers are merciless and will eat any cub that is not with its parent.
For example, 'tiger A' will eat 'cub b' if 'tiger B' is on the other side of the river.

How does the entire group cross the river safely?

This riddle is certainly a variant of the river crossing riddle found on google, although the version I was given has waited until this moment to find itself on the internet.

# Solution
First, I frame this game in the riddle as a graph.

The nodes of the graph should uniquely encode the state of the game.
Not all nodes are 'valid' as some states are either infeasible or results in the cubs being eaten.
The edges of the graph should connect valid nodes to other valid nodes.

Once the graph has been estabilished, I used the Breadth-first search algorithm to find the shortest path between the starting state and the solution state.

That is pretty much all there is to it!
There are some caveats such as how to encode the node, and how to 'feel out' the graph during the search algorithm rather than before, but those are unimportant details.

I encourage you to try the riddle for yourself first, then use the following gif to check that you got the right answer!

<3t3c solution here>

# Simpler Variant
To further demonstrate my powers to my unsuspecting grandparents, I searched the space of all possible riddles to find different variants.
I wanted the variant I present to my grandparents to satisfy two conditions.

    1. A simpler version requiring less steps in the solution
    2. Still gave the same sense of cleverness and satisfaction once solved

The version I was given was too difficult, it involved running a brute-force algorithm by hand for 13 steps.
Indeed, in my whole family, only I was foolish enough to give up my time to find the solution, which seems predictive of the profession I am in now.

Now that I have nieces of my own, I wanted to give them an easier variant of the riddle, but one that still gave the sense of solving something tricky.
The tricky part was figuring out what seemed tricky about the riddle, and why it gave me the sense of being clever after having found the solution.

It can't feel like you are carrying out a mindless algorithm, like that for multiplying two long numbers, where is the fun in that?
After investigating further, I believe I found the culprit, and it has more to do with human psychology than actual difficulty (as we expect).