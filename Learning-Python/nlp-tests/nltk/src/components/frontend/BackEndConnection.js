import axios from 'axios';

class BackEndConnectionImpl {
    async send_url_to_backend(url, callback) {
        console.log(url)
        return axios.get('/url-to-txt-and-tokens?url=' + url, {})
            .then(function (response) {
                if (callback) {
                    callback(response.data);
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
