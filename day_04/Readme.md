# Day 4

Today's advent challenge was all about the orginization of data and finding
needles in haystacks. My irresponsible dictionary use bit me after coming back
to the problem six hours later. This led to some thoughts on dictionaries:

Dictionaries come in multiple flavors for Python. Here is a list of what I've
encountered in my experience, but I am sure it's not exhaustive:
* Functional mappings where keys map to values through a function. Acting on
the dictionary is decoupled from it's creating in a nice way. I like to name
these after verbs, and the comment on line 61 does some heavy lifting.
* Configuration mappings similar to Flask's `app.config`. The key-value pairs
are contextually grouped because they all alter a configuration. An object could
provide the same function, but using a dictionary indicates the mapping is
consumed elsewhere.
* Panda's `DataFrame` offers dict access to it's column:series mapping.
* Big balls of state. Avoid these if possible. `sometimes['this']['seems']['ok']` but it's not. 

Today I walked a fine line between functional mappings and a big ball of state.
A good exercise would be to recreate the solution with `sqlite` to get nicely 
structured data. A class-based approach would be easier, but I'm sick of writing
objects at work and wouldn't mind the pain of an SQL engine for a little.