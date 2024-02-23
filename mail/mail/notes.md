## TODO (commit points):

### Must remain single page application - all changes must be made in inbox.js

### ~~Send Mail:~~
~~- using the POST /emails route~~ 
~~- send the composed mail (if all fields are valid)~~
~~- redirect to sent mailbox~~

### 3 Mailboxes:
~~- using GET /emails/<str:mailbox> display all mail from given mailbox~~
~~- each email displayed in its own clickable <div> with border with~~
~~    - Sender, Subject, Timestamp~~
~~    - unread email - white background~~
~~    - read email - grey background~~


### View Emails:
- using GET /emails/<int:email_id> display email user has clicked on
- display as a popup, add another div and be sure to show/hide it within the other fucntions
- display:
    - Sender, Recipents, Subject, Timestamp, Body
    - a opened email should now be "read"
    - x in corner of popup to close and go back

    - Archive:
        - using PUT /emails/<int:email_id> allow user to toggle archvied status
        - once toggled redirect to inbox
        
    - Reply:
        - "reply" button that redirects to compose and prefills
            - recipent = sender
            - subject = RE: {subject}
            - body = "On {timestamp} {sender} wrote: {body}


### Styling
- Fix form field styling (remove bootstrap)
- Fix color pallete, stop with the shit darkmode grey
    Primary: White
    Secondary: Green
    Text: Grey
- Add animation
    - Popup:
        grow should start from where click originated
        shrink should end at center of that div
    - Form:
        shake submit button if there is an error
    - Archive:
        on archive it should shrink the popup to the archive tab location



## API DOCS:

### GET /emails/<str:mailbox>
    mailbox == inbox, sent, or archive
    returns JSON of all emails in that category in reverse chrono order
        if no emails returns empty array
        if no mailbox returns {"error": "Invalid mailbox"}
    Input
```js 
    fetch("/emails/inbox")
    .then(response => response.json())
    .then(emails => {
        // Print emails
        console.log(emails)
    })
```
    Output
```js
    [
        {
            "id": 100,
            "sender": "foo@example.com",
            "recipients": ["bar@example.com"],
            "subject": "Hello!",
            "body": "Hello, world!",
            "timestamp": "Jan 2 2020, 12:00 AM",
            "read": false,
            "archived": false
        },
        {
            "id": 95,
            "sender": "baz@example.com",
            "recipients": ["bar@example.com"],
            "subject": "Meeting Tomorrow",
            "body": "What time are we meeting?",
            "timestamp": "Jan 1 2020, 12:00 AM",
            "read": true,
            "archived": false
        }
    ]
```

### GET /emails/<int:email_id>
    email_id == int of id (obvs)
    returns JSON of that email
        if none returns 404 Not Found & {"error":"email not found"}

    Input
```js
    fetch("/emails/100")
    .then(response => response.json())
    .then(emails => {
        // Print emails
        console.log(emails)
    })
```
    Output
```js
    {
        "id": 100,
        "sender": "foo@example.com",
        "recipients": ["bar@example.com"],
        "subject": "Hello!",
        "body": "Hello, world!",
        "timestamp": "Jan 2 2020, 12:00 AM",
        "read": false,
        "archived": false
    }
```

### POST /emails
    Send emails to the server
    Requries - recipents, subject, body

    Input
```js
    fetch("/emails", {
        method: "POST",
        body: JSON.stringify({
            recipents: "name@example.com",
            subject: "Meeting time",
            body: "How about we meet tomorrow at 3pm?"
        })
    })
    .then(response => response.json())
    .then(result => {
        //Print results
        console.log(result)
    })
```
    Output
```js
    //200 OK
    {"message": "Email sent successfully"}
    //400 ERROR
    {"error": "Atleast One recipent required"}
    {"error": "User with email ________ does not exist"}
```

### PUT /emails/<int:email_id>
    mark email as read/unread | archived/unarchived

    Input
```js
    fetch("/emails/100", {
        method: "PUT",
        body: JSON,stringify({
            read: true/false
            archived: true/false
        })
    })
```
    No Output