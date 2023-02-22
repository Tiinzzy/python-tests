import axios from 'axios';

class BackEndConnectionImpl {
    async send_url_to_backend(url, callback) {
        return axios.get("/url-to-txt-and-tokens?url=" + url, {})
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

    async send_text_file_to_backend(query, callback) {
        return axios.post("/file-to-txt-and-tokens", {}, { params: { query: query } })
            .then(response => {
                if (response.status === 200) {
                    if (callback) {
                        callback(response.data);
                    }
                    return response.data;
                } else {
                    return false;
                }
            })
            .catch(error => {
                return false;
            });
    }

    async get_common_words(count, callback) {
        return axios.get("/get-common-words-count?count=" + count, {})
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

    async get_frequency_of_words(count, callback) {
        return axios.get("/get-frequency-of-words?count=" + count, {})
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
