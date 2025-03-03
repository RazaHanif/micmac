import React, { useEffect, useState } from 'react';

const LoginPage = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const [data, setData] = useState();
    const [csrf, setCsrf] = useState();

    useEffect(() => {
        fetch('http://127.0.0.1:8000/token/', {
            method: 'GET',
            credentials: 'include',
        })
        .then (response => {
            if (response.status != 200){
                const err = new Error(response.status)
                err.name = 'Getting CSRF'
                throw err
            }
        return response.json()
        })
        .then(data => {
            setCsrf(data.csrfToken)
        })
    }, [])

    const handleUsernameChange = (e) => {
        setUsername(e.target.value)
    }

    const handlePasswordChange = (e) => {
        setPassword(e.target.value)
    }

    const handleSubmit = (e) => {
        e.preventDefault();

        fetch('http://127.0.0.1:8000/login/', { 
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrf,
            },
            body: JSON.stringify({
                username,
                password,
            }),
            credentials: 'include'
        })
        .then (response => {
            if (response.status != 200){
                const err = new Error(response.status)
                err.name = 'Logging In'
                throw err
            }
            
            return response.json()
        })
        .then(data => {
            setData(data)
        })
        .catch(err => {
            console.error('Error Logging In', err)
        })

        console.log(`username:${username} -- password:${password} -- csrf:${csrf}`)
        console.log(data)
    };
        

    return (
        <div className="login-container">
            <h2>Login</h2>

            {/* Error message (if any) */}
            {errorMessage && <div className="error">{errorMessage}</div>}

            <form onSubmit={handleSubmit} method="POST">
                <div className="form-group">
                    <label htmlFor="username">Username</label>
                    <input
                        type="text"
                        id="username"
                        name="username"
                        value={username}
                        onChange={handleUsernameChange}
                        required
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="password">Password</label>
                    <input
                        type="password"
                        id="password"
                        name="password"
                        value={password}
                        onChange={handlePasswordChange}
                        required
                    />
                </div>

                <div className="form-group">
                    <button type="submit">Log in</button>
                </div>

                <div className="form-links">
                    {/* Links for password reset and registration */}
                    <a href="/password-reset/">Forgot your password?</a><br />
                    <a href="/register/">Don't have an account? Sign up</a>
                </div>
            </form>
        </div>
    );
};

export default LoginPage;
