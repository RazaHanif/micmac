function Card() {
    const imgSrc = "https://cdn.jsdelivr.net/npm/twemoji@11.3.0/2/svg/1f9f1.svg"

    const lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit."
  
    return(
        <>
            <div className="card">
                <div className="card-user">
                    <div className="card-user-pic">
                        <img src={imgSrc} alt="profile picture"/>
                    </div>
                    <div className="card-user-name">
                        UserName
                    </div>

                </div>
                <div className="card-post">
                    <div className="card-text">
                        {lorem}
                    </div>
                </div>
                
            </div>
        </>
    );
}

export default Card

