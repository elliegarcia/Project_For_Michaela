dataFile = read.csv("Zip_MedianValuePerSqft_AllHomes.csv",header= TRUE);
#suppose u want col 1, col 9 and col 15 
col2 = 2;
col268 = 268;
zipfile = dataFile[,c(col2, col268)];
write.csv(zipfile, file = "median_values_test.csv", row.names=FALSE)
