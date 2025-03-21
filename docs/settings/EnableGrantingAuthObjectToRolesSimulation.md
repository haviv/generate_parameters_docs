# Enable Granting Auth Object To Roles Simulation

**Technical Name:** EnableGrantingAuthObjectToRolesSimulation

**Category:** Workflow Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The Enable Granting Auth Object To Roles Simulation parameter is designed to support the configuration of simulation scenarios within the Pathlock Cloud GRC platform. This functionality is crucial for analyzing the potential impacts of granting specific authorization objects to roles before the changes are actually implemented within live systems.

**Business Impact:**

Enabling this parameter allows organizations to proactively assess and mitigate risks associated with access control changes. By simulating the assignment of authorization objects to roles, security administrators can identify potential segregation of duties (SoD) conflicts, unauthorized access risks, or compliance violations, thereby enhancing the organization's security posture and ensuring compliance with regulatory standards.

**Technical Impact when configured:**

When enabled, this parameter affects the system's capability to simulate the granting of authorization objects to roles. These simulations can help in understanding the implications of such changes on system access and permissions without making any real-time changes to the system's configuration.

**Example Scenario:**

Consider a scenario where a company wants to grant additional access rights to a role that is assigned to users in the finance department. Before applying this change, by enabling the simulation feature, the security team can evaluate if granting these access rights would violate any SoD policies or grant unintended excessive permissions, potentially putting sensitive data at risk.

**Related Settings:**

- SendWorkflowReminderForRequests
- SendWorkflowReminderForAuthorizationReviews

**Best Practices:** 

- Configure when planning significant changes in role-based access controls or when introducing new roles and authorization objects to ensure these changes do not introduce security vulnerabilities or compliance issues.
  
- Avoid when the simulation results are consistently ignored or not used for decision-making, as this may lead to operational inefficiencies and unnecessary processing overhead.