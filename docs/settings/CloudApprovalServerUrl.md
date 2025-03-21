# Cloud Approval Server Url

**Technical Name:** CloudApprovalServerUrl

**Category:** Workflow

**Default Value:**

**Impact Level:** High

**Description:**

The Cloud Approval Server Url parameter specifies the URL of the server that handles approval processes in the Pathlock Cloud GRC platform. It is used to configure where approval requests are sent and managed within the cloud environment.

**Business Impact:**

Configuring this URL correctly is crucial for enabling and streamlining workflow approvals. It directly affects the efficiency and security of approval processes, which are integral to compliance, risk management, and security policies within an organization.

**Technical Impact when configured:**

When properly configured, the Cloud Approval Server Url ensures that workflow steps requiring approval are correctly routed to the designated cloud server, facilitating timely and secure processing of approvals. Misconfiguration may result in the inability to process approvals, leading to workflow disruptions and potential compliance issues.

**Examples Scenario:**

A company has implemented Pathlock for managing access requests. When an employee requests access to a sensitive system, the request is routed to the cloud approval server specified by the Cloud Approval Server Url. The approval server handles the request, ensuring that all necessary approvals are obtained before access is granted, ensuring compliance with the company's internal access control policies.

**Related Settings:**

- CloudApprovalToken

**Best Practices:** configure when setting up or modifying workflow processes that require cloud-based approvals to ensure secure and efficient handling. Avoid when the approval process is managed locally or does not require cloud-based routing.