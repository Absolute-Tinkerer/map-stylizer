# map-stylizer
GUI written in Python to parse OSM (OpenStreetMap) files and render them onscreen. Layers may be toggled on/off and drawing may be customized.
<hr>
<p>This program allows a user to render OSM files within the GUI. The GUI enables the user to easily modify which layers are visible and the style of these layers.</p>
<h1>Basic Demo Video</h1>
<a href="https://www.youtube.com/watch?v=0ZPQwr0leys"><img src="https://img.youtube.com/vi/0ZPQwr0leys/0.jpg"></a>
<h1>Steps</h1>
<ol>
  <li>Download the source code open the program by typing <code>python main.py</code> in the command line.</li>
  <li>Open your browser of choice to <a href="https://www.openstreetmap.org/">OpenStreetMap</a>.</li>
  <li>Click the "Export" tab and select the "Manually select a different area" link. Shape and place the box over the region from which you want map data. Click "Export" to download the OSM file for the box you've drawn. If you get an error that you've selected too many nodes, you may alternatively click "Overpass API."<br><b>Note:</b> Ensure your downloaded OSM file is around 30MB. Larger files will noticeably slow the program.</li>
  <li>Open your OSM file using the GUI.</li>
  <li>Edit away!</li>
</ol>
<h1>Editing</h1>
<ul>
  <li>Choose which layers you want visible<br><b>Note:</b> Layers are grouped by OSM keys (i.e., "highway," "waterway," etc.)</li>
  <li>Change the style of line or fill layers</li>
  <ul>
    <li>Line layers are QPen objects, so you can specify the line's width, color, style, cap style, and join style</li>
    <li>Fill layers are QColor objects, so you can only specify their color</li>
  </ul>
  <li>When you save an image, the resulting configuration is saved into the "configs" folder so you can reimport these settings for another project</li>
  <li>You can also automate the creation of configurations via your own script, where you use the Configuration class to set colors of layers en masse
</ul>
<h1>Adding Additional Layers</h1>
<p>When you import an OSM file and begin manipulating it, you will likely notice warnings on your command prompt indicating there are additional layers not rendering because they need to be added. This is okay, as I've added the majority of layers you would be interested in; however, if you would like to add the layers mentioned, follow the below steps:</p>
<ol>
  <li>In the constants.py file:</li>
  <ol>
    <li>Create a <u>unique</u> (both variable name and variable value) VAL variable under the appropriate KEY group</li>
    <li>Create a <u>unique</u> (both variable name and variable value) CONFIG_STYLE variable under the appropriate KEY group</li>
    <li>Connect the new VAL and new CONFIG_STYLE in the DATA_GROUPS dictionary</li>
  </ol>
  <li>Finally, in the configuration.py file, connect the CONFIG_STYLE to a QPen (for a layer to be rendered as a line) or QColor (for a layer to be rendered as a fill)</li>
</ol>



### Contributing

To edit the GUI, use `cd src/gui/MainWindow` and run `pyuic5 mainwindow.ui > MainWindowUI.py`. If your 
git commit shows the entire file changed, you have accidentally changed the line endings from CRLF mode, 
so please change them back. You should only see a few lines changed in the py file