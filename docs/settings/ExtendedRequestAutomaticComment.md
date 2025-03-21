# Extended Request Automatic Comment

**Technical Name:** ExtendedRequestAutomaticComment

**Category:** Workflow

**Default Value:** 1

**Impact Level:** Medium

**Description:**

The Extended Request Automatic Comment parameter is utilized within the Pathlock Cloud GRC platform to automatically determine and append comments to authorization request workflows based on extended request time configuration.

**Business Impact:**

Configuring this parameter appropriately ensures that all extended authorization requests are documented with a timestamp. This aids in auditing and tracking request extensions, thus enhancing the accountability and transparency of the request approval process.

**Technical Impact when configured:**

When configured, this parameter influences the workflow approval process by appending an automatic comment that includes the extended request time. This facilitates better management of authorization requests by providing clear visibility into extensions granted during the approval process.

**Example Scenario:**

Consider a scenario where a user requests access to a sensitive system. The approval process takes longer than anticipated, triggering an extension. With Extended Request Automatic Comment enabled and configured, the workflow automatically annotates the extension with a comment, indicating the extension duration and potentially the reason, if configured to include such details.

**Related Settings:**

- `ExtendedRequestTimeHours`

**Best Practices:** 

- **Configure when:** There is a need for precise tracking and documentation of extended authorization request times within the workflow, to enhance auditability and governance.
- **Avoid when:** Authorization request processes are informal, or there is no requirement from the governance, risk, and compliance (GRC) perspective to document and track request time extensions.