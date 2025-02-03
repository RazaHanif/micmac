import PropTypes from 'prop-types'


function PropCard(props) {
  
    return(
        <>
            <div className="card">
                <h2>Name: {props.name}</h2>
                <p>Age: {props.age}</p>
                <p>Student: {props.isStudent ? "Yes" : "No"}</p>
            </div>
            <br></br>
        </>
    );
}

PropCard.propTypes = {
    name: PropTypes.string,
    age: PropTypes.number,
    isStudent: PropTypes.bool,
}

PropCard.defaultProps = {
    name: "Guest",
    age: 0,
    isStudent: false,
}

export default PropCard
