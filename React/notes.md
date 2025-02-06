###### React Notes

React is a JS library

React components are reusable js/html codes

React uses JSX - JavascriptXML

App.jsx 
    Main page code is stored here
    At the top make sure to import Component from ./Component

    then in App() you can have some info, or you can just return the page within 
    return(
        <>
            <Component><Compenent/>
        </> 
    )

Images
    Can import images from external webpages by making a var with the link then subbing that into the jsx

    const pic = www.pic.com

    <img src={pic}><img/>

    or by getting it from the assets folder locally

    import localPic from './piclocation'

    <img src={localPic}><img/>

Props
    can pass props (args) to a component

    <Component arg1="string" arg2={123} arg3=true><Component>

    in Component code
    
    function Component(props)

    <p>name = {props.name}</p>

    also should include proptypes to get a console log error if the wrong type of prop is passed, along with defualts

    import PropTypes from 'prop-types'

    Component.propTypes = {
        name: PropTypes.string,
    }

    Component.defaultProps = {
        name: "Guest",
    }

Conditonal
    if/else can be used in returns but try to use ternary instead

    condition ? if : else

Lists
    Lists can be manipulated same as js, and you can pass list objs as a prop to the component

onClick
    if a click handler is 
        onClick={func(arg)}
    it will call assoon as the page loads
    to prevent that make it 
        onClick={() => func(arg)}

React Hooks
    function that allows func compoennets to use react features without writing class components (useState, useEffect, useContext...)

useState
    React hook that allows the creation of a stat var AND a setter function to update its value in the DOM
    const [name, setName] = useState("guest")

    setName("name")

onChange
    event handler used with forms
    Triggers a funciton everytime the value changes