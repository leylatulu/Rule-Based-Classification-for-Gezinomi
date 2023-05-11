<h1 align="center">Rule Based Classification for Gezinomi</h1> 


<details>
<summary><h2 align="left">Business Problem</h2></summary>
Gezinomi company wants to create level-based new customer definitions (persona) using some features of its customers, and to create segments according to these new customer definitions and to estimate how much the new customers can earn on average according to these segments.
</details>


<details>
<summary><h2 align="left">Data Set Story</h2></summary>
The data set includes the prices of the sales made by Gezinomi company and information about these sales. This data set is hidden.<br>

The data set consists of records created in each sales transaction. This means that the _table is not deduplicated_. In other words, a user with certain demographic characteristics **may have made more than one purchase**.
</details>


<details>
<summary><h2 align="left">Description of Features</h2></summary>

|**FEATURE**| **DESCRIPTION** |
| --- | --- | 
|SaleID|Sale ID| 
|SaleDate|Sale Date|
|CheckInDate|Customer's check-in date|
|Price|Price paid for sale|
|ConceptName|Hotel concept information|
|SaleCityName|City information of the hotel|
|CInDay|Customer's check-in day|
|SaleCheckInDayDiff|Day difference between check-in and check-in date|
|Seasons|Season information on the check-in date|
</details>