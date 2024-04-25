# Python-Office-Hours-Queue
Program simulating an office hours queue


The first thing we did was look at the printer queue simulation in the textbook for inspiration. 
Next, we implemented a similar queue, changing certain aspects of the code to more accurately portray an office hours.
We also implemented a counter to give every student who came to office hours a unique position within the queue.
To accurately simulate an office hours block, we assumed students would ask 1-10 questions, and the TA would answer
1 question per minute. We also assumed a new student would arrive on average once every 5 minutes.
When testing the results of our queue, we originally found issues with students not being counted correctly, and unrealistic
question and answer time. After this, we made the appropriate changes detailed above and it resulted in a more realistic output.
