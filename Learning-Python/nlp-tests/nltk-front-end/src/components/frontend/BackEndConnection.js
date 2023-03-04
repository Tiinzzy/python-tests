import axios from 'axios';

class BackEndConnectionImpl {
    #url = null;
    #text = null;

    async send_url_to_backend(url, callback) {
        this.#url = url;
        this.#text = null;
        
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
        this.#url = null;
        this.#text = query.text;

        return axios.post("/file-to-txt-and-tokens", query, {})
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
        return axios.post("/get-common-words-count", { count, url: this.#url, text: this.#text }, {})
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
        return axios.post("/get-frequency-of-words", { count, url: this.#url, text: this.#text }, {})
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

    async get_dispersion_plot_graph(words, callback) {
        return axios.post("/get-graph-of-dispersion-plot", { words, url: this.#url, text: this.#text }, {})
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

    async get_all_words(callback) {
        return axios.post("/get-all-tokens-for-graph", { url: this.#url, text: this.#text }, {})
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
