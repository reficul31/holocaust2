<h1><center>IECSE HOLOCAUST</center></h1>
<a href="https://codeclimate.com/github/adwalvekar/holocaust2"><img src="https://codeclimate.com/github/adwalvekar/holocaust2/badges/gpa.svg" /></a>
<a href="https://codeclimate.com/github/adwalvekar/holocaust2"><img src="https://codeclimate.com/github/adwalvekar/holocaust2/badges/issue_count.svg" /></a>
<img src="https://travis-ci.org/adwalvekar/holocaust2.svg?branch=master" />

<br><h2>Usage</h2>
<br>This is the backend to the Node Webkit front end which is an offline data storage and UI for registrations. 
<br>The process is that the User first logs in with admin password to be able to make an event. The event
<br>consists of the following : Event Name (Post name is 'event'), Event passkey (Post name is 'password') and 
<br> Form structure (Post Name is 'form_data'). The backend currently processes the JSON data recieved in form of 'form_data'
<br> to make a new table with the required specificaitons. 
<Br> <Br>
When the user(non admin) wants to load the available events, it is required that the user enters the password of the event.
<br>On Successful verification of the password, the backend sends the JSON format of the table. The frontend renders the JSON.
<br>Now the user can record data according to the forms which is stored locally on the computer until the user hits the upload
<br> button to the server which prompts the user to enter the password. On successful verification, the recorded data is sent
<br>to the server in form of JSON. The backend deciphers this code and stores into the database.
<br>
<br>The Backend removes all special charecters and replaces spaces with under scores.
<br>
<br>
<h2>Form data format</h2>
Sample Form data :<br>
<pre>
<br>{
<br>	"form_data": [
<br>        {
<br>            "type": "textbox",
<br>            "label": "Registration Number"
<br>            "placeholder": "Nothing"
<br>        },
<br>        {
<br>            "type": "checkbox",
<br>            "label": "Programming languages you know?",
<br>            "values": "C++,Java,Python"
<br>        },
<br>        {
<br>            "type": "radiobutton",
<br>            "label": "Had Coffee?",
<br>            "values": "Yes,No"
<br>        },
<br>{
<br>            "type": "radiobutton",
<br>            "label": "Member?",
<br>            "values": "Yes,No"
<br>        }
<br>    ]
<br>}
</pre>

<h2>Status Codes</h2>
Status codes for everything is very simple. True if action output/status is true, else false. 
