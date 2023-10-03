module.exports.pluginsConfig = {
    token_auth: {
        enable: false,
        before: true,
        routers: [
            {
                method: "get",
                path: "/fhir/:resourceType"
            }
        ],
        admin: {
            loginPath: "",
            username: "",
            password: ""
        },
        jwt: {
            secretKey: ""
        }
    },
    oauth2: {
        enable: false,
        before: true,
        server: {
            url: "",
            realm: "",
            clientId: "",
            clientSecret: ""
        }
    },
    checkReference: {
        enable: true,
        before: true
    }
};