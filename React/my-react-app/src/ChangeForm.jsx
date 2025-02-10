import React, {useState} from 'react'

function ChangeForm() {

    const [name, setName] = useState("Name")
    const [quantity, setQuantity] = useState(0)
    const [comment, setComment] = useState("")
    const [payment, setPayment] = useState("")
    const [shipping, setShipping] = useState("")


    function handleNameChange(e) {
        setName(e.target.value)
    }

    function handleQuantityChange(e) {
        setQuantity(e.target.value)
    }

    function handleCommentChange(e) {
        setComment(e.target.value)
    }

    function handlePaymentChange(e) {
        setPayment(e.target.value)
    }

    function handleShippingChange(e) {
        setShipping(e.target.value)
    }

    // Wow



    return(
        <>
            <p>Name: {name}</p>
            <input placeholder={name} onChange={handleNameChange} type='text'></input>

            <p>Quantity: {quantity}</p>
            <input placeholder={quantity} onChange={handleQuantityChange} type='number'></input>
            <br/>
            <textarea value={comment} onChange={handleCommentChange} placeholder="Enter Instructions"></textarea>
            <p>Comment: {comment}</p>
            <br/>

            <select value={payment} onChange={handlePaymentChange}>
                <option value="">Select an option</option>
                <option value="VISA">Visa</option>
                <option value="MC">Master Card</option>
                <option value="AMEX">American Express</option>
                <option value="GIFT">Gift Card</option>
            </select>
            <p>Payment Type: {payment}</p>
            <br/>
            <label>
                <input type="radio" value="Pick Up" checked={shipping === "Pick Up"} onChange={handleShippingChange}></input>
                Pick Up
            </label>
            <label>
                <input type="radio" value="Delivery" checked={shipping === "Delivery"} onChange={handleShippingChange}></input>
                Delivery
            </label>
            <p>Shipping Type: {shipping}</p>
        </>


    )

}

export default ChangeForm

