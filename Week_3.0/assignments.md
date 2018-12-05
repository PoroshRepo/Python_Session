
<html>
<head>
  <meta charset="utf-8">
</head>
<body>
<h2>Assignment 3.0</h2>
Welcome to the third assignment. From now on, there won't be any rule or restriction to design your solutions. We have just one very easy solution to design this week. 

<h3> Evaluating homogeneity of clustering: </h3>
There are many traditional ways of evaluating a clustering scenario. Today we are going to solve this using a different approach. Before you proceed, please find <b>Two_Patterns_TEST.csv</b> file under <b> Week_3.0/Session_02/K-Means </b> section. You have to apply KMeans clustering algorithm on this dataset. The following intuitions are very important to be followed -

<li>The first column (index 0) of the dataset is label column. Do not include this column in the clustering computation.</li>
<li>The label column is used as ground truth. (e.g. Two samples having same labels should be in the same cluster ;) )</li>
<li>Once clustering is done, use the label column to find out which label is dominating a particular cluster. (A cluster might have maximum number of samples that belong to label 2.)</li>
<li>The homogeneity of that cluster can be computed like this, <b>homogeneity = frequency of dominant label / total number of members</b></li>
<li>Find homogeneity for all the clusters.</li>

<h4> Parameters: </h4>
Try with following k values - 3,4,5,6,8,10,12,15

<h4> Deliverables: </h4>
<li>For each K, average all the homogeneity and store them in a list. Submit a <b>K vs Average Homogeneity</b> graph. </li>
<li>For each K, find out the SSE (Sum of square error) and store them in a list. Submit a <b>K vs SSE</b> graph. </li>

<h4>Deadline: </h4> 11:59 pm, Monday
<h4>Submission: </h4> 
You have to submit your solutions through your personal repository, otherwise your solution won't be considered. The deadline 
won't be extended as well. So, technically submitting your solutions even at 12:00 am, Tuesday won't help.
