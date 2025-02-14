import React, { useState } from 'react';

const LoginPage = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();

        // Example of how you might handle the form submission.
        // Replace this with your actual authentication logic.
        if (username === 'admin' && password === 'password') {
            alert('Logged in successfully!');
        } else {
            setErrorMessage('Invalid username or password.');
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
                        onChange={(e) => setUsername(e.target.value)}
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
                        onChange={(e) => setPassword(e.target.value)}
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
