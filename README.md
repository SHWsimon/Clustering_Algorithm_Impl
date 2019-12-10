# Clustering_Algorithm_Impl

1. lloyd.py : Lloyd’s k-means
2. kmeanspp.py : k-means++
	
	Arguments:
	><ul>
	><li>Input1: A data file. The data is a comma separated matrix of size n × m. Here the data points are the rows (not the columns) of the matrix.</li>
	><li>Input2: k, the number of desired clusters.</li>
	><li>Input3: r, the number of random iterations.</li>
	><li>Input4: output file.</li>
	>  <p>Ex: 
			Python3 keanspp.py inputdata k r output</p>
 	></ul>
	
	Output result:
	><ul>
	><li>Output1: A comma separated file containing n integer values. Each integer value is in the range 0 . . . k−1, specifying the cluster of the corresponding row.</li>
	><li>Output2: The quantization error</li>
 	></ul>

3. spectral.py : Spectral clustering
	
	Arguments:
	><ul>
	><li>Input1: A data file. Same as the data file of Part I.</li>
	><li>Input2: k, the number of desired clusters. Same as in Part I.</li>
	><li>Input3: σ, sigma</li>
	><li>Input4: output file.</li>
	>  <p>Ex:
			Python3 spectral.py inputdata k sigma outputclusters</p>
 	></ul>
	
	Output result:
	><ul>
	><li>Output1: A comma separated file containing n integer values. Each integer value is in the range 0 . . . k−1, specifying the cluster of the corresponding row.</li>
	><li>Output2: The quantization error</li>
 	></ul>

