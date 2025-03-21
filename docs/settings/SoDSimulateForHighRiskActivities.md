# SoD Simulate For High Risk Activities

**Technical Name:** SoDSimulateForHighRiskActivities

**Category:** SOD

**Default Value:**

**Impact Level:** High

**Description:**

The `SoDSimulateForHighRiskActivities` parameter is designed to enable simulation capabilities within the Pathlock Cloud GRC platform, focusing specifically on Separation of Duties (SoD) conflicts for high-risk activities. By leveraging this parameter, organizations can proactively identify and mitigate potential security risks associated with conflicting roles and permissions, ensuring compliance with internal and external regulatory requirements.

**Business Impact:**

Effective configuration of this parameter significantly enhances an organization's security posture by preventing unauthorized access and reducing the potential for fraud. It facilitates stringent compliance processes by ensuring that critical activities are only performed by authorized personnel, minimizing risks associated with SoD violations.

**Technical Impact when configured:**

When enabled, the `SoDSimulateForHighRiskActivities` parameter allows for the simulation of access rights within high-risk areas of the system. This proactive measure helps in assessing potential SoD conflicts before they occur in real-world scenarios. It supports a more granular and proactive approach to risk management by identifying and addressing vulnerabilities in the authorization framework.

**Examples Scenario:**

Let's say an organization wants to assign new roles within its ERP system but needs to ensure these changes do not introduce any SoD conflicts. By leveraging `SoDSimulateForHighRiskActivities`, the system administrators can simulate these changes to spot potential conflicts among high-risk activities, thus ensuring that roles are assigned in compliance with the organization's internal controls and external regulatory obligations.

**Related Settings:**

- UseGroupNameAsActivityInActiveDirectory

**Best Practices:** 

- **Configure when:** Implementing or modifying roles and permissions associated with high-risk activities, or when compliance requirements necessitate rigorous SoD controls.
- **Avoid when:** The operational overhead or performance impact of simulation outweighs the security or compliance benefits, although this is rare given the high stakes of SoD conflicts in critical activities.