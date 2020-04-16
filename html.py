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
    .err {
        color: #EE1100;
        font-weight: bold
        }
    .warn {
        color: #FFCC00;
        font-weight: bold
        }
    .info {
        color: #4059ff;
        }
    .debug {
        color: #CCA0A0;
        }
</style>
"""

FRAME = f"""
    <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <title>%(title)s</title>
            {STYLE}
        </head>
    
        <body>
            <h1>%(title)s</h1>
            <h3>%(version)s</h3>
            <div class="box">
        <table>
            
"""

_END_OF_DOC_FMT = """
    </table>
    </div>
    </body>
</html>
"""

