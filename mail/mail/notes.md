## TODO (commit points):

### Must remain single page application - all changes must be made in inbox.js

### ~~Send Mail:~~
~~- using the POST /emails route~~ 
~~- send the composed mail (if all fields are valid)~~
~~- redirect to sent mailbox~~

~~### 3 Mailboxes:~~
~~- using GET /emails/<str:mailbox> display all mail from given mailbox~~
~~- each email displayed in its own clickable <div> with border with~~
~~    - Sender, Subject, Timestamp~~
~~    - unread email - white background~~
~~    - read email - grey background~~


~~### View Emails:~~
~~- using GET /emails/<int:email_id> display email user has clicked on~~
~~- display as a popup, add another div and be sure to show/hide it within the other fucntions~~
~~- display:~~
~~    - Sender, Recipents, Subject, Timestamp, Body~~
~~    - a opened email should now be "read"
~~    - x in corner of popup to close and go back~~

~~    - Archive:~~
~~        - using PUT /emails/<int:email_id> allow user to toggle archvied status~~
~~        - once toggled redirect to inbox~~
        
~~    - Reply:~~
~~        - "reply" button that redirects to compose and prefills~~
~~            - recipent = sender~~
~~            - subject = RE: {subject}~~
~~            - body = "On {timestamp} {sender} wrote: {body}~~