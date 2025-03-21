# Enable Apply Changes From Authorization Simulation in Activity to Role

**Technical Name:** EnableApplyChangesFromAuthorizationSimulation

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

Enables the application of changes identified during an authorization simulation directly to the related role configurations within the Pathlock Cloud GRC platform. This feature facilitates dynamic security adjustments based on simulated access scenarios.

**Business Impact:**

Improves security posture by allowing for rapid application of optimized access controls, potentially reducing the risk of excessive permissions and ensuring that roles are only granted the necessary authorizations for their functions. It streamlines the process of updating roles in response to simulation insights, thus enhancing operational efficiency and compliance.

**Technical Impact when configured:**

- Directly applies simulation-recommended changes to role configurations, reducing manual effort and error.
- Helps maintain an optimized least privilege model by adjusting role permissions based on simulated access needs and risks.
- Accelerates the role update process, enabling quicker response to compliance or security policy adjustments.

**Examples Scenario:**

- **Before Configuration:** Administrators manually review authorization simulation reports and apply necessary changes to roles, a time-consuming process with high potential for oversight or errors.
- **After Configuration:** Changes suggested by the authorization simulation are automatically applied to roles, significantly streamlining the role maintenance process, and ensuring that access rights are kept up-to-date with organizational policies and compliance requirements.

**Related Settings:**

- `EmergencyAccessReportTemplateId`
- `EmployeeNumberLength`

**Best Practices:** Configure when aiming to streamline role management and maintain accurate access controls. Avoid when changes require extensive review or when simulations might suggest broad or non-specific adjustments that need manual refinement.