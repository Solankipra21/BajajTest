import requests


def send_post_request():
    url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
    payload = {
        "name": "Prasun Solanki",
        "regNo": "0827AL221102",
        "email": "prasunsolanki220874@acropolis.in"
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data['webhook'], data['accessToken']
    else:
        raise Exception(f"Failed to generate webhook: {response.status_code} - {response.text}")

webhook, accessToken = send_post_request()

access_token = accessToken


url = 'https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON'


headers = {
    "Authorization": access_token,
    "Content-Type": "application/json"
}


body = {
    "finalQuery": "SELECT e1.EMP_ID, e1.FIRST_NAME, e1.LAST_NAME, d.DEPARTMENT_NAME, COUNT(e2.EMP_ID) AS YOUNGER_EMPLOYEES_COUNT FROM EMPLOYEE e1 JOIN DEPARTMENT d ON e1.DEPARTMENT = d.DEPARTMENT_ID LEFT JOIN EMPLOYEE e2 ON e1.DEPARTMENT = e2.DEPARTMENT AND e2.DOB > e1.DOB GROUP BY e1.EMP_ID, e1.FIRST_NAME, e1.LAST_NAME, d.DEPARTMENT_NAME ORDER BY e1.EMP_ID DESC;"
}


response = requests.post(url, headers=headers, json=body)


