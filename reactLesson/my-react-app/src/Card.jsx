import profilePic from './assets/Mystic.png'

function Card() {
  
    return(
        <>
            <div className="card">
                <img src={profilePic} alt="profile picture"></img>
                <h2>Raza Hanif</h2>
                <p>Start Up - Founder</p>
                
            </div>
            <br></br>
        </>
    );
}

export default Card
