# CS 175 
## Chess text-to-move mapping 

### Abstract 
Our goal is to turn a user's natural language input of a desired move to the corresponding move on python's chess library object. Our methodology is to use embeddings of statements describing the move generated in several different formats to match as close to the user input as possible. This architecure has much less cost and time compared to a much more advanced language model made to handle a much larger range of natural language than just similarity matching. 

### Files
#### lucas_testspace_with_tests.ipynb 
is the end-to-end pipeline run and its outputs are displayed without needing to be run to see performance of all embedding and SLM models bar SOTA LLM model which is run independently with results appended. 

#### demo_pipeline.ipynb 
is the minute long sample notebook that can be run to visualize the process with 3 sample test cases. 