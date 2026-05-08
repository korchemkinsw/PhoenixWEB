const BASE_URL = "http://127.0.0.1:8000"

class Api {
  constructor (url, headers) {
    this._url = url
    this._headers = headers
  }

  BackUrl = {
    company: BASE_URL+"/phoenix/company",
    panels: BASE_URL+"/phoenix/panels",
  }

  getData (url, name, setData, setError) {
    return fetch(url)
      .then((response) => {
        if (response.ok) {
          return response;
        }
        throw new Error(`${response.status} - ${response.statusText}`)
      })
      .then((response) => response.json())
      .then((name) => setData(name))
      .then((error) => setError(error));
  }
}

export default new Api(process.env.API_URL || 'http://localhost', {'content-type': 'application/json'})