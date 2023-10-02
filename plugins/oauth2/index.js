const enforce = require("./middleware/enforce");

/**
 * @param {import("express").Express} app
 */
module.exports = (app) => {
    app.use('/api', enforce);
};
