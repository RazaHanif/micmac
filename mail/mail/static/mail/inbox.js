document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
	document.querySelector('#email-button').addEventListener('click', close_popup);
	document.querySelector('#read-toggle').addEventListener('click', read_toggle);
	document.querySelector('#archive-toggle').addEventListener('click', archive_toggle);

  // By default, load the inbox
  load_mailbox('inbox');
});


// Toggle read status of email, updates db & css
function read_toggle() {
	let btn = document.querySelector('#read-toggle')
	
	if (btn.classList.contains('clicked')) {
		btn.className = 'toggle-btn'
	} else {
		btn.className = 'toggle-btn clicked'
	}
}

// Toggle archive status of email, updates db & css
function archive_toggle() {
	let btn = document.querySelector('#archive-toggle')

	if (btn.classList.contains('clicked')) {
		btn.className = 'toggle-btn'
	} else {
		btn.className = 'toggle-btn clicked'
	}
}


function close_popup() {
	document.querySelector('#email-subject').innerHTML = ''
	document.querySelector('#email-sender').innerHTML = ''
	document.querySelector('#email-recipients').innerHTML = ''
	document.querySelector('#email-time').innerHTML = ''
	document.querySelector('#email-body').innerHTML = ''
	document.querySelector('#read-toggle').className = 'toggle-btn'
	document.querySelector('#archive-toggle').className = 'toggle-btn'

	let fill = document.querySelector('#fill-layer')
	fill.addEventListener('animationend', () => {
		fill.style.visibility = 'hidden'
	})
	fill.style.animationName = 'softClose'
	fill.style.animationPlayState = 'running'

	console.log("Close")
}

// email_id passed as arg
function open_popup(id) {
	fetch(`/emails/${id}`)
	.then(response => response.json())
	.then(email => {
		document.querySelector('#email-subject').innerHTML = email.subject
		document.querySelector('#email-sender').innerHTML = email.sender
		email.recipients.forEach((user) => {
			document.querySelector('#email-recipients').innerHTML += `${user} `
		})
		document.querySelector('#email-time').innerHTML = email.timestamp
		document.querySelector('#email-body').innerHTML = email.body
		if (email.read) {
			document.querySelector('#read-toggle').className = 'toggle-btn clicked'
		}
		if (email.archived) {
			document.querySelector('#archive-toggle').className = 'toggle-btn clicked'
		}
			// Print emails
			console.log(email)
	})
	let fill = document.querySelector('#fill-layer')
	fill.addEventListener('animationend', () => {
		fill.style.visibility = 'visible'
	})
	fill.style.animationName = 'softOpen'
	fill.style.animationPlayState = 'running'
	
	console.log("Open", id)
}

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#recipients-error').style.opacity = 0;
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

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