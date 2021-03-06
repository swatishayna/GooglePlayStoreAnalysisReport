import streamlit.components.v1 as components
import streamlit as st
from app_logger.logger import applogger
import os

filename = os.path.basename(__file__)

def display_tableauReport():
    
    file_object = open("logs/operations.txt", 'a+')
    logger_object = applogger()
    logger_object.log(file_object, f'Current Script: {filename}')
    logger_object.log(file_object, 'Entered tableau dashboard')

    st.title("Google Play Store Analytics\n\n")
    html_temp = """
        <div class='tableauPlaceholder' id='viz1633065126909' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;GP&#47;GPSAnalysis_16312886435150&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='GPSAnalysis_16312886435150&#47;Dashboard1' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;GP&#47;GPSAnalysis_16312886435150&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1633065126909');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='1545px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='910px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='1545px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='910px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.minHeight='2150px';vizElement.style.maxHeight=(divElement.offsetWidth*1.77)+'px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(html_temp, width= 1550,height = 2000)
        # components.iframe("https://public.tableau.com/views/GPSAnalysis_16312886435150/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link")
