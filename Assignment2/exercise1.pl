competitor(sumsum, appy).
developed(sumsum, galactica_s3).
stolen(stevey, galactica_s3).
boss(stevey, appy).

unethical(X) :- boss(X, Company), 
                competitor(Competitor, Company), 
                developed(Competitor, Technology), 
                stolen(X, Technology).
