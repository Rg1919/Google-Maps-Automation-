# Google-Maps-Automation-
Welcome to the Travel Planner script, a comprehensive tool designed to streamline your travel planning experience. This script leverages the power of Selenium for web automation, enabling you to effortlessly retrieve travel details from Google Maps and seamlessly share them through ProtonMail.

Requirements
Before getting started, make sure you have the following components in place:

Python 3: Ensure you have Python 3 installed on your system. You can download it from Python Downloads.

Selenium Library: Install the necessary libraries using pip:

bash
Copy code
pip install selenium pyautogui
ChromeDriver: Download ChromeDriver from ChromeDriver Downloads. Extract the executable and add its location to your system PATH.

Installation
Clone the Repository: Clone or download this repository to your local machine.

bash
Copy code
git clone https://github.com/your_username/travel-planner.git
Navigate to the Directory: Change your working directory to the project folder.

bash
Copy code
cd travel-planner
Install Dependencies: Install the required Python libraries.

bash
Copy code
pip install -r requirements.txt
Usage
Run the Script: Execute the script in your terminal or preferred Python environment.

bash
Copy code
python travel_planner.py
Follow the On-Screen Prompts: Enter your destination, location, and decide whether you want to send the travel details.

Sending Travel Details: If you opt to send the details, provide your ProtonMail login credentials and the recipient's email address.

Automated Process: The script will automatically navigate through Google Maps, retrieve detailed travel information, compose an email with the extracted details, and attach a screenshot.

Important Notes
Internet Connection: Ensure a stable internet connection for the script to function correctly.

Google Maps and ProtonMail Accounts: The script relies on Google Maps and ProtonMail. Ensure you have valid accounts for both services.

ProtonMail Attachment: The script utilizes PyAutoGUI for automated file attachment in ProtonMail. Please refrain from interacting with your ProtonMail interface during the script execution.

Enjoy a seamless travel planning experience with the Travel Planner!





