# Text-Summarization

<h3>PURPOSE</h3>
<p>
A conventional AI algorithm for summarizing large texts into a short readable format without the use of any external/inbuilt libraries.
</p>

<h3>ALGORITHM</h3>
<p>
<ol>
<li>1. Word vectors weight assignments is used to determine the priority orders indexing.</li>
<li>2. Two step Stem cells pruning is done to restrict insignificant nodes from contributing to weight sums.</li>
<li>3. Heap based sorting to form coherence.</li>
</ol>
</p>

<h3>FRAMEWORK</h3>
<p>
No external libraries were used for the implementation.
We make use of the heap data structure (for soring word vectors).
</p>

<h3>HOW TO RUN<h3>
<p>
Select the text file you we to summarize.
Set file path to input text file.
Run python script to generate summary.
</p>

<i>Summary length is maitained as standard length (1/3)rd of total length.</i>
