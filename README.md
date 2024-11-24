# PERSONAL-ASSISTANT
Overview
SAG 1.0 is an interactive Python-based personal assistant program designed to assist users with various day-to-day tasks. Its functionality spans from basic utility operations, such as opening calculators, to personal touches like sending occasion-specific messages. It integrates elements of interactivity, data visualization, and task automation.

**Features**
Personalized Greetings:

Detects the time of day and greets the user accordingly.
Identifies the user by their login credentials.
**Task Automation:**

Calculator: Perform basic arithmetic operations (+, -, *, /).
Alarm Setup: Allows users to set alarms with custom labels.
Play Music: Reads a playlist file (playlist.csv) and plays a selected song or adds new songs to the playlist.
Pen Down Notes: Craft occasion-specific notes (e.g., birthdays, festivals).
**File-Based Operations:
**
Opens and displays contents of:****
Phonebook: Reads contacts from phbook.csv.
Timetable: Reads and displays a timetable from TT.csv.
Shows air pollution levels or literacy rates using pre-supplied datasets.
Data Visualization:
**
**Plots literacy rates of Indian states****.
Visualizes air pollution metrics (AQI and PM2.5) for Indian states.
Requirements
Python 3.6 or later.

**Libraries:**
pandas for data handling.
numpy for numerical operations.
matplotlib for plotting and visualizations.
**CSV Files:**
playlist.csv: Music playlist.
phbook.csv: Phonebook with contact details.
TT.csv: Timetable details.
state air pollution.csv: Air pollution data for Indian states.

**Usage Instructions**
Run the script using any Python IDE or terminal.
Log in with credentials:
Username: shresth
Password: shresth@singh
After a successful login:
Respond to the prompt "HOW MAY I HELP YOU SIR:" with supported commands:
open calculator - For arithmetic operations.
pen down a note - To create custom occasion messages.
play music - Manage and play songs.
open my phonebook - Display saved contacts.
open timetable - Show daily timetable.
show air pollution level in India - Visualize air quality data.
set alarm - Schedule alarms.
literacy rate in states of India - View a bar chart of state-wise literacy rates.
Follow interactive prompts for each feature.

**File Structure**
Main Script: SAG 1.0.py
Data Files:
playlist.csv (Music Playlist)
phbook.csv (Phonebook)
TT.csv (Timetable)
state air pollution.csv (Pollution Data)
Limitations
Static login credentials. Future versions can include dynamic user authentication.
Limited music integration; no actual playback mechanism (e.g., linking to external players).
Dependency on pre-existing CSV files for functionality.
Future Enhancements
Add voice command integration.
Enable more robust music playback using APIs (e.g., Spotify).
Enhance data security with encrypted login credentials.
Broaden data visualization for more states and metrics.
Author
Developed by Shresth Singh.

Enjoy using SAG 1.0 to simplify your day! 😊
