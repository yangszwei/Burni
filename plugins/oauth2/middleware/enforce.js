const config = require('../../config').pluginsConfig;

/**
 * Verify the access token against the OIDC server.
 *
 * @param {string} accessToken
 * @return {Promise<boolean>}
 */
const verifyToken = async (accessToken) => {
    const url = new URL(config.server.url);
    url.pathname = `/realms/${config.server.realm}/protocol/openid-connect/token/introspect`;

    const data = new FormData();
    data.append('client_id', config.server.clientId);
    data.append('client_secret', config.server.clientSecret);
    data.append('token', accessToken);

    try {
        const response = await fetch(url, { method: 'POST', body: data });
        if (!response.ok) {
            return false;
        }
    } catch (e) {
        console.error("Failed to verify token: " + e);
        return false;
    }
};

/**
 * @type {import("express").RequestHandler}
 */
module.exports = async (req, res, next) => {
    const accessToken = req.header('Authorization').replace(/Bearer /, '');
    if (!await verifyToken(accessToken)) {
        return false;
    }

    await next();
};
