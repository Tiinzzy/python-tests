import axios from 'axios';

class BackEndConnectionImpl {
    async get_data_from_backaned(componenet, callback) {
        return axios.get('/send-data-to-frontend', {})
            .then(function (response) {
                if (callback) {
                    callback(componenet, response.data);
                }
                return response.data;
            })
            .catch(function (error) {
                console.log(error);
                return false;
            })
    }

}

export default class BackEndConnection {
    static #object = null;

    static INSTANCE() {
        if (BackEndConnection.#object === null) {
            BackEndConnection.#object = new BackEndConnectionImpl();
        }
        return BackEndConnection.#object;
    }

}
