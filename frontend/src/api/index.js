class Api {
  constructor(url, headers) {
    this._url = url
    this._headers = headers
  }

  getCompanyList(setList, setError) {
    return fetch(
      'http://127.0.0.1:8000/phoenix/company',
      {
        method: 'GET',
      })
      .then((response) => {
        if (response.ok) {
          return response;
        }
        throw new Error(`${response.status} - ${response.statusText}`)
      })
      .then((response) => response.json())
      .then((data) => setList(data))
      .then((error) => setError(error));
    }

  getGroupsCompanyList(setList, setError, company_id) {
    return fetch(
      `http://127.0.0.1:8000/phoenix/company/groups/${company_id}`,
      {
        method: 'GET',
      })
      .then((response) => {
        if (response.ok) {
          return response;
        }
        throw new Error(`${response.status} - ${response.statusText}`)
      })
      .then((response) => response.json())
      .then((data) => setList(data))
      .then((error) => setError(error));
    }

  getCompany(setCard, setError, company_id) {
    return fetch(
      `http://127.0.0.1:8000/phoenix/company/${company_id}`,
      {
        method: 'GET',
      })
      .then((response) => {
        if (response.ok) {
          return response;
        }
        throw new Error(`${response.status} - ${response.statusText}`)
      })
      .then((response) => response.json())
      .then((data) => setCard(data))
      .then((error) => setError(error));
    }
}

export default new Api(process.env.API_URL || 'http://localhost', { 'content-type': 'application/json' })