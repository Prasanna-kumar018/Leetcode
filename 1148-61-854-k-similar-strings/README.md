<h2> 1148 61
854. K-Similar Strings</h2><hr><div><p>Strings <code>s1</code> and <code>s2</code> are <code>k</code><strong>-similar</strong> (for some non-negative integer <code>k</code>) if we can swap the positions of two letters in <code>s1</code> exactly <code>k</code> times so that the resulting string equals <code>s2</code>.</p>

<p>Given two anagrams <code>s1</code> and <code>s2</code>, return the smallest <code>k</code> for which <code>s1</code> and <code>s2</code> are <code>k</code><strong>-similar</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s1 = "ab", s2 = "ba"
<strong>Output:</strong> 1
<strong>Explanation:</strong> The two string are 1-similar because we can use one swap to change s1 to s2: "ab" --&gt; "ba".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s1 = "abc", s2 = "bca"
<strong>Output:</strong> 2
<strong>Explanation:</strong> The two strings are 2-similar because we can use two swaps to change s1 to s2: "abc" --&gt; "bac" --&gt; "bca".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s1.length &lt;= 20</code></li>
	<li><code>s2.length == s1.length</code></li>
	<li><code>s1</code> and <code>s2</code> contain only lowercase letters from the set <code>{'a', 'b', 'c', 'd', 'e', 'f'}</code>.</li>
	<li><code>s2</code> is an anagram of <code>s1</code>.</li>
</ul>
</div>