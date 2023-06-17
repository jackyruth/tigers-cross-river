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

<img src="/home/jacky/Downloads/franklin/grandpa-riddle/3t3c.gif" style="zoom:70%;" />

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

Take a look at Step 8 in the solution.

<img src="/home/jacky/Downloads/franklin/grandpa-riddle/3t3c-barrier.png" style="zoom:70%;" />

If you squint a little, the state of the game at step 8 looks like a state you can reach immediately in the first step.
Manually running the search algorithm is difficult because you have to keep track of all the states you've visited so you don't visit them again.
This requires solid bookkeeping, which we humans tend to disregard in our attempt to solve the problem quickly in order to look clever.

One of the first thing we do in our tendency to disregard proper bookkeeping is to stop tracking the location of the boat.
Maybe we see the boat as less of a prominent figure than the tigers/cubs or we think in our arrogrance that we'll remember which shore the boat is on, but the location of the boat is the first thing we mess up.

When the location of the boat is even slightly questioned, it throws up a psychological barrier once we hit step 8.
Either we don't recognize the state at step 8 being an uniquely new state, or just thrown enough doubt that we lose confidence in the accuracy of our bookkeeping records, both will hinder our progress to the solution.

This is the main barrier in the riddle.
In fact, once we confidently progress in our search after step 8, the solution becomes almost immediately evident.

When looking for a variant of the riddle, it must hit the same psychological barrier in order to give us the satisfaction we crave having found the solution.
I believe I found the simpler variant of the riddle I have been looking for.

The River Crossing Riddle (Simpler Variant)
=========================
There are three tigers and two cubs.
Each tiger is a parent to exactly one of the cubs, leaving the last cub without a parent.

The tigers and cubs are trying to cross a river.
There is a boat next to the shore capable of carrying at most two animals at a time.
Only the tigers know how to row the boat, the cubs can only be passengers.

The tigers are merciless and will eat any cub that is not with its parent.
For example, 'tiger A' will eat 'cub b' if 'tiger B' is on the other side of the river.

How does the entire group cross the river safely?

The solution to this simpler variant involves 7 steps as opposed to the 13 steps required in the original version.

<img src="/home/jacky/Downloads/franklin/grandpa-riddle/3t2c.gif" style="zoom:70%;" />

The psychological barrier arises in step 4, and I can confirm that it is indeed a barrier as my grandpa just couldn't get past it.

<img src="/home/jacky/Downloads/franklin/grandpa-riddle/3t2c-barrier.png" style="zoom:70%;" />