# Clustering_Algorithm_Impl

1. lloyd.py : Lloyd’s k-means
2. kmeanspp.py : k-means++
	><ul>
	  ><li>Client-side</li>
	  >  <p>JavaScript/CSS/HTML/EJS</p>
	  ><li>Server-side</li>
	  >  <p>Node.js</p>
	  ><li>Database</li>
	  >  <p>MongoDB</p>
	  ><li>IDE</li>
	  >  <p>Cloud9</p>
	  ></ul>
	>Arguments:
	>>• Input1: A data file. The data is a comma separated matrix of size n × m. Here the data points are the rows (not the columns) of the matrix.
	>• Input2: k, the number of desired clusters.
	>• Input3: r, the number of random iterations.
	>• Input4: output file
	>Ex: 
	>	Python3 keanspp.py inputdata k r output

	>Output result:
	>• Output1: A comma separated file containing n integer values. Each integer value is in the range 0 . . . k−1, specifying the cluster of the corresponding row.
	>• Output2: The quantization error	

3. spectral.py : Spectral clustering
	Arguments:
	• Input1: A data file. Same as the data file of Part I.
	• Input2: k, the number of desired clusters. Same as in Part I.
	• Input3: σ, sigma
	• Input4: output file
	Ex:
		Python3 spectral.py inputdata k sigma outputclusters

	Output result:
		• Output1: A comma separated file containing n integer values. Each integer value is in the range 0 . . . k−1, specifying the cluster of the corresponding row.
		• Output2: The quantization error	
	
