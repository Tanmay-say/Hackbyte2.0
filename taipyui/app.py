
from taipy import Gui

# Define the path or URL to your .exe file
exe_file_url = "vsw11.exe"

# Define the GUI layout with a login button, centered content, and a download button
gui = Gui()

download_page = f"""
<div style='text-align: center;'>
    <div style='text-align: right; padding: 10px;'>
        <button onclick="alert('Login functionality not implemented yet.');">Login</button>
    </div>
    <h1>My Project Name</h1>
    <h3><p>"Revolutionize Your Racing: Navigate the Tracks with the Wave of a Hand.</p>
    <p> Experience unparalleled control and immersion without the confines of traditional gaming peripherals.</p>
     <p> Your gateway to the future of interactive gaming starts with a gesture."</p></h3>
    <h2>Download the Application</h2>
    <p>Click the button below to download the .exe file:</p>
    <a href='{exe_file_url}'><button>Download File</button></a>
</div>
"""

# Add the download page to the GUI
gui.add_page("download", download_page)

if __name__ == "__main__":
    gui.run()