Single page apps
    use js and css to display different content on same page,
    using js & django can dynamically load content

    Can use window.onpopstate & history.pushState() to store 'states' in browser history that user can jump between

Docment object
    is the whole page and the content on it

    document.body.offsetHeight

Window Object
    window.innerHeight/innerWidth
    Can be used to get the dimension of the users window view

    window.scrollY
    distance from top of page 

    document.body.offsetHeight = total page length
    window.scrollY + window.innerHeight = how much user scrolled already

    if document.body.offsetHeight == window.scrollY + window.innerHeight -- user is at the bottom of the page

    using this you can do stuff when the user gets to the bottom of the page -- infinite scroll

    ***USE SCROLL PROJECT FROM SRC TO GET TEMPLATE FOR INIFINTE SCROLL***

React
    Imperative Programming
        Give computer steps on what to do 

        <h1>1</h1>

        let num = parseInt(document.QuerySelector('h1').innerHTML)
        num += 1
        document.QuerySelector('h1').innerHTML = num

    Declarative Programming 
        Describe what state should be displayed and in what form

        <h1>{ num }</h1>

        num += 1

        
    