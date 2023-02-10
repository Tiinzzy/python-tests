const axios = require('axios');

axios.defaults.baseURL = 'http://localhost:5000';

class BackEndConnectionImpl {
    async get_wikipedias_relationships(callback) {
        return axios.get('/all-relationships', {})
            .then(function (response) {
                if (callback) {
                    callback(response.data);
                };
                return response.data;
            })
            .catch(function (error) {
                console.log(error);
                return false;
            })
    }

}

module.exports = class BackEndConnection {
    static #object = null;

    static INSTANCE() {
        if (BackEndConnection.#object === null) {
            BackEndConnection.#object = new BackEndConnectionImpl();
        }
        return BackEndConnection.#object;
    }
}
