from taipy import Gui

# Define the path or URL to your .exe file
exe_file_url = "vsw11.exe"

# Define the GUI layout with centered content and a download button
gui = Gui()

download_page = f"""
<div style='text-align: center;'>
    <h1>My Project Name</h1>
    <p>An amazing project that does amazing things.</p>
    <h2>Download the Application</h2>
    <p>Click the button below to download the .exe file:</p>
    <a href='{exe_file_url}'><button>Download File</button></a>
</div>
"""

# Add the download page to the GUI
gui.add_page("download", download_page)

if __name__ == "__main__":
    gui.run()