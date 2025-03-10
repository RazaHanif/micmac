// get comfertable using ternary instead of if else

import PropTypes from 'prop-types'


function UserGreeting(props) {

    const userTrue = <h2 className="user-true">
                        Welcome {props.username}
                    </h2>

    const userFalse = <h2 className="user-false">
                            Please Log In
                        </h2>
    
    return(props.isLoggedIn ? userTrue : userFalse)
    
}

UserGreeting.proptypes = {
    isLoggedIn: PropTypes.bool,
    username: PropTypes.string,
}

UserGreeting.defaultProps = {
    username: "Guest",
    isLoggedIn: false,
}


export default UserGreeting