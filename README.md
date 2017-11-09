# Text-Summarization

<h3>PURPOSE</h3>
<p>
A conventional AI algorithm for summarizing large texts into a short readable format without the use of any external/inbuilt libraries.
</p>

<h3>ALGORITHM</h3>
<p>
<ol>
<li> Word vectors weight assignments is used to determine the priority orders indexing.</li>
<li> Two step Stem cells pruning is done to restrict insignificant nodes from contributing to weight sums.</li>
<li> Heap based sorting to form coherence.</li>
</ol>
</p>

<h3>FRAMEWORKS</h3>
<p>
No external libraries were used for the implementation.
We make use of the heap data structure (for sorting word vectors).
</p>

<h3>HOW TO RUN</h3>
<p>
<ol>
<li>Select the text file you wish to summarize.</li>
<li>Set file path to input text file.</li>
<li>Run python script to generate summary.</li>
</ol>
</p>

<i>Summary length is maitained as standard length (1/3)rd of total length.</i>
