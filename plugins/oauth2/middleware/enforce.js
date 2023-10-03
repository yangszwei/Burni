const { oauth2: config } = require('../../config').pluginsConfig;
const fetch = require('node-fetch');

/**
 * Verify the access token against the OIDC server.
 *
 * @param {string} accessToken
 * @return {Promise<boolean>}
 */
const verifyToken = async (accessToken) => {
    const url = new URL(config.server.url);
    url.pathname = `/realms/${config.server.realm}/protocol/openid-connect/token/introspect`;

    const data = {
        client_id: config.server.clientId,
        client_secret: config.server.clientSecret,
        token: accessToken
    }

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams(data)
        });
        if (!response.ok) {
            return false;
        }

        const token = await response.json();

        return token.active;
    } catch (e) {
        console.error("Failed to verify token: " + e);
        return false;
    }
};

/**
 * @type {import("express").RequestHandler}
 */
module.exports = async (req, res, next) => {
    if (!req.path.startsWith('/api')) {
        next();
        return;
    }

    const accessToken = req.header('Authorization')?.replace(/Bearer /, '') ?? '';
    if (!await verifyToken(accessToken)) {
        return res.status(401).send();
    }

    next();
};
