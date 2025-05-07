<h1>Fetch Weather Data From <a href="https://openweathermap.org/">OpenWeatherMapAPI</a> and Automate it to Run Daily With Github Actions</h1>

<h2>Description</h2>
This project automates the process of collecting 5-day weather forecasts in London, schedule the script to run at 6am UTC every day, and storing weather data into csv in github repository.
<br />

<h2>Languages and Utilities Used</h2>

- <b>python</b>
- <b>web scrapping</b>
- <b>requests</b>
- <b><a href="https://openweathermap.org/">openweathermapAPI</a></b>
- <b>ETL</b>
- <b>pandas</b>

<h2>How to obtain API Key:</h2>

<p align="center">
<br />
You have to sign in to <a href="https://openweathermap.org/">openweathermapAPI</a>, then navigate to My API Keys<br/>
<img src="https://i.imgur.com/WGDsGwV.jpeg" height="70%" width="70%" alt="MyAPIKeys"/>
<br />
<br />
Copy the API Key<br/>
<img src="https://i.imgur.com/b0ullLH.jpeg" height="70%" width="70%" alt="CopytheAPIKey"/>
<br />
<br />
Then paste the API KEY into repository secret in Settings > Secrets and Variables > Actions > Click on New Repository Secret<br/>
<br />
<br />

<h2>How to download the csv file, open Actions tabs and click on Fetch Weather Data</h2>

<p align="center">
<br/>Open Actions tabs and click on Fetch Weather Data<br/>
<br />
<img src="https://i.imgur.com/99Bub3b.png" height="80%" width="80%" alt="ActionsTabs">
<br />
<br />
Then, click the download symbol<br/>
<br />
<img src="https://i.imgur.com/udxoQ5N.png" height="80%" width="80%" alt="DownloadCSV">
<br />
<br />
Here is the Example of the output in csv format<br/>
<br />
<img src="https://i.imgur.com/GbXA5cD.png" height="50%" width="50%" alt="CSVOutput">
<br />


<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
