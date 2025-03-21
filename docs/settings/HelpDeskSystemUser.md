**Technical Name:** HelpDeskSystemUser

**Category:** Workflow

**Default Value:**

**Impact Level:** High

**Description:** The HelpDeskSystemUser parameter is designated for specifying the system user account utilized for integration with external help desk systems, such as ServiceNow. It dictates the identity under which automated service requests are opened, ensuring appropriate permissions and access controls are applied.

**Business Impact:** Proper configuration of the HelpDeskSystemUser parameter ensures that automated workflows that require ticket creation or service requests in external systems (like ServiceNow) are processed smoothly, without interruption. This configuration guarantees that requests are sanctioned and traceable to a specific system user, thereby maintaining audit trails and aligning with compliance requirements.

**Technical Impact when configured:** Correct configuration ensures seamless integration with external service management systems, facilitating automatic ticket or service request generation directly from the Pathlock GRC platform. Misconfiguration can lead to permission errors, failed requests, or audit trail inconsistencies.

**Examples Scenario:** When an anomaly or non-compliant activity is detected within the GRC platform, the system automatically triggers a workflow action (OpenServiceNowServiceRequest) to open a ticket in ServiceNow. The HelpDeskSystemUser parameter ensures that this ticket is opened under a designated system user account, complying with predefined security and operational protocols.

**Related Settings:** 

- ServiceNowProvider
- WorkflowInstance

**Applicable Workflows Actions:** 

- OpenServiceNowServiceRequest

**Best Practices:** configure when integrating with external systems for workflow automation. Avoid when the external system does not require specific user context or where using a generic user would suffice. Ensure that the HelpDeskSystemUser has the necessary permissions in the external system to perform actions (open tickets, create requests, etc.) as intended.