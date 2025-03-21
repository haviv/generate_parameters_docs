**Help Desk System Password**

**Technical Name:** HelpDeskSystemPassword

**Category:** Security

**Default Value:**

**Impact Level:** High

**Description:** The `HelpDeskSystemPassword` parameter is utilized for authenticating and interfacing with external help desk systems, such as ServiceNow. It is essential for ensuring secure and authorized access to create or update service requests via automated workflows within the Pathlock Cloud GRC platform.

**Business Impact:** The security and integrity of the help desk operations are directly impacted by how this password is managed. Improper handling or unauthorized access to this password can lead to security breaches, unauthorized access to sensitive information, or disruptions in automated workflow processes.

**Technical Impact when configured:** Secure configuration enables automated processes to interact with help desk systems like ServiceNow, facilitating the creation and synchronization of tickets based on specific triggers or conditions within the GRC workflows. It ensures that sensitive operations requiring authentication are executed securely and efficiently.

**Examples Scenario:** When an anomaly or a risk is detected within the GRC platform, such as a potential segregation of duties (SOD) conflict, an automated workflow can trigger the creation of a ServiceNow ticket to address the issue. The `HelpDeskSystemPassword` ensures that this process is securely authenticated, allowing for the issue to be logged and addressed appropriately within the help desk system.

**Related Settings:** WorkflowInstance, ServiceNowTicketCustomWorkflowValidation, OpenTicket

**Applicable Workflows Actions:** 
- OpenServiceNowServiceRequest
- RunCustomMethod

**Best Practices:** 
- **configure when** setting up automated workflows that require secure interaction with external service management systems like ServiceNow.
- **avoid when** the credentials might be exposed to non-secure environments or if there is no requirement for automated ticket creation or management through external systems.