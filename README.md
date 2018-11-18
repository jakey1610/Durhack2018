# Durhack2018
Hack for Durhack 2018:

Our project took on the issue of the convoluted, yet monolithic, TPP dataset: we aimed to abstract key data and visualise it in a clear, streamlined fashion, for a doctor's use. Thus, a doctor could seamlessly view a patient's past medical history, simply through searching for the patient's name. The data has also been categorised depending on the way the statistic was found: for example, through an observation or encounter. Several analysis features have also been implemented: calcium, cholesterol and sodium levels are compared with the masses (in the case, the dataset given) and if they fall lower than second percentile, or higher than the ninety-eighth, it is flagged upon doctor's viewing. There is additionally a separate page which illustrates this graphically, regardless of where one falls in the data. Overall, we hoped to have streamlined the interface between a doctor and his patient's past, whilst illuminating any issues, or potential ones, as well.


Inside folder "Durhack" is a python web application requiring dependencies:

-flask 

-matplotlib 

-numpy

Running instructions:

Create a new folder "patients" inside the "durhack" directory.

Add a dataset of .json files in the FHIR format inside patients (link: https://files.slack.com/files-pri/T942CKUM6-FE683EX8S/download/fhir.7z)

run server.py


If we had more time, we would have considered deploying our application using a service such as AWS or Google Cloud
