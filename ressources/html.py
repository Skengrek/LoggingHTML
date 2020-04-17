"""
Contains the frame of the HTML documents
"""

STYLE = """
<style type="text/css">
    body, html {
        background: #000000;
        width: 1000px;
        font-family: Arial;
        font-size: 16px;
        color: #C0C0C0;
        }
    h1 {
        color : #FFFFFF;
        border-bottom : 1px dotted #888888;
        }
    pre {
        font-family : arial;
        margin : 0;
        }
    .box {
        border : 1px dotted #818286;
        padding : 5px;
        margin: 5px;
        width: 950px;
        background-color : #292929;
        }
    .error {
        color: #EE1100;
        }
    .warning {
        color: #FFCC00;
        }
    .info {
        color: #4059ff;
        }
    .debug {
        color: #CCA0A0;
        }
    .tabcontent {
        display: none;
    }
    /* Style the buttons that are used to open the tab content */
    .tab button {
        background-color: grey;
        border: none;
        outline: none;
        cursor: pointer;
        padding: 14px 16px;
        margin: none;
        transition: 0.3s;
    }
    
    /* Change background color of buttons on hover */
    .tab button:hover {
        background-color: #ddd;
    }
    
    /* Create an active/current tablink class */
    .tab button.active {
        background-color: #ccc;
    }
</style>
"""

# * The script part of the HTML.
# * ##########################################################################

# ? tab_switch: take care of the tabs selecting wich information the
# ? user wants to see
SCRIPT = """
// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();

function tab_switch(evt, type) {
    // script modified from a w3schools example 
    var i, tab_content, tablinks;
    
    // Declare all variables
    var i, tabcontent, tablinks;
    
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    
    if (type == "all") {
        type = "tabcontent"
    }
    
    // Show the current tab, and add an "active" class to the button that opened the tab
    elements = document.getElementsByClassName(type);
    for (i = 0; i < elements.length; i++) {
        elements[i].style.display = "block";
    }
    evt.currentTarget.className += " active";
}
"""

# * The core frame of the HTML file
# * ##########################################################################


START = f"""
    <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <title>%(title)s</title>
            {STYLE}
        </head>
    
        <body>
            <h1>%(title)s</h1>
            <h3>%(version)s</h3>
            <div class="tab">
                <button class="tablinks"id="defaultOpen" onclick="tab_switch(event, 'all')">all</button>
                <button class="tablinks" onclick="tab_switch(event, 'error')">Errors</button>
                <button class="tablinks" onclick="tab_switch(event, 'warning')">Warnings</button>
                <button class="tablinks" onclick="tab_switch(event, 'info')">information</button>
                <button class="tablinks" onclick="tab_switch(event, 'debug')">debug</button>
            </div>
            <div class="box">            
            
            <table>
            <tr>
                <th scope="row" width="100">Time</td>
                <td width="150"><pre>File and line</pre></td>
                <td><pre>message</pre></td>
            </tr>
    
"""

END = f"""
    </table>
    </div>
    <script>{SCRIPT}</script>
    </body>
</html>
"""


MSG = """

<tr class="tabcontent %(class)s">
        <th scope="row" width="100">%(time)s</td>
        <td width="150"><pre><span title="%(moduleMouseOver)s">%(origin)s (%(line)s)</span></pre></td>
        <td><pre>%(msg)s</pre></td>
</tr>

"""
