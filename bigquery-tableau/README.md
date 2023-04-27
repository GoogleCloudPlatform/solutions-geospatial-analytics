<!-- Output copied to clipboard! -->

<!-----

You have some errors, warnings, or alerts. If you are using reckless mode, turn it off to see inline alerts.
* ERRORs: 0
* WARNINGs: 0
* ALERTS: 18

Conversion time: 5.255 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β34
* Thu Apr 27 2023 09:16:33 GMT-0700 (PDT)
* Source doc: Using BigQuery Spatial Data in Tableau through WMS server
* Tables are currently converted to HTML tables.
* This document has images: check for >>>>>  gd2md-html alert:  inline image link in generated source and store images to your server. NOTE: Images in exported zip file from Google Docs may not appear in  the same order as they do in your doc. Please check the images!

----->


<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 0; ALERTS: 18.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>
<a href="#gdcalert2">alert2</a>
<a href="#gdcalert3">alert3</a>
<a href="#gdcalert4">alert4</a>
<a href="#gdcalert5">alert5</a>
<a href="#gdcalert6">alert6</a>
<a href="#gdcalert7">alert7</a>
<a href="#gdcalert8">alert8</a>
<a href="#gdcalert9">alert9</a>
<a href="#gdcalert10">alert10</a>
<a href="#gdcalert11">alert11</a>
<a href="#gdcalert12">alert12</a>
<a href="#gdcalert13">alert13</a>
<a href="#gdcalert14">alert14</a>
<a href="#gdcalert15">alert15</a>
<a href="#gdcalert16">alert16</a>
<a href="#gdcalert17">alert17</a>
<a href="#gdcalert18">alert18</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>



[TOC]



### 


### 1. Summary

Using Web Map Service (WMS) in Tableau is a powerful way to add geospatial data to your visualizations. In this document, we will provide an introduction to WMS and how it can be used in Tableau. The target audience for this document is Tableau users who want to incorporate geographic data into their visualizations. By the end of this document, readers can expect to learn how to connect to WMS servers, how to use WMS layers in Tableau, and how to customize WMS layers to suit their needs. Whether you are new to WMS or have some experience with it, this document will provide you with the knowledge and skills needed to incorporate WMS into your Tableau workflow effectively.

The [Tableau BigQuery connection](https://help.tableau.com/current/pro/desktop/en-us/examples_googlebigquery.htm) only supports tabular attributes from BigQuery, and geometry fields can not be displayed in Tableau. (If the query contains Latitude or Longitude numeric fields, both fields can be recognized by Tableau Map and display the 

coordinates accordingly). Fully BigQuery geospatial support from Tableau Map is not supported.  


```
Any googler can request a tableau license at go/stuff. 
```


Tableau[ supports WMS](https://help.tableau.com/current/pro/desktop/en-us/maps_mapsources_wms.htm) as a background map, we can use a GeoServer to pass through WMS requests for Tableau. 



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")


Draft [here](https://drawio-internal.googleplex.com/#G1BUgikkdCEN6kZ9FfC3P_3Ditv3cZt18s).


### 2. GeoServer Web Map Services (WMS)  

WMS is an open standard defined by the [Open Geospatial Consortium](https://www.ogc.org/) (OGC). 

Web Map Service (WMS) is a standard protocol for serving georeferenced map images over the internet. It is a widely used standard for accessing and sharing maps and related geographic data over the web. WMS provides a way to access and display geographic data in a variety of client applications, including web browsers, desktop GIS software, and mobile devices.

In a WMS service, map images are generated on the fly by the server in response to user requests. The client application sends a request to the WMS server for a specific map image, specifying the area of interest, the desired size and format of the image, and any other options such as the desired layers or styling. The server responds with the requested image in the specified format, which can be displayed in the client application.

Check out this [link](https://mapserver.org/ogc/wms_server.html) for a list of WMS commands and sample requests and responses. 


### 3. Use WMS server in Tableau


#### 3.1 Connect to a WMS server 



1. In Tableau Desktop, select Map > Background Maps >WMS Servers.

    

<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.png "image_tooltip")


2. In the Add WMS Servers dialog box, type the URL for the server you want to connect to in Tableau, and then click OK.



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.png "image_tooltip")


Select "Use tiled maps" option, Tableau will request tiles from the server in the appropriate format, rather than downloading and rendering the entire map image at once. This can improve the speed and efficiency of the map visualization in Tableau.


```
Not checking this option could dramatically slow the client side map tile rendering. 
```


Add WMS server URL [https://geoserver1-admin-nbfmgtngza-uc.a.run.app/geoserver/cite/wms](https://geoserver1-admin-nbfmgtngza-uc.a.run.app/geoserver/cite/wms%60).

You can add as many map servers as you want to a workbook. Each WMS server you add appears as a background map in the Background Maps menu.



<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image4.png "image_tooltip")



#### 3.2 Use a WMS background map

After you connect to a WMS server, you can create a map view using the WMS background map that Tableau creates.



1. In Tableau Desktop, select Map > Background Maps, and then select a WMS background map to use in the view. \


<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image5.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image5.png "image_tooltip")

2. Add a datasource. In this example, we use the builtin sample data of sample-superstores. 

    

<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image6.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image6.png "image_tooltip")


3. Add geographic fields to the view by dragging the city field to the marks. 

      \


<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image7.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image7.png "image_tooltip")



	

	



4. Select Map > Map Layers, and then select the map layers you want to show in the view. \


<p id="gdcalert8" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image8.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert9">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image8.png "image_tooltip")

5. Map layer shown. You can enable the map controls to zoom in and out, pan maps etc. 

    

<p id="gdcalert9" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image9.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert10">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image9.png "image_tooltip")



    ```
Please note that Tableau Desktop maps use the EPSG 3857 (Web Mercator) projection while WMS servers use the EPSG 4326 or EPSG 4269 projections. The EPSG 4326 projections may look distorted, particularly at northern latitudes.
```




#### 3.3 Settings in Tableau for Maps


###### Map Layer Background Washout

Map Layer Background Washout reduces the opacity or saturation of the background of a map layer to allow the underlying data to stand out more prominently. It can be particularly useful when working with map data that has a lot of detail or complexity, and you want to highlight specific data points or patterns.

To apply a Map Layer Background Washout in Tableau, Select ‘Map’ menu, then ‘Map Layers’



<p id="gdcalert10" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image10.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert11">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image10.png "image_tooltip")


You can then adjust the Washout percentage setting. 100% being transparent. 



<p id="gdcalert11" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image11.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert12">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image11.png "image_tooltip")


The following images are Washout at 50% and 0. 


<table>
  <tr>
   <td>

<p id="gdcalert12" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image12.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert13">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


<img src="images/image12.png" width="" alt="alt_text" title="image_tooltip">

   </td>
   <td>

<p id="gdcalert13" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image13.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert14">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


<img src="images/image13.png" width="" alt="alt_text" title="image_tooltip">

   </td>
  </tr>
</table>



###### Map Options

You can set some map controls tools visibility including show map scale using the Map Options Menu. Available options shown in the following image. 



<p id="gdcalert14" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image14.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert15">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image14.png "image_tooltip")



#### 3.4 Common error messages



1. Error message: The map cannot be drawn because there was an error retrieving map tiles. 

    Solution: Select “Map” then “Map Layers”, check the right map layer. 

2. Error message: One or more of the map images from the server were blank. 

    Solution: Data from the WMS server does not match the data within the view. Make sure the data in the view corresponds to the map data, usually by pan/zoom to an area that matches with the WMS server map data. 



#### 3.5 Save a WMS server as a Tableau map source

After you add a WMS server to your workbook, it is saved with the workbook and available to anyone you share the workbook with. You can also save a WMS server as a Tableau Map Source (.tms) file, which you can share with others so they can quickly connect to it and use it in their own workbooks.



1. Select Map > Background Maps > Map Services. This opens the Map Services dialog.
2. Select the map you want to save as a Tableau map source, and click Export. This opens the Export Connection dialog.
3. Type a file name, choose a location, and click Save.


#### 3.6 Common problems with WMS 

Some common problems when using WMS include:



* Slow loading times. The content, speed, and performance of a WMS server depends on the network and WMS provider. 
* Limited data availability. 
* Difficulty in customizing the maps to fit specific needs. 
* Lack of offline access. 


### 4. Serving BigQuery Spatial Data with GeoServer

GeoServer is a widely-used open-source web map service known for its performance, scalability, and ability to handle large amounts of data and high traffic loads. It supports various spatial data formats and protocols such as WMS, WFS, and WCS. However, serving BigQuery Spatial Data with GeoServer was not straightforward until the release of bigquery-geotools.

Geoserver can run in a tomcat servlet container on [Cloud Run](https://cloud.google.com/run), using [Filestore](https://cloud.google.com/filestore) as a shared configuration directory and shared geowebcache blob store location. Please see the [readme file](https://github.com/GoogleCloudPlatform/solutions-geospatial-analytics/blob/main/geoserver-run/README.md) for detailed instructions. 

Bigquery-geotools now enables users to connect and serve BigQuery spatial data, including polygons and polylines, as a layer in GeoServer. To set up [bigquery-geotools](https://github.com/GoogleCloudPlatform/bigquery-geotools) and start using it with GeoServer, refer to the readme file for detailed instructions.


#### 4.1 GeoServer Settings for Performance

The following GeoServer settings can impact tile serving performance and improve overall performance:



* GeoWebCache Caching Setting: Enable caching to reduce server requests and improve response times for frequently-requested data. GeoServer uses GeoWebCache for integrated tile caching, increasing server responsiveness and reliability. Configure disk quotas for caching settings to monitor disk usage.
* Use image formats with lower file sizes: Choose image formats like PNG8 or JPEG for raster data to decrease file size and reduce the time it takes to transmit the data over the network.
* Optimize database performance: If your GeoServer is connected to a database, ensure that the database is correctly optimized, with appropriate indexes and spatial indexes in place for efficient querying.
* Adjust JVM settings: Tune the Java Virtual Machine (JVM) settings, such as heap size and garbage collection options, to improve the performance of the GeoServer instance.
* Use hardware acceleration: If your server hardware supports it, enable hardware acceleration for rendering, which can significantly improve map rendering performance.
* Configure connection pooling: Optimize the number of concurrent connections to the data source by configuring connection pooling settings in the data store configuration.
* Enable HTTP compression: Enable HTTP compression (e.g., gzip) to reduce the amount of data transferred over the network, which can improve response times for clients with slower connections.
* Use multi-threading and parallel processing: Configure GeoServer to take advantage of multi-core processors and parallel processing to improve map rendering and data processing performance.
* By optimizing these GeoServer settings, you can achieve better tile serving performance and overall server efficiency. Keep in mind that balancing cache performance and resource usage is essential for optimizing your GeoServer's performance.
1. Hardware: Upgrading hardware, such as increasing the amount of RAM or using a faster CPU can help to improve performance. For cloud run architecture and optimization, please reference this guide [here](https://github.com/GoogleCloudPlatform/solutions-geospatial-analytics/blob/main/geoserver-run/README.md)..


#### 





[https://geoserver1-admin-nbfmgtngza-uc.a.run.app/geoserver/web/?0](https://geoserver1-admin-nbfmgtngza-uc.a.run.app/geoserver/web/?0)

admin / geoserver

[https://pantheon.corp.google.com/run/detail/us-central1/geoserver1/logs?project=bigquery-geotools](https://pantheon.corp.google.com/run/detail/us-central1/geoserver1/logs?project=bigquery-geotools)

“just had a call with customer TGS, they said the ability to connect geoserver with BQ is "a dream come true".    so i think we might be on the right track here 

<p id="gdcalert15" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image15.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert16">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image15.png "image_tooltip")
”

Error when try to uncheck “enable disk quota”



<p id="gdcalert16" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image16.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert17">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image16.png "image_tooltip")




<p id="gdcalert17" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image17.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert18">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image17.png "image_tooltip")




<p id="gdcalert18" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image18.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert19">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image18.png "image_tooltip")


