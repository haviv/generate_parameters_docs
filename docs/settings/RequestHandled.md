# Request Handled

**Technical Name:** RequestHandled

**Category:** Workflow

**Default Value:** Not Applicable

**Impact Level:** Medium

**Description:**

The `RequestHandled` parameter is designed to ensure that requests to the Cloud Approvals Server are properly managed and directed based on customer-specific keys. It facilitates the routing of approval requests to the appropriate handler page, contingent upon the presence of the `CustomerKey` parameter.

**Business Impact:**

Effective management of request handling can streamline the approval process, enhancing operational efficiency and ensuring requests are processed in a timely and secure manner. Mismanagement or errors related to this parameter could result in delays, improper request routing, and potential security concerns.

**Technical Impact when configured:**

When correctly configured, `RequestHandled` contributes to a robust and reliable approval process by ensuring requests are only processed after verifying the existence of a customer key. This verification process safeguards against unauthorized access and ensures that each request is appropriately handled according to customer-specific workflows.

**Examples Scenario:**

- A company uses the Pathlock Cloud GRC platform for handling approvals of risk assessment documents. The `RequestHandled` parameter ensures that each approval request is correctly routed to the designated user or department based on the customer key, thereby streamlining the workflow and improving efficiency.

**Related Settings:** N/A

**Applicable Workflows Actions:** N/A

**Best Practices:** 

- **Configure when**: Setting up approval workflows that require differentiation and specific handling based on customer or user keys. This ensures that each request is processed through the correct workflow path.
  
- **Avoid when**: Implementation does not involve multi-tenant environments or when approval requests do not need to be distinguished by unique identifiers. Misconfiguration could lead to unnecessary complexity and potential routing errors.