import React, { useEffect, useState } from 'react';

const LoginPage = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const [data, setData] = useState();

    const handleUsernameChange = (e) => {
        setUsername(e.target.value)
    }

    const handlePasswordChange = (e) => {
        setPassword(e.target.value)
    }

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await fetch('http://127.0.0.1:8000/token/', { // Simple JWT endpoint
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    username,
                    password,
                }),
            });

            if (response.ok) {
                const data = await response.json();
                // Store access token and refresh token (e.g., in localStorage)
                localStorage.setItem('access_token', data.access_token);
                localStorage.setItem('refresh_token', data.refresh_token);
                // Redirect or update state as needed
            } else {
                const errorData = await response.status;
                setErrorMessage(errorData || 'Invalid credentials');
            }
        } catch (error) {
            console.error('Error logging in:', error);
            setErrorMessage('An error occurred');
        }
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
