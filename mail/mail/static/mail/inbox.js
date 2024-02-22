document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

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
			switch(mailbox) {
				case "inbox":
					console.log("inbox")
					add_to_page(`<p>From: ${email.sender}</p>
											<p>Subject: ${email.subject}</p>
											<p>Time: ${email.timestamp}`)
					break;
				case "sent":
					console.log("sent")
					add_to_page(`<p>To: ${email.recipients}</p>
											<p>Subject: ${email.subject}</p>
											<p>Time: ${email.timestamp}`)
					// code block
					break;
				case "archive":
					console.log("archive")
					if (email.archived === true) {
						add_to_page(`<p>From: ${email.sender}</p>
											<p>Subject: ${email.subject}</p>
											<p>Time: ${email.timestamp}`)
					}
					break
				default:
					console.log("how did you get here?", mailbox)
			}
    });
  })
}


function add_to_page(obj) {
	const element = document.createElement('div');
	element.innerHTML = obj
	element.style.border = "1px solid black"
	element.style.margin = "5px"
	element.addEventListener('click', function() {
		console.log('This element has been clicked!')
	});
	document.querySelector('#emails-view').append(element);
}