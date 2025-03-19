# Action name: QueryServiceNowTicket

**Category:** Workflow

**Description:**  
The `QueryServiceNowTicket` action automates the process of querying ticket information from ServiceNow, a commonly used help desk system. This action connects to ServiceNow using provided credentials, retrieves detailed information about a specific ticket by its number, and then populates this data into a designated form within the Pathlock Cloud platform. Additionally, it marks the workflow action as completed by setting the appropriate status. This facilitates seamless integration of ticket management processes, enabling users to access and act upon ServiceNow ticket data directly within Pathlock Cloud workflows, enhancing efficiency and streamlining IT service management operations.

**Parameters:**  
- Basic:
  - Name: TicketNumber
  - Description: The unique identifier for the ServiceNow ticket to be queried. This parameter is used to fetch ticket details from the ServiceNow system. It forms the basis of the query sent to ServiceNow's API.
  - Default value: N/A
  - Mandatory: yes

**Business impact:**  
Incorporating ServiceNow ticket information directly into Pathlock Cloud workflows significantly improves operational efficiency for IT service management tasks. By automating the retrieval and processing of ticket data, organizations can reduce manual data entry errors, speed up ticket resolution times, and improve the overall user experience for IT staff and end-users. It enables a clearer audit trail, better compliance practices due to accurate and timely data handling, and enhances risk management by ensuring that issues tracked in ServiceNow are correctly reflected and acted upon within the Pathlock ecosystem.

**Example of usage:**  
In a scenario where an organization uses ServiceNow for IT service management and Pathlock Cloud for identity and access management (IAM), an employee might submit a ticket requesting access to a specific system. An automated workflow in Pathlock can use the `QueryServiceNowTicket` action to retrieve the ticket details based on the ticket number provided by the employee. The workflow can then parse this data to decide on the necessary steps to fulfill the access request, streamlining the process of managing access rights based on IT service tickets.

**Prerequisites:**  
- A valid ServiceNow instance URL, user credentials (username and password) with permissions to access ticket information.
- The “TicketNumber” parameter must be known and provided to the workflow action.
- Proper configuration and connectivity between the Pathlock Cloud platform and the ServiceNow system.

**Error Handling and Troubleshooting:**  
- If a “Ticket not found” error occurs, verify that the “TicketNumber” parameter is correct and corresponds to an existing ticket in the ServiceNow system.
- Authentication errors can occur if the provided ServiceNow credentials are incorrect. Ensure that the username and password are entered correctly and that the account has the necessary permissions to query ticket information.
- Network or connectivity issues may prevent the workflow from connecting to ServiceNow. Check the network connectivity and ensure that the Pathlock Cloud platform can reach the ServiceNow instance URL.

