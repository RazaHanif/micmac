import PropTypes from 'prop-types'

function PropList(props) {

    const cat = props.category
    
    const itemList = props.items

    const listItems = itemList.map(item => <li key={item.id}>{item.name} - {item.calories}</li>)
    

    return (
        <>
            <h3>{cat}</h3>
            <ol>{listItems}</ol>
        </>
    )

}

export default PropList