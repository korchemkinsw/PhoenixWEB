class Api {
  constructor(url, headers) {
    this._url = url
    this._headers = headers
  }

  getCompanyList(setList, setError) {
    return fetch(
      '/phoenix/company/',
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
      `/phoenix/company/groups/${company_id}/`,
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

    getDetailCompany(setCard, setError, company_id) {
      return fetch(
        `/phoenix/company/detail/${company_id}/`,
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

  getResponseTeam(setTeams, setError) {
    return fetch(
      '/phoenix/rrteams/',
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
      .then((data) => setTeams(data))
      .then((error) => setError(error));
    }
}

export default new Api(process.env.API_URL || 'http://localhost', { 'content-type': 'application/json' });
