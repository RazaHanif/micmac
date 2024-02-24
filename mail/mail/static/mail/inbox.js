document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', () => compose_email());
	document.querySelector('#email-button').addEventListener('click', close_popup);

  // By default, load the inbox
  load_mailbox('inbox');
});

// declaring variables to use later for add/remove event listeners
let readToggleFunction
let archiveToggleFunction
let replyFunction

// read_toggle & archive_toggle is the same shit but different buttons/db values

// Toggle read status of email, updates db & css
function read_toggle(email_id) {
	let btn = document.querySelector('#read-toggle')

	// Get current email.read value
	// Toggle read value as !email.read
	// After all that close the popup and redirect to inbox
	fetch(`/emails/${email_id}`)
	.then(response => response.json())
	.then(email => {
		fetch(`/emails/${email_id}`, {
			method: 'PUT',
			body: JSON.stringify({
				read: !email.read
			})
		})
		.then(() => {
			close_popup()
			load_mailbox('inbox')
		})
	})
}

// Toggle archive status of email, updates db & css
function archive_toggle(email_id) {
	let btn = document.querySelector('#archive-toggle')

		// Get current email.archive value
	// Toggle archive value as !email.archive
	// After all that close the popup and redirect to inbox
	fetch(`/emails/${email_id}`)
	.then(response => response.json())
	.then(email => {
		fetch(`/emails/${email_id}`, {
			method: 'PUT',
			body: JSON.stringify({
				archived: !email.archived
			})
		})
		.then(() => {
			close_popup()
			load_mailbox('inbox')
		})
	})
}

// email_id passed as arg
function open_popup(email_id) {

	// Get JSON for the email and fill in the values before opening popup
	fetch(`/emails/${email_id}`)
	.then(response => response.json())
	.then(email => {
		// Update all values in popup
		document.querySelector('#email-subject').innerHTML = email.subject
		document.querySelector('#email-sender').innerHTML = email.sender
		document.querySelector('#email-time').innerHTML = email.timestamp
		document.querySelector('#email-body').innerHTML = email.body
		
		// Display multiple emails
		email.recipients.forEach((user) => {
			document.querySelector('#email-recipients').innerHTML += `${user} `
		})

		// Eventlisteners for the toggle buttons
		// Done this way to make removeEventListener function properly on close
		readToggleFunction = () => read_toggle(email.id)
		document.querySelector('#read-toggle').addEventListener('click', readToggleFunction);
		archiveToggleFunction = () => archive_toggle(email.id)
		document.querySelector('#archive-toggle').addEventListener('click', archiveToggleFunction);
		replyFunction = () => {
			close_popup()
			compose_email(email.id)
		}
		document.querySelector('#reply').addEventListener('click', replyFunction)

		// Update button css
		if (email.read) {
			document.querySelector('#read-toggle').className = 'toggle-btn clicked'
		}
		if (email.archived) {
			document.querySelector('#archive-toggle').className = 'toggle-btn clicked'
		}
		console.log(email)
	})

	// Run animation to display the popup
	let fill = document.querySelector('#fill-layer')
	fill.addEventListener('animationend', () => {
		fill.style.visibility = 'visible'
	})
	fill.style.animationName = 'softOpen'
	fill.style.animationPlayState = 'running'
	
	console.log("Open", id)
}

// Close the popup when the 'x' button is clicked
function close_popup() {
	// Reset all the values for next email
	document.querySelector('#email-subject').innerHTML = ''
	document.querySelector('#email-sender').innerHTML = ''
	document.querySelector('#email-recipients').innerHTML = ''
	document.querySelector('#email-time').innerHTML = ''
	document.querySelector('#email-body').innerHTML = ''

	// Remove eventlisteners and reset css styling
	document.querySelector('#read-toggle').removeEventListener('click', readToggleFunction)
	document.querySelector('#read-toggle').className = 'toggle-btn'
	document.querySelector('#archive-toggle').removeEventListener('click', archiveToggleFunction)
	document.querySelector('#archive-toggle').className = 'toggle-btn'
	document.querySelector('#reply').removeEventListener('click', replyFunction)

	// Run animation to close the popup
	let fill = document.querySelector('#fill-layer')
	fill.addEventListener('animationend', () => {
		fill.style.visibility = 'hidden'
	})
	fill.style.animationName = 'softClose'
	fill.style.animationPlayState = 'running'

	console.log("Close")
}


function compose_email(email_id=0) {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
	
	document.querySelector('#recipients-error').style.opacity = 0;
	if (email_id === 0) {
		// Clear out composition fields
		document.querySelector('#compose-recipients').value = '';
		document.querySelector('#compose-subject').value = '';
		document.querySelector('#compose-body').value = '';
	} else {
		fetch(`/emails/${email_id}`)
		.then(response => response.json())
		.then(email => {
			document.querySelector('#compose-recipients').value = email.sender
			document.querySelector('#compose-subject').value = `RE: ${email.subject}`
			document.querySelector('#compose-body').value = `On ${email.timestamp} ${email.sender} wrote: ${email.body}\n\n`
		})
	}

  // Add Submit functionailty
  document.querySelector('#compose-form').addEventListener('submit', function(event) {
    event.preventDefault()

    // POST email to send to server
    fetch("/emails", {
      method: "POST",
      body: JSON.stringify({
        recipients: document.querySelector('#compose-recipients').value,
        subject: document.querySelector('#compose-subject').value,
        body: document.querySelector('#compose-body').value
      })
    })
    .then(response => response.json())
    .then(data => {
      if ("message" in data){
        console.log('OK: ', data)
        // Delete this line in prod
        alert(data.message) 
        load_mailbox('inbox')
      } else {
        console.log('Error: ', data.error)
        document.querySelector('#recipients-error').innerHTML = data.error
        document.querySelector('#recipients-error').style.color = "red"
        document.querySelector('#recipients-error').style.opacity = 100
      }
    })
    .catch(error => {
      console.log("oops")
    })
  });
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
	console.log(mailbox)
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
    emails.forEach(email => {
			let output
			switch(mailbox) {
				case "inbox":
					console.log("inbox")
					output = `<p>From: ${email.sender}</p>
											<p>Subject: ${email.subject}</p>
											<p>Time: ${email.timestamp}`
					break;
				case "sent":
					console.log("sent")
					output = `<p>To: ${email.recipients}</p>
											<p>Subject: ${email.subject}</p>
											<p>Time: ${email.timestamp}`
					break;
				case "archive":
					console.log("archive")
					if (email.archived === true) {
						output = `<p>From: ${email.sender}</p>
											<p>Subject: ${email.subject}</p>
											<p>Time: ${email.timestamp}`
					}
					break
				default:
					console.log("how did you get here?", mailbox)
			}

			const element = document.createElement('div')
			element.innerHTML = output
			element.className = 'email_div'
			if (email.read && mailbox === 'inbox') {
				element.className += ' read'
			}
			element.addEventListener('click', () => {
				open_popup(email.id)
			})

			document.querySelector('#emails-view').append(element)
    });
  })
}